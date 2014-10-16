#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

PUB_MOTION = None
STATE =0
def callback(data):

    print'********'
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z
    print z

    # angle constants
    DEFAULT_ANGLE_THRESH = 0.01
    ESCAPE_ANGLE_THRESH = 0.1

    #
    DEFAULT_LINEAR_THRESH = 0.02
    ESCAPE_LINEAR_THRESH = 0.1

    ANGLE_THRESH = DEFAULT_ANGLE_THRESH
    LINEAR_THRESH = DEFAULT_LINEAR_THRESH
    global STATE
    if STATE == 1:
        ANGLE_THRESH = ESCAPE_ANGLE_THRESH
        LINEAR_THRESH = ESCAPE_LINEAR_THRESH
    # check if we are near y axis. If not,
        # check if we are within 0.02 arbitrary units of facing z = 0,
    # if so, head forward some good amount (0.5)
    # otherwise turn clockwise 0.1d
    twist = Twist()
    print "x: " , x 
    print "y: " , y
    print "z: " , z
    if x < 0.2 and y < 0.2 :
        return
    if abs(x) < LINEAR_THRESH:
        if abs(0.7 - abs(z)) < ANGLE_THRESH:
            STATE = 1

            twist.linear.x = -0.5 * y
            
            print("1")
        else:
            twist.angular.z = max(0.5 * abs(0.7 -abs(z)) , 0.001)
            print 2
    else:
        if abs(z) < ANGLE_THRESH:
            STATE=0

            twist.linear.x = -0.5 * x
            print 3
        else:
            twist.angular.z = max(0.5 * (abs(z)) , 0.001)
            print 4

    
    PUB_MOTION.publish(twist)
     
def wildcat():
    rospy.init_node('wildcat_goes_home', anonymous=True)
    rospy.Subscriber('/odom', Odometry, callback)

    global PUB_MOTION
    PUB_MOTION = rospy.Publisher('mobile_base/commands/velocity', Twist)
    rospy.spin()

def getDistance(point):
    return math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)

        
if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass
 