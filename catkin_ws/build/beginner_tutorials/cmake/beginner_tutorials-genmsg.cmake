# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "beginner_tutorials: 8 messages, 1 services")

set(MSG_I_FLAGS "-Ibeginner_tutorials:/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/msg;-Ibeginner_tutorials:/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg;-Istd_msgs:/opt/ros/hydro/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/hydro/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/hydro/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(beginner_tutorials_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)

### Generating Services
_generate_srv_cpp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
)

### Generating Module File
_generate_module_cpp(beginner_tutorials
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(beginner_tutorials_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(beginner_tutorials_generate_messages beginner_tutorials_generate_messages_cpp)

# target for backward compatibility
add_custom_target(beginner_tutorials_gencpp)
add_dependencies(beginner_tutorials_gencpp beginner_tutorials_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS beginner_tutorials_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)

### Generating Services
_generate_srv_lisp(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
)

### Generating Module File
_generate_module_lisp(beginner_tutorials
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(beginner_tutorials_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(beginner_tutorials_generate_messages beginner_tutorials_generate_messages_lisp)

# target for backward compatibility
add_custom_target(beginner_tutorials_genlisp)
add_dependencies(beginner_tutorials_genlisp beginner_tutorials_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS beginner_tutorials_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionFeedback.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoGoal.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/devel/share/beginner_tutorials/msg/GotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)
_generate_msg_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)

### Generating Services
_generate_srv_py(beginner_tutorials
  "/home/motionlab/WildCats/catkin_ws/src/beginner_tutorials/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
)

### Generating Module File
_generate_module_py(beginner_tutorials
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(beginner_tutorials_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(beginner_tutorials_generate_messages beginner_tutorials_generate_messages_py)

# target for backward compatibility
add_custom_target(beginner_tutorials_genpy)
add_dependencies(beginner_tutorials_genpy beginner_tutorials_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS beginner_tutorials_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/beginner_tutorials
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(beginner_tutorials_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(beginner_tutorials_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
add_dependencies(beginner_tutorials_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/beginner_tutorials
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(beginner_tutorials_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(beginner_tutorials_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
add_dependencies(beginner_tutorials_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/beginner_tutorials
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(beginner_tutorials_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(beginner_tutorials_generate_messages_py actionlib_msgs_generate_messages_py)
add_dependencies(beginner_tutorials_generate_messages_py geometry_msgs_generate_messages_py)
