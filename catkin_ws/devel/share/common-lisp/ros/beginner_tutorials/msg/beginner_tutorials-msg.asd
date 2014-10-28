
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "GotoFeedback" :depends-on ("_package_GotoFeedback"))
    (:file "_package_GotoFeedback" :depends-on ("_package"))
    (:file "GotoResult" :depends-on ("_package_GotoResult"))
    (:file "_package_GotoResult" :depends-on ("_package"))
    (:file "GotoAction" :depends-on ("_package_GotoAction"))
    (:file "_package_GotoAction" :depends-on ("_package"))
    (:file "GotoActionResult" :depends-on ("_package_GotoActionResult"))
    (:file "_package_GotoActionResult" :depends-on ("_package"))
    (:file "GotoGoal" :depends-on ("_package_GotoGoal"))
    (:file "_package_GotoGoal" :depends-on ("_package"))
    (:file "GotoActionGoal" :depends-on ("_package_GotoActionGoal"))
    (:file "_package_GotoActionGoal" :depends-on ("_package"))
    (:file "GotoActionFeedback" :depends-on ("_package_GotoActionFeedback"))
    (:file "_package_GotoActionFeedback" :depends-on ("_package"))
  ))