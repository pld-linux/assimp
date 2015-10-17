Summary:	Open Asset Import Library
Name:		assimp
Version:	3.1.1
Release:	0.1
License:	distributable
Group:		Libraries
Source0:	http://netix.dl.sourceforge.net/project/%{name}/%{name}-3.1/%{name}-%{version}_no_test_models.zip
# Source0-md5:	ccd4788204509da58a3a53c7aeda7a8b
URL:		http://sourceforge.net/projects/assimp/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	unzip
BuildRequires:	zziplib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Importer library to import assets from different common 3D file formats
such as Collada, Blend, Obj, X, 3DS, LWO, MD5, MD2, MD3, MDL, MS3D
and a lot of other formats. The data is stored in an own in-memory
data-format, which can be easily processed.

%package devel
Summary:	Header files for assimp
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The header files are only needed for development of programs using the
assimplibrary.

%prep
%setup -q

%build
mkdir build
cd build
%cmake \
	CMAKE_HOME_DIR=/usr \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README Readme.md
%attr(755,root,root) %{_libdir}/libassimp.so.3.1.*
%attr(755,root,root) %ghost %{_libdir}/libassimp.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assimp
%attr(755,root,root) %{_libdir}/libassimp.so
%{_libdir}/cmake/assimp-3.1
%{_includedir}/assimp
%{_pkgconfigdir}/assimp.pc

