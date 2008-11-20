#
# Conditional build:
#
%define		qt_ver		4.4.3
%define		snap		886570

Summary:	Tapioca Qt
Summary(pl.UTF-8):	Tapioca Qt
Name:		tapioca-qt
Version:	0.17.7
Release:	0.%{snap}.2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	1cd9913f09e804fb654eec6a6385274f
URL:		http://decibel.kde.org/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	telepathy-qt-devel >= 0.17.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

#%description -l pl.UTF-8

%package devel
Summary:        Header files for tapioca-qt library
Summary(pl.UTF-8):      Pliki nag�~B처wkowe biblioteki tapioca-qt
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for tapioca-qt library.

%description devel -l pl.UTF-8
Pliki nag�~B처wkowe biblioteki tapioca-qt.

%prep
%setup -q -n %{name}-%{version}-%{snap}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtTapioca.so.0.17.7
%attr(755,root,root) %ghost %{_libdir}/libQtTapioca.so.1707

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtTapioca.so
%{_includedir}/QtTapioca
%{_pkgconfigdir}/QtTapioca.pc
