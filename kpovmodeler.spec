Summary:	A modeling and composition program
Name:		kpovmodeler
Version: 	1.1.3
Release: 	%mkrel 5
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/4.1.0/src/extragear/%name-%version-kde4.1.0.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kpovmodeler.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
%if %mdkversion < 200900
Obsoletes:	kdegraphics-kpovmodeler < 1:3.5.10-3
%endif
%if %mdkversion < 200100
Obsoletes:  kdegraphics3-kpovmodeler < 1:3.5.10-5
%endif
Conflicts:	kde-l10n < 3.5.9-5

%description 
Program to enter scenes for the 3D rendering engine PovRay.

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
%setup -q -n %name-%version-kde4.1.0

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
