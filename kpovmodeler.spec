Summary:	A modeling and composition program
Name:		kpovmodeler
Version:	1.1.3
Release:	7
License:	GPLv2+
Group:		Graphics
Url:		https://www.kpovmodeler.org
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/4.1.0/src/extragear/%{name}-%{version}-kde4.1.0.tar.bz2
Patch0:		kpovmodeler-1.1.3-kde4.1.0-cmake.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

%description
Program to enter scenes for the 3D rendering engine PovRay.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/dbus-1/interfaces/org.kde.%{name}.xml
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_appsdir}/%{name}/
%{_kde_iconsdir}/*/*/*/*.png

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname lkpovmodeler %{major}

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 1.1.3-6

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_kde_libdir}/liblkpovmodeler.so.%{major}*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-kde4.1.0
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_libdir}/*.so

%find_lang %{name} --with-html

