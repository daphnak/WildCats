#!/usr/bin/env python
import rospy
import math
import actionlib

from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseGoal

from tf.transformations import euler_from_quaternion, quaternion_from_euler


PUB_GOAL = None
PUBD = False

def callback(data):
    sendToOnce()

def sendToOnce():
    global PUB_GOAL, PUBD
    # if PUBD:
    #     return

    # PUBD = True

    DISTANCE_THRESHOLD = .1
    print'********'
    # x = data.pose.pose.position.x
    # y = data.pose.pose.position.y
    
    # if math.sqrt(x**2+y**2) < DISTANCE_THRESHOLD:
    #     return

    ps = PoseStamped()
    ps.header.frame_id = "/map"
    ps.header.stamp = rospy.Time.now()
    ps.pose.position.x = 1
    ps.pose.position.y = 0
    ps.pose.position.z = 0

    q = quaternion_from_euler(0, 0, 0, 'sxyz')
    ps.pose.orientation.x = q[0]
    ps.pose.orientation.y = q[1]
    ps.pose.orientation.z = q[2]
    ps.pose.orientation.w = q[3]

    mbag = MoveBaseActionGoal()
    mbag.header = ps.header
    mbag.goal.target_pose = ps




    print mbag
    PUB_GOAL.publish(mbag)
    
     
def wildcat():
    rospy.init_node('WildCat_Teleport', anonymous=True)
    #client = actionlib.SimpleActionClient('WildCat_Teleport', sendToOnce)
    #client.wait_for_server()

    global PUB_GOAL
    #PUB_GOAL = rospy.Publisher('/move_base_simple/goal', PoseStamped)
    PUB_GOAL = rospy.Publisher('/move_base/goal', MoveBaseActionGoal)

    rospy.Subscriber('/odom', Odometry, callback)
    #for i in range(100):
    #    sendToOnce()
        # pass
    
    rospy.spin()

def getDistance(point):
    return math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)

        
if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass
 
