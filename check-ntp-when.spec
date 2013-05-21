%define name check-ntp-when
%define version 0.1
%define unmangled_version 0.1
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

%description
check_ntp_when queries a remote NTP client and checks the recentness 
(or freshness) of its NTP polling. In certain cases, NTP clients can
"forget" to poll, and drift out of sync.

%prep
%setup -q


%build
pandoc -s -w man README.md -o %{name}.1

%install
mkdir -p %{_bindir} && cp %{SOURCE0} %{_bindir}
mkdir -p %{_mandir}/man1 && cp %{name}.1 %{_mandir}/man1

%files
%attr(0644,root,root) %doc %{_mandir}/man1/%{name}.1
%attr(0755,root,root) %{_bindir}/${name}

%changelog
* Tue May 21 2013 Colin Panisset <nonspecialist@clabber.com> 0.1-1
- Initial version with manpage
