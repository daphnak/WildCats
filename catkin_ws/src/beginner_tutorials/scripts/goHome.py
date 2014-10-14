#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped

PUB_MIN_POINT = None
PUB_MOTION = None
# header: 
#   seq: 66855
#   stamp: 
#     secs: 5578
#     nsecs: 970000000
#   frame_id: camera_depth_optical_frame


def callback(response):
        print'********'
        gen = point_cloud2.read_points(response,skip_nans=True)

        try:
            firstPoint = gen.next()
            minDist = getDistance(firstPoint)
            minPoint = firstPoint
            for point in gen:
                distance = getDistance(point)
                if distance < minDist:
                    if (point[1] < 0.1):
                        minDist = distance
                        minPoint = point
            print minDist
            print minPoint
            
            # Create minimum distance point object for visualization purposes
            pointMin = Point()
            pointMin.x = minPoint[0]
            pointMin.y = minPoint[1]
            pointMin.z = minPoint[2]
            result = PointStamped()
            result.point = pointMin
            header = Header()
            header.frame_id = 'camera_depth_optical_frame'
            result.header = header 
            PUB_MIN_POINT.publish(result)

            # Move towards nearest point
            twist = Twist()
            if pointMin.x > 0.2:
                twist.angular.z = -0.7
            elif pointMin.x < -0.2:
                twist.angular.z = 0.7
            elif pointMin.z > 0.2:
                twist.linear.x = 0.2 # or make negative to run away from things

            PUB_MOTION.publish(twist)
        except StopIteration:
            pass

def wildcat():
    rospy.init_node('wildcat', anonymous=True)
    rospy.Subscriber('/camera/depth_registered/points', PointCloud2, callback)
    rospy.Subscriber('/odom', Odometry, show_text_in_rviz)

    global PUB_MIN_POINT
    PUB_MIN_POINT = rospy.Publisher('minPoints', PointStamped)
    global PUB_MOTION
    PUB_MOTION = rospy.Publisher('mobile_base/commands/velocity', Twist)
    rospy.spin()

def getDistance(point):
    return math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)

        
if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass
