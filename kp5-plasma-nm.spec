#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.10
%define		qtver		5.15.2
%define		kpname		plasma-nm
%define		kf5ver		5.39.0

Summary:	plasma-nm
Name:		kp5-%{kpname}
Version:	5.27.10
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	0e11c62c2a23d161b5b8cbe6e87517bc
URL:		http://www.kde.org/
BuildRequires:	ModemManager-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-modemmanager-qt-devel
BuildRequires:	kf5-networkmanager-qt-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	ninja
BuildRequires:	openconnect-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	qca-qt5-devel >= 2.1.1
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Plasma applet written in QML for managing network connections.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplasmanm_editor.so
%attr(755,root,root) %{_libdir}/libplasmanm_internal.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/networkmanagement.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/networkmanagement
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
%{_libdir}/qt5/qml/org/kde/plasma/networkmanagement/qmldir
%{_datadir}/knotifications5/networkmanagement.notifyrc
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%dir %{_datadir}/kcm_networkmanagement
%dir %{_datadir}/kcm_networkmanagement/qml
%{_datadir}/kcm_networkmanagement/qml/ConnectionItem.qml
%{_datadir}/kcm_networkmanagement/qml/ListItem.qml
%{_datadir}/kcm_networkmanagement/qml/main.qml
%{_datadir}/metainfo/org.kde.plasma.networkmanagement.appdata.xml
%{_datadir}/kcm_networkmanagement/qml/AddConnectionDialog.qml
%{_datadir}/kcm_networkmanagement/qml/ConfigurationDialog.qml
%dir %{_libdir}/qt5/plugins/plasma/network
%dir %{_libdir}/qt5/plugins/plasma/network/vpn
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_pptpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_sshui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
%{_datadir}/qlogging-categories5/plasma-nm.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so
%{_desktopdir}/kcm_networkmanagement.desktop

%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
