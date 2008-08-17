Name:           gcube
Version:        0.4
Release:        3%{?dist}
Summary:        Nintendo Gamecube emulator
Group:          Applications/Emulators
License:        GPLv2
URL:            http://gcube.exemu.net
Source0:        http://gcube.exemu.net/downloads/%{name}-%{version}-src.tar.bz2
Patch0:         gcube-0.4-nostrip.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  SDL-devel >= 1.2.7
BuildRequires:  zlib-devel


%description
A Nintendo Gamecube emulator which uses SDL


%prep
%setup -qn %{version}
%patch0 -p1


%build
make release %{?_smp_mflags} CPU="" ENABLE_SOUND=1 OPTFLAGS="%{optflags} -fno-strict-aliasing" \
%ifarch ppc x86_64
ASM_X86=0
%else
ASM_X86=1
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
* Wed Dec 12 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-3
- Minor spec changes for devel
- License change due to new guidelines

* Wed Oct 25 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-2
- Dropped nasm buildrequire. Not actually used
- Added patch to not strip binaries for debuginfo packages

* Mon Oct 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-1
- Initial Release