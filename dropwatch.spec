Summary: Kernel dropped packet monitor 
Name: dropwatch 
Version: 1.4
Release: 8%{?dist} 
Source0: https://fedorahosted.org/releases/d/r/dropwatch/dropwatch-%{version}.tbz2
URL: http://fedorahosted.org/dropwatch
License: GPLv2+ 
Group: Applications/System 
Patch0: dropwatch-1.4-typecast.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: kernel-devel, libnl-devel, readline-devel
BuildRequires: binutils-devel, binutils-static libnl3-devel pkgconfig
Requires: libnl3, readline

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%setup -q 
%patch0 -p1 -b .typecast

%build
cd src
export CFLAGS=$RPM_OPT_FLAGS
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0755 src/dropwatch $RPM_BUILD_ROOT%{_bindir}
install -m0644 doc/dropwatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc README
%doc COPYING

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.4-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-7
- Mass rebuild 2013-12-27

* Sun May 12 2013 Anton Arapov <anton@redhat.com> - 1.4-6
- Fix the build for ppc platform. Typecast issue (#960092)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Dan Horák <dan@danny.cz> - 1.4-4
- rebuilt again for fixed soname in libnl3

* Fri Jan 18 2013 Neil Horman <nhorman@redhat.com> - 1.4-3
- rebuilt to pull in new libnl3 dependencies

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Neil Horman <nhorman@redhat.com> - 1.4-1
- Update to latest upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Neil Horman <nhorman@redhat.com> - 1.2
- Update to latest upstream

* Thu Apr 07 2010 Neil Horman <nhorman@redhat.com> - 1.1-2
- Adding more missing buildrequires

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 1.1-1
- Add missing buildrequires

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 1.1-0
- Move to latest upstream sources

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Neil Horman <nhorman@redhat.com> 1.0-2
- Fixed up Errors found in package review (bz 491240)

* Tue Mar 17 2009 Neil Horman <nhorman@redhat.com> 1.0-1
- Initial build

