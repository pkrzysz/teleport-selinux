# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/local/bin/teleport; \
restorecon -R /var/run/teleport.pid; \
[ -d /var/run/teleport ] && restorecon -R /var/run/teleport; \
restorecon -R /var/lib/teleport; \

%define selinux_policyver 3.13.1-192

Name:   teleport_selinux
Version:	1.8
Release:	2
Summary:	SELinux policy module for teleport with cil port support for rhel 7.4+

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		https://teleport.isbank.is
Source0:	teleport.cil
Source1:	teleport_selinux.8


Requires: policycoreutils, libselinux-utils
Requires(post): policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for teleport.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man8/teleport_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -i %{_datadir}/selinux/packages/teleport.cil

if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r teleport
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/teleport.cil
%{_mandir}/man8/teleport_selinux.8.*


%changelog
