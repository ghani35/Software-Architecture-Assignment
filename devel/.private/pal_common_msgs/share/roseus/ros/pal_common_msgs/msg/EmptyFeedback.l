;; Auto-generated. Do not edit!


(when (boundp 'pal_common_msgs::EmptyFeedback)
  (if (not (find-package "PAL_COMMON_MSGS"))
    (make-package "PAL_COMMON_MSGS"))
  (shadow 'EmptyFeedback (find-package "PAL_COMMON_MSGS")))
(unless (find-package "PAL_COMMON_MSGS::EMPTYFEEDBACK")
  (make-package "PAL_COMMON_MSGS::EMPTYFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude EmptyFeedback.msg.html


(defclass pal_common_msgs::EmptyFeedback
  :super ros::object
  :slots ())

(defmethod pal_common_msgs::EmptyFeedback
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get pal_common_msgs::EmptyFeedback :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get pal_common_msgs::EmptyFeedback :datatype-) "pal_common_msgs/EmptyFeedback")
(setf (get pal_common_msgs::EmptyFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======


")



(provide :pal_common_msgs/EmptyFeedback "d41d8cd98f00b204e9800998ecf8427e")

