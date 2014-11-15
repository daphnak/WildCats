#! /usr/bin/env python
from gotoClient import goto
from goToNamedLocation import goToNamedLocation
from  std_msgs.msg import String
from threading import Timer
import sys
import rospy

PUB_POSE = None

LISTENING_STATE = "MINIMAL"

def poseCallback(message):
    pass

def voiceCallback(message):
    global LISTENING_STATE
    print "yo msg was '%s'" % message.data
    print "current state is " , LISTENING_STATE 
    if message.data == "okay-wild-cat":
        print "okay-wildcat"
        if LISTENING_STATE == "MINIMAL":
            print "i was minimal"
            LISTENING_STATE = "WAITING"
            t = Timer(5, timeout)
            t.start()
    else:
        pass
        # add more parsing as needed

def timeout():
    global LISTENING_STATE
    
    if LISTENING_STATE == "WAITING":
        LISTENING_STATE = "MINIMAL"
        print "time out aw"


if __name__=="__main__":
    try:
        rospy.init_node("command_interpreter")
        rospy.Subscriber('/wildcat_detected_poses', String, poseCallback)
        rospy.Subscriber('/recognizer/output', String, voiceCallback)
        rospy.spin()
    except rospy.ROSInterruptException: pass
