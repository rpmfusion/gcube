Name:          gcube
Version:       0.4
Release:       6%{?dist}
Summary:       Nintendo Gamecube emulator

Group:         Applications/Emulators
License:       GPLv2+
URL:           http://gcube.exemu.net
# source is no longer present at original source0.
# further devel under other project names. md5sum matches dribble original.
# Source0:       http://gcube.exemu.net/downloads/%{name}-%{version}-src.tar.bz2
Source0:       http://ftp.netbsd.org/pub/NetBSD/packages/distfiles/%{name}-%{version}-src.tar.bz2
Patch0:        gcube-0.4-nostrip.patch
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: SDL-devel >= 1.2.7
BuildRequires: zlib-devel


%description
A Nintendo Gamecube emulator which uses SDL


%prep
%setup -qn %{version}
%patch0 -p1


%build
make release %{?_smp_mflags} CPU="" ENABLE_SOUND=1 OPTFLAGS="%{optflags} -fno-strict-aliasing" \
%ifarch %{ix86}
ASM_X86=1
%else
ASM_X86=0
%endif


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 bin2dol %{buildroot}%{_bindir}
install -m0755 gcmap %{buildroot}%{_bindir}
install -m0755 gcube %{buildroot}%{_bindir}
install -m0755 isopack %{buildroot}%{_bindir}
install -m0755 thpview %{buildroot}%{_bindir}
install -m0755 tplx %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc COPYING README README.debug


%changelog
* Sun Sep 28 2008 David Timms <iinet.net.au@dtimms> 0.4-6
- mod asm compile logic to retry build on ppc64 builder {adrian, rathann}
- remove excludearch ppc64

* Mon Sep 22 2008 David Timms <iinet.net.au@dtimms> 0.4-5
- add ExcludeArch: ppc64 since lack of asm bswap stops build

* Sun Sep 21 2008 David Timms <iinet.net.au@dtimms> 0.4-4
- initial import into rpmfusion and release bump
- set license tag to match updated fedora guideline

* Wed Dec 12 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-3
- Minor spec changes for devel
- License change due to new guidelines

* Wed Oct 25 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-2
- Dropped nasm buildrequire. Not actually used
- Added patch to not strip binaries for debuginfo packages

* Mon Oct 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-1
- Initial Release
