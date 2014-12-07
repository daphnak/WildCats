#! /usr/bin/env python
from gotoClient import goto
from goToNamedLocation import goToNamedLocation
from std_msgs.msg import String
from geometry_msgs.msg import *
from threading import Timer
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
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
        say("Nice")
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
    if STATE == "WAITING_FOR_POSE" or STATE == "NAVIGATING_TO_HOME":
        STATE = "NAVIGATING_TO_GOAL"
        # print 'nice: ', message
        print "Navigating to goal"
        say("navigating to goal")
        goto(message.x, message.y, frame="/openni_depth_frame", callback=goNavCompleteCallback)

def voiceCallback(message):
    global STATE
    # print "yo msg was '%s'" % message.data
    print "current state is " , STATE
    if "akio-wild-cat" in message.data or "okay-wild-cat" in message.data:
        if STATE == "LISTENING":
            STATE = "WAITING_FOR_POSE"
            print "Waiting for pose"
            say("Waiting for pose")
            t = Timer(20, timeout)
            t.start()
    elif "good-job-wild-cat" in message.data and (STATE == "WAITING_FOR_TRASH" or STATE == "NAVIGATING_TO_GOAL"):
        STATE = "NAVIGATING_TO_HOME"
        print 'imma goin\' home'
        say("going home")
        goto(0.9, 0.2, frame="/map", callback=goHomeCompleteCallback) 

def timeout():
    global STATE
    
    if STATE == "WAITING_FOR_POSE":
        STATE = "LISTENING"
        print "time out aw"

def say(s):
    soundhandle = SoundClient()
    voice = 'voice_kal_diphone'
    print 'Saying: %s' % s
    print 'Voice: %s' % voice
    soundhandle.say(s,voice)



if __name__=="__main__":
    try:
        rospy.init_node("command_interpreter")
        rospy.Subscriber('/wildcat_detected_poses', Point, poseCallback)
        rospy.Subscriber('/recognizer/output', String, voiceCallback)
        rospy.spin()
    except rospy.ROSInterruptException: pass
