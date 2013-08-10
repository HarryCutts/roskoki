
(cl:in-package :asdf)

(defsystem "koki-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "KokiMsg" :depends-on ("_package_KokiMsg"))
    (:file "_package_KokiMsg" :depends-on ("_package"))
  ))