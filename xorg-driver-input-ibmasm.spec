Summary:	IBM Advanced System Management X input driver
Name:		xorg-driver-input-ibmasm
Version:	2.1
Release:	1
License:	MIT
Group:		X11/Applications
URL:		http://sourceforge.net/projects/ibmasm/
Source0:	http://downloads.sourceforge.net/ibmasm/ibmasm-xinput-%{version}.tar.bz2
# Source0-md5:	2480c6c6498da6cc17f285e060a141e2
BuildRequires:	libtool
BuildRequires:	pixman-devel
BuildRequires:	xorg-xserver-server-devel
Requires:	ibmasm >= 3.0-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the X11 input driver to allow the IBM Advanced
System Management (RSA 1 Service Processor) adapter to control the X
mouse and keyboard events.

%prep
%setup -q -n ibmasm-xinput-%{version}

sed -i -e 's#xf86Version.h#xorgVersion.h#' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} $(pkg-config pixman-1 --cflags)"
%configure \
	--with-xorg-sdk-dir=%{_includedir}/xorg \
	--with-xorg-module-dir=%{_libdir}/xorg/modules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/ibmasm_drv.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README INSTALL
%attr(755,root,root) %{_libdir}/xorg/modules/input/ibmasm_drv.so
