; Auto-generated. Do not edit!


(cl:in-package pal_common_msgs-msg)


;//! \htmlinclude DisableActionGoal.msg.html

(cl:defclass <DisableActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type pal_common_msgs-msg:DisableGoal
    :initform (cl:make-instance 'pal_common_msgs-msg:DisableGoal)))
)

(cl:defclass DisableActionGoal (<DisableActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DisableActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DisableActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pal_common_msgs-msg:<DisableActionGoal> is deprecated: use pal_common_msgs-msg:DisableActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DisableActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_common_msgs-msg:header-val is deprecated.  Use pal_common_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <DisableActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_common_msgs-msg:goal_id-val is deprecated.  Use pal_common_msgs-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <DisableActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_common_msgs-msg:goal-val is deprecated.  Use pal_common_msgs-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DisableActionGoal>) ostream)
  "Serializes a message object of type '<DisableActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DisableActionGoal>) istream)
  "Deserializes a message object of type '<DisableActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DisableActionGoal>)))
  "Returns string type for a message object of type '<DisableActionGoal>"
  "pal_common_msgs/DisableActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DisableActionGoal)))
  "Returns string type for a message object of type 'DisableActionGoal"
  "pal_common_msgs/DisableActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DisableActionGoal>)))
  "Returns md5sum for a message object of type '<DisableActionGoal>"
  "a7386e7a41cdfb8807af810188ae810d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DisableActionGoal)))
  "Returns md5sum for a message object of type 'DisableActionGoal"
  "a7386e7a41cdfb8807af810188ae810d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DisableActionGoal>)))
  "Returns full string definition for message of type '<DisableActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%DisableGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: pal_common_msgs/DisableGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# This action disables a functionality for a set amount of seconds.~%# A negative or zero value will disable it until the goal is canceled~%~%float32 duration # [s] for how long to disable the functionality~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DisableActionGoal)))
  "Returns full string definition for message of type 'DisableActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%DisableGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: pal_common_msgs/DisableGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# This action disables a functionality for a set amount of seconds.~%# A negative or zero value will disable it until the goal is canceled~%~%float32 duration # [s] for how long to disable the functionality~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DisableActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DisableActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'DisableActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))
