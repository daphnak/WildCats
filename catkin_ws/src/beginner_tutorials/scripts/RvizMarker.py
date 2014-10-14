#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA
from nav_msgs.msg import Odometry

points = []


def wildcat():
    rospy.init_node('marker_maker')
    global PUB
    PUB = rospy.Publisher('visualization_marker', Marker)
    rospy.Subscriber('/odom', Odometry, show_text_in_rviz)
    rospy.spin()




def show_text_in_rviz(data):
    x = data.pose.pose.position.x
    y= data.pose.pose.position.y
    global points
    points.append(Point(x,y,0))
    marker = Marker(type=Marker.LINE_STRIP, id=0,
                lifetime=rospy.Duration(10),
                pose=Pose(Point(0,0,0), Quaternion(0, 0, 0, 1)),
                points=points,
                scale=Vector3(0.06, 0.06, 0.06),
                header=Header(frame_id='odom'),
                color=ColorRGBA(0.0, 1.0, 0.0, 0.8))
    global PUB
    PUB.publish(marker)



if __name__ == '__main__':
    try:
        wildcat()
    except rospy.ROSInterruptException: pass