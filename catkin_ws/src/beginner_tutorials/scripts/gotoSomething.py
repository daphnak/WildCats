#!/usr/bin/env python
import rospy
import threading
import math
from time import time
from geometry_msgs.msg import Twist
from visualization_msgs.msg import Marker


PUB_MOTION = None
PREV_TIME = 0

# angular displacement direction needed
# forward?

def setInterval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()

def markerHandler(response):
        global PREV_TIME
        print'********'
        now = time()
        diff = now - PREV_TIME
        print 'time since last callback' , diff
        PREV_TIME = now


        pointPosition = response.pose.position

        twist = Twist()
        if pointPosition.x > 0.05:
            twist.angular.z = -0.7
            print 1
        elif pointPosition.x < -0.05:
            twist.angular.z = 0.7
            print 2
        # elif pointPosition.z > 0.4:
        if getDistance(pointPosition) > 0.4:
            twist.linear.x = 0.2 # or make negative to run away from things
            print 3
        PUB_MOTION.publish(twist)


def getDistance(position):
    return math.sqrt(position.y**2 + position.z**2)

def wildcat():
    rospy.init_node('goToMarker', anonymous=True)
    rospy.Subscriber('/wildcat_visualization_marker', Marker, markerHandler)
    global PUB_MOTION
    PUB_MOTION = rospy.Publisher('mobile_base/commands/velocity', Twist)
    rospy.spin()

if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass
