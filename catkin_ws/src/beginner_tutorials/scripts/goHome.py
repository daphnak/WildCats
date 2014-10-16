#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

PUB_MOTION = None
STATE =0
def callback(data):
    DISTANCE_THRESHOLD = .1
    print'********'
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    
    if math.sqrt(x**2+y**2) < DISTANCE_THRESHOLD:
        return

    twist = Twist()
    print "x: " , x 
    print "y: " , y
    quat = data.pose.pose.orientation
    quat_array = (quat.x, quat.y, quat.z, quat.w)
    angles = euler_from_quaternion(quat_array)
    yaw = angles[2] 
    print yaw

    yawTarget = math.atan2(y,x) + math.pi
    print yawTarget
    
    if abs(yaw - yawTarget) < 0.5:
        twist.linear.x = 0.2
	print 1
    else:
	twist.angular.z = -.4 if yaw > yawTarget else .4 
	print 2
    
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
 
