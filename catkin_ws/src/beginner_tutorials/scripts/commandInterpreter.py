#! /usr/bin/env python
from gotoClient import goto
from goToNamedLocation import goToNamedLocation
from std_msgs.msg import String
from geometry_msgs.msg import *
from threading import Timer
import sys
import rospy

PUB_POSE = None

# LISTENING, WAITING_FOR_POSE, NAVIGATING_TO_GOAL, WAITING_FOR_TRASH, NAVIGATING_TO_HOME, FUBAR
STATE = "LISTENING"


# ***** Navigation complete callbacks *****

def goHomeCompleteCallback(terminal_state, result):
    print "terminal state is: ", terminal_state, " and result is: ", result, "*"
    global STATE
    if STATE == "NAVIGATING_TO_HOME":
        STATE = "LISTENING"
    else:
        print "Error: recieved goHomeCompleteCallback while state was ", STATE


def goNavCompleteCallback(terminal_state, result):
    print "terminal state is: ", terminal_state, " and result is: ", result, "*"
    global STATE
    if STATE == "NAVIGATING_TO_GOAL":
        STATE = "WAITING_FOR_TRASH"
    else:
        print "Error: recieved goNavCompleteCallback while state was ", STATE

# ***** Command callbacks *****

def poseCallback(message):
    global STATE
    # print 'poseCallback'
    if STATE == "WAITING_FOR_POSE":
        STATE = "NAVIGATING_TO_GOAL"
        # print 'nice: ', message
        print "Navigating to goal"
        goto(message.x, message.y, frame="/openni_depth_frame", callback=goNavCompleteCallback)

def voiceCallback(message):
    global STATE
    # print "yo msg was '%s'" % message.data
    print "current state is " , STATE
    if message.data == "okay-wild-cat":
        if STATE == "LISTENING":
            STATE = "WAITING_FOR_POSE"
            print "Waiting for pose"
            t = Timer(20, timeout)
            t.start()
    elif message.data == "thank-you-wild-cat" and (STATE == "WAITING_FOR_TRASH" or STATE == "NAVIGATING_TO_GOAL"):
        STATE = "NAVIGATING_TO_HOME"
        print 'imma goin\' home'
        goto(1.3, 0, frame="/map", callback=goHomeCompleteCallback) 

def timeout():
    global STATE
    
    if STATE == "WAITING_FOR_POSE":
        STATE = "LISTENING"
        print "time out aw"


if __name__=="__main__":
    try:
        rospy.init_node("command_interpreter")
        rospy.Subscriber('/wildcat_detected_poses', Point, poseCallback)
        rospy.Subscriber('/recognizer/output', String, voiceCallback)
        rospy.spin()
    except rospy.ROSInterruptException: pass
