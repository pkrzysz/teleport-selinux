# Teleport selinux policy

Compatibile with RHEL 7.4+,8,9/RockyLinux8/RockyLinux9

Should work for multiplex proxy/node services, as well as auth services with etcd/minio

If other services are not working, probably port definiotions are missing from selinux policy.
In that case either use semanage to add port, or add port to rpm by editing cil file.


As SELinux is all about file path, make sure that all references to certificates are on:
/var/lib/teleport

For multiple config files, use *.pid file in dedicated directory - /var/run/teleport


on proxy/auth servers nis needs to be enabled:

setsebool -P nis_enabled 1
