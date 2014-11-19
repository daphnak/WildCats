#!/usr/bin/env python
import rospy
from tf2_msgs.msg import TFMessage
from time import time
from  std_msgs.msg import String
from geometry_msgs.msg import *

PEOPLE_MAP = {}
PUB_POSE = None

class Person:
    VALID_BODY_PARTS = set(["head", "left_hand", "right_hand"])
    POSE_THRESHOLD = 5

    def __init__(self, personNum):
        self.personNum = personNum
        self.parts = {}
        self.poseHit = 0
        self.hit = False

    def addBodyPart(self, partName, position):
        if partName not in Person.VALID_BODY_PARTS:
            # print partName, " is not a valid body part"
            pass
        else:
            # print "nice"
            self.parts[partName] = position
        self.detectPose()

    # pose is both hands above head
    def detectPose(self):
        for part in Person.VALID_BODY_PARTS:
            if part not in self.parts:
                self.poseHit = 0
                self.hit = False
                return

        headZ = self.parts['head'].z
        leftHandZ = self.parts['left_hand'].z
        rightHandZ = self.parts['right_hand'].z

        if headZ < leftHandZ and headZ < rightHandZ:
            self.poseHit += 1
            # if self.poseDetected() and not self.hit:
            #     self.hit = True
            #     # print "Nice", self.poseHit
            # print "Pose detected: pose foo" #, self.poseHit 
        else:
            self.hit = False
            self.poseHit = 0
            # print "\tNo pose detected"

    def poseDetected(self):
        return True if self.poseHit > Person.POSE_THRESHOLD else False

    def getPose(self):
        p = Point()
        p.x = self.parts["head"].x
        p.y = self.parts["head"].y
        p.z = self.parts["head"].z

        return p
         

def messageHandler(message):
    global PEOPLE_MAP
    # print "***"
    position = message.transforms[0].transform.translation
    # print position
    partNameRaw = message.transforms[0].child_frame_id

    partNameArray = partNameRaw.rpartition("_") # splits on LAST occurrence of underscore. Returns: ["name", "_", "num"]
    partName = partNameArray[0]
    personNum = partNameArray[2]

    # print partName
    # print personNum

    person = None
    if personNum in PEOPLE_MAP:
        person = PEOPLE_MAP[personNum]
    else:
        person = Person(personNum)
        PEOPLE_MAP[personNum] = person

    person.addBodyPart(partName, position)

    if person.poseDetected():
        pose = person.getPose()
        PUB_POSE.publish(pose)



def wildcat():
    rospy.init_node('poseDetector', anonymous=True)
    rospy.Subscriber('/tf', TFMessage, messageHandler)
    global PUB_POSE
    PUB_POSE = rospy.Publisher('/wildcat_detected_poses', Point)
    rospy.spin()


if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass



#     rosmsg show TFMessage
# [tf2_msgs/TFMessage]:

# geometry_msgs/TransformStamped[] transforms
#   std_msgs/Header header
#     uint32 seq
#     time stamp
#     string frame_id
#   string child_frame_id
#   geometry_msgs/Transform transform
#     geometry_msgs/Vector3 translation
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Quaternion rotation
#       float64 x
#       float64 y
#       float64 z
#       float64 w
