%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		libkcompactdisc
Summary:	KCompactdisc
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f672769ee39e420b94c0171681127393
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.24.0
BuildRequires:	kf5-ki18n-devel >= 5.24.0
BuildRequires:	kf5-solid-devel >= 5.24.0
BuildRequires:	phonon-qt5-devel >= 4.8.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDE Compact Disc library provides an API for applications using
the KDE Platform to interface with the CD drives for audio CDs.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libKF5CompactDisc.so.5
%attr(755,root,root) %{_libdir}/libKF5CompactDisc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KCompactDisc
%{_includedir}/KF5/kcompactdisc_version.h
%{_libdir}/cmake/KF5CompactDisc
%attr(755,root,root) %{_libdir}/libKF5CompactDisc.so
%{_libdir}/qt5/mkspecs/modules/qt_KCompactDisc.pri
