; Auto-generated. Do not edit!


(cl:in-package koki-msg)


;//! \htmlinclude KokiMsg.msg.html

(cl:defclass <KokiMsg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (tags
    :reader tags
    :initarg :tags
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass KokiMsg (<KokiMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <KokiMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'KokiMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name koki-msg:<KokiMsg> is deprecated: use koki-msg:KokiMsg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <KokiMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader koki-msg:header-val is deprecated.  Use koki-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'tags-val :lambda-list '(m))
(cl:defmethod tags-val ((m <KokiMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader koki-msg:tags-val is deprecated.  Use koki-msg:tags instead.")
  (tags m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <KokiMsg>) ostream)
  "Serializes a message object of type '<KokiMsg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'tags))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream))
   (cl:slot-value msg 'tags))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <KokiMsg>) istream)
  "Deserializes a message object of type '<KokiMsg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'tags) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'tags)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<KokiMsg>)))
  "Returns string type for a message object of type '<KokiMsg>"
  "koki/KokiMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KokiMsg)))
  "Returns string type for a message object of type 'KokiMsg"
  "koki/KokiMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<KokiMsg>)))
  "Returns md5sum for a message object of type '<KokiMsg>"
  "fe7110c393ddc1d808f67f0d26385fab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'KokiMsg)))
  "Returns md5sum for a message object of type 'KokiMsg"
  "fe7110c393ddc1d808f67f0d26385fab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<KokiMsg>)))
  "Returns full string definition for message of type '<KokiMsg>"
  (cl:format cl:nil "Header header~%uint16[] tags~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'KokiMsg)))
  "Returns full string definition for message of type 'KokiMsg"
  (cl:format cl:nil "Header header~%uint16[] tags~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <KokiMsg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'tags) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <KokiMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'KokiMsg
    (cl:cons ':header (header msg))
    (cl:cons ':tags (tags msg))
))
