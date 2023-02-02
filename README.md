# Teleport selinux policy

Compatibile with RHEL 7.4+,8,9/RockyLinux8/RockyLinux9

Should work for multiplex proxy/node services, as well as auth services with etcd/minio

If other services are not working, probably port definiotions are missing from selinux policy.
In that case either use semanage to add port, or add port to rpm by editing cil file.
