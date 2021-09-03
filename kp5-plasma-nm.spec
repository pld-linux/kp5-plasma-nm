%define		kdeplasmaver	5.22.5
%define		qtver		5.9.0
%define		kpname		plasma-nm
%define		kf5ver		5.39.0

Summary:	plasma-nm
Name:		kp5-%{kpname}
Version:	5.22.5
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f5c59caedb3b9ae19cdb91f8ba4a7536
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12

BuildRequires:	NetworkManager-devel
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

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
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_l2tpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_openconnectui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_openswanui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_openvpnui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_pptpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_sshui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_sstpui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_strongswanui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_vpncui.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/networkmanagement
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
%{_libdir}/qt5/qml/org/kde/plasma/networkmanagement/qmldir
%{_datadir}/knotifications5/networkmanagement.notifyrc
%{_datadir}/kservices5/plasmanetworkmanagement_l2tpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openconnectui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openswanui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openvpnui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_pptpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_sshui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_sstpui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_strongswanui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_vpncui.desktop
%{_datadir}/kservicetypes5/plasma-networkmanagement-vpnuiplugin.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_networkmanagement.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_fortisslvpnui.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libplasmanetworkmanagement_iodineui.so
%dir %{_datadir}/kcm_networkmanagement
%dir %{_datadir}/kcm_networkmanagement/qml
%{_datadir}/kcm_networkmanagement/qml/ConnectionItem.qml

%{_datadir}/kcm_networkmanagement/qml/ListItem.qml
%{_datadir}/kcm_networkmanagement/qml/main.qml
%{_datadir}/kservices5/kcm_networkmanagement.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_fortisslvpnui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_iodineui.desktop
%{_datadir}/kservices5/plasmanetworkmanagement_openconnect_juniperui.desktop
%{_datadir}/metainfo/org.kde.plasma.networkmanagement.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement/contents.rcc
%{_datadir}/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.json
%{_datadir}/kservices5/plasmanetworkmanagement_openconnect_globalprotectui.desktop
%{_datadir}/kcm_networkmanagement/qml/AddConnectionDialog.qml
%{_datadir}/kcm_networkmanagement/qml/ConfigurationDialog.qml
%{_datadir}/kservices5/plasmanetworkmanagement_openconnect_pulseui.desktop
