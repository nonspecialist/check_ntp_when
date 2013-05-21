%define name check-ntp-when
%define version 0.2
%define unmangled_version 0.2
%define release 1

Name:		%{name}
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	Checks the poll recentness of a remote NTP client

Group:		Applications/System
License:	GPL
URL:		http://github.com/nonspecialist/check_ntp_when
Source0:	check_ntp_when
Source1:	README.md

BuildRequires:	pandoc
Requires:	ntp, nagios-common
BuildArch:	noarch

%description
check_ntp_when queries a remote NTP client and checks the recentness 
(or freshness) of its NTP polling. In certain cases, NTP clients can
"forget" to poll, and drift out of sync.

%prep
/bin/true

%build
pandoc -s -w man %{SOURCE1} -o check_ntp_when.1

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/nagios/plugins \
	 ${RPM_BUILD_ROOT}/%{_mandir}/man1 
cp check_ntp_when.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1
cp %{SOURCE0} ${RPM_BUILD_ROOT}/usr/lib/nagios/plugins

%files
%attr(0644,root,root) %doc %{_mandir}/man1/check_ntp_when.1.gz
%attr(0755,root,root) /usr/lib/nagios/plugins/check_ntp_when

%changelog
* Tue May 21 2013 Colin Panisset <nonspecialist@clabber.com> 0.2-1
- Change destination path to be a nagios plugin
- Update dependencies to reflect nagios plugin status
* Tue May 21 2013 Colin Panisset <nonspecialist@clabber.com> 0.1-1
- Initial version with manpage
