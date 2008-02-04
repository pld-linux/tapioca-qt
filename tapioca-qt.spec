Summary:	tapioca-qt
Summary(pl.UTF-8):   tapioca-qt
Name:		tapioca-qt
Version:	0.14.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://mesh.dl.sourceforge.net/sourceforge/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	169318705af6386057b537c5317d520d
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tapioca-qt

%description -l pl.UTF-8
tapioca-qt

%package devel
Summary:	Header files for tapioca-qt libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek tapioca-qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tapioca-qt libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek tapioca-qt

%prep
%setup -q

%build
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtTapioca.so.?
%attr(755,root,root) %{_libdir}/libQtTapioca.so.*.*.*
%attr(755,root,root) %{_libdir}/pkgconfig/QtTapioca.pc
            
%files devel
%defattr(644,root,root,755)
%{_includedir}/QtTapioca
%attr(755,root,root) %{_libdir}/libQtTapioca.so
