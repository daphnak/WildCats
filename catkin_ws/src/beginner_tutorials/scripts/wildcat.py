#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2

PUB_MIN_POINT = None
PUB_MOTION = None
# header: 
#   seq: 66855
#   stamp: 
#     secs: 5578
#     nsecs: 970000000
#   frame_id: camera_depth_optical_frame


def callback(response):
        gen = point_cloud2.read_points(response,skip_nans=True)
        print'********'
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
            if pointMin.x > 0.15:
                twist.angular.z = -0.25
            elif pointMin.x < -0.15:
                twist.angular.z = 0.25
            elif pointMin.z > 0.1:
                twist.linear.x = 1 # or make negative to run away from things

            PUB_MOTION.publish(twist)
        except StopIteration:
            pass





def wildcat():
    rospy.init_node('wildcat', anonymous=True)
    rospy.Subscriber('/camera/depth/points', PointCloud2, callback)
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





# ef read_points(cloud, field_names=None, skip_nans=False, uvs=[]):
# 28      """
# 29      Read points from a L{sensor_msgs.PointCloud2} message.
# 30  
# 31      @param cloud: The point cloud to read from.
# 32      @type  cloud: L{sensor_msgs.PointCloud2}
# 33      @param field_names: The names of fields to read. If None, read all fields. [default: None]
# 34      @type  field_names: iterable
# 35      @param skip_nans: If True, then don't return any point with a NaN value.
# 36      @type  skip_nans: bool [default: False]
# 37      @param uvs: If specified, then only return the points at the given coordinates. [default: empty list]
# 38      @type  uvs: iterable
# 39      @return: Generator which yields a list of values for each point.
# 40      @rtype:  generator
# 41  



# try:
#         for i in range(n):
#             result.append(seq.next())
#     except StopIteration:
#         pass