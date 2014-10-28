#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import PointCloud2, PointField
from visualization_msgs.msg import Marker
from gotoClient import goto
PUB_MOTION = None

def callback(response):
        print'********'
        pointPosition = response.pose.position


            
        # Create minimum distance point object for visualization purposes
        # pointPosition = Point()
        # pointPosition.x = minPoint[0]
        # pointPosition.y = minPoint[1]
        # pointPosition.z = minPoint[2]
        # result = PointStamped()
        # result.point = pointPosition
        # header = Header()
        # header.frame_id = 'camera_depth_optical_frame'
        # result.header = header 
        # PUB_MIN_POINT.publish(result)



        # Move towards nearest point
        twist = Twist()
        if pointPosition.x > 0.1:
            twist.angular.z = -0.5
            print 1
        elif pointPosition.x < -0.1:
            twist.angular.z = 0.5
            print 2
        elif pointPosition.z > 0.2:
            twist.linear.x = 0.2 # or make negative to run away from things
            print 3
        PUB_MOTION.publish(twist)

def wildcat():
    rospy.init_node('goToMarker', anonymous=True)
    rospy.Subscriber('/visualization_marker', Marker, callback)
    global PUB_MOTION
    PUB_MOTION = rospy.Publisher('mobile_base/commands/velocity', Twist)
    rospy.spin()

if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass
