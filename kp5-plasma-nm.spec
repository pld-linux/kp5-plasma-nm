%define		kdeplasmaver	5.5.4
%define		qtver		5.5.1
%define		kpname		plasma-nm
%define		kf5ver		5.5.0

Summary:	plasma-nm
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	70287df57f1869801d4cab8179c20f2e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12

BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}

BuildRequires:	pkgconfig
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	gettext-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-networkmanager-qt-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	kf5-modemmanager-qt-devel
BuildRequires:	openconnect-devel >= 3.99
BuildRequires:	qca-qt5-devel >= 2.1.1
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Nm.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/kde5-nm-connection-editor
%attr(755,root,root) /usr/lib64/libplasmanm_editor.so
%attr(755,root,root) /usr/lib64/libplasmanm_internal.so
%attr(755,root,root) /usr/lib64/qt5/plugins/kf5/kded/networkmanagement.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_l2tpui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_openconnectui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_openswanui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_openvpnui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_pptpui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_sshui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_sstpui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_strongswanui.so
%attr(755,root,root) /usr/lib64/qt5/plugins/libplasmanetworkmanagement_vpncui.so
%attr(755,root,root) /usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
/usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/qmldir
/usr/share/applications/kde5-nm-connection-editor.desktop
/usr/share/knotifications5/networkmanagement.notifyrc
/usr/share/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
/usr/share/kservices5/plasmanetworkmanagement_l2tpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openconnectui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openswanui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openvpnui.desktop
/usr/share/kservices5/plasmanetworkmanagement_pptpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_sshui.desktop
/usr/share/kservices5/plasmanetworkmanagement_sstpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_strongswanui.desktop
/usr/share/kservices5/plasmanetworkmanagement_vpncui.desktop
/usr/share/kservicetypes5/plasma-networkmanagement-vpnuiplugin.desktop
/usr/share/kxmlgui5/kde5-nm-connection-editor/kde5-nm-connection-editorui.rc
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/ConnectionItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/Header.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/PopupDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/SwitchButton.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/Toolbar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.desktop
