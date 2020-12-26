Summary:	Open Asset Import Library
Summary(pl.UTF-8):	Asset Import - otwarta biblioteka do importu danych trójwymiarowych
Name:		assimp
Version:	5.0.1
Release:	2
License:	BSD
Group:		Libraries
Source0:	https://github.com/assimp/assimp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eb7b7385a5c3194ab46d7f869d7ac6cf
Patch0:		%{name}-irrxml.patch
Patch1:		%{name}-pc.patch
URL:		https://www.assimp.org/
BuildRequires:	cmake >= 3.0
BuildRequires:	irrxml-devel
BuildRequires:	libstdc++-devel
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	unzip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Importer library to import assets from different common 3D file
formats such as Collada, Blend, Obj, X, 3DS, LWO, MD5, MD2, MD3, MDL,
MS3D and a lot of other formats. The data is stored in an own
in-memory data-format, which can be easily processed.

%description -l pl.UTF-8
Biblioteka importująca służąca do odczytu danych trójwymiarowych
(assets) z różnych popularnych formatów plików, takich jak Collada,
Blend, Obj, X, 3DS, LWO, MD5, MD2, MD3, MDL, MS3D i innych. Dane są
przechowywane w pamięci, we własnym formacie, który można łatwo
przetworzyć.

%package devel
Summary:	Header files for assimp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki assimp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
The header files needed for development of programs using the assimp
library.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do tworzenia programów wykorzystujących
bibliotekę assimp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DASSIMP_LIB_INSTALL_DIR:PATH=%{_lib} \
	-DSYSTEM_IRRXML=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE Readme.md
%attr(755,root,root) %{_libdir}/libassimp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libassimp.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assimp
%attr(755,root,root) %{_libdir}/libassimp.so
%{_libdir}/cmake/assimp-5.0
%{_includedir}/assimp
%{_pkgconfigdir}/assimp.pc
