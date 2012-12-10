Summary:	A modeling and composition program
Name:		kpovmodeler
Version: 	1.1.3
Release: 	5
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/4.1.0/src/extragear/%name-%version-kde4.1.0.tar.bz2
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kpovmodeler.org
BuildRequires: 	kdelibs4-devel
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
export LDFLAGS="$LDFLAGS -lkdeui -lQtGui"
%cmake_kde4
%make

%install
cd build
%{makeinstall_std}
cd -

rm -f %buildroot%_kde_libdir/*.so

%find_lang %name --with-html


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-5mdv2011.0
+ Revision: 620040
- the mass rebuild of 2010.0 packages

* Sat Sep 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.3-4mdv2010.0
+ Revision: 438571
- Obsolete kde3 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-3mdv2010.0
+ Revision: 438165
- rebuild

* Wed Nov 26 2008 Funda Wang <fwang@mandriva.org> 1.1.3-2mdv2009.1
+ Revision: 307004
- obsoletes old kde3 apps

* Tue Jul 29 2008 Funda Wang <fwang@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 252949
- New version 1.1.3

* Sat Jul 19 2008 Funda Wang <fwang@mandriva.org> 1.1.2-4mdv2009.0
+ Revision: 238671
- conflicts with older kde-i18n

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 1.1.2-3mdv2009.0
+ Revision: 236114
- drop versioned conflicts, as it conflicts with same soname
- conflicts with libs

* Tue Jul 15 2008 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2009.0
+ Revision: 236071
- import kpovmodeler


