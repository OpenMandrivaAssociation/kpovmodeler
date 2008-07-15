Summary:	A modeling and composition program
Name:		kpovmodeler
Version: 	1.1.2
Release: 	%mkrel 2
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/4.0.4/src/extragear/%name-%version-kde4.0.4.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kpovmodeler.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
Conflicts:	kdegraphics-kpovmodeler < 1:3.5.9-8
Conflicts:	%{_lib}kdegraphics0-kpovmodeler < 1:3.5.9-8

%description 
Program to enter scenes for the 3D rendering engine PovRay.

%if %mdkversion < 200900
%post
/sbin/ldconfig
%update_menus

%postun
/sbin/ldconfig
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so.*
%_kde_libdir/kde4/*.so
%_kde_datadir/dbus-1/interfaces/*.xml
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/*
%_kde_iconsdir/*/*/*/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-kde4.0.4

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

rm -f %buildroot%_kde_libdir/*.so

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
