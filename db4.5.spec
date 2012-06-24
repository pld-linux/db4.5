#
# Conditional build:
%if "%{pld_release}" == "ac"
%bcond_with	java		# build Java library
%bcond_with	nptl		# use process-shared POSIX mutexes (NPTL provides full interface)
%else
%bcond_without	java		# don't build Java library
%bcond_without	nptl		# don't use process-shared POSIX mutexes (NPTL provides full interface)
%endif
%bcond_without	tcl		# don't build Tcl bindings
%bcond_with	pmutex		# use process-shared POSIX mutexes (not available with linuxthreads)
%bcond_without	static_libs	# don't build static libraries
%bcond_with	default_db	# use this db as default system db
%bcond_with	rpm_robustness	# apply rpm-robustness patch (use robust mutexes)
#
%define		mver		4.5
%define		ver		%{mver}.20
%define		patchlevel	2
%{?with_nptl:%define	with_pmutex	1}
%ifnarch i586 i686 athlon pentium3 pentium4 %{x8664}
%undefine with_java
%endif

Summary:	Berkeley DB database library for C
Summary(pl.UTF-8):	Biblioteka C do obsługi baz Berkeley DB
Name:		db4.5
Version:	%{ver}.%{patchlevel}
Release:	1
Epoch:		0
License:	Sleepycat public license (GPL-like, see LICENSE)
Group:		Libraries
#Source0Download: http://www.oracle.com/technetwork/database/berkeleydb/downloads/index-082944.html
Source0:	http://download.oracle.com/berkeley-db/db-%{ver}.tar.gz
# Source0-md5:	b0f1c777708cb8e9d37fb47e7ed3312d
%patchset_source -f http://download.oracle.com/berkeley-db/patches/db/%{ver}/patch.%{ver}.%g 1 %{patchlevel}
Patch0:		db-rpm-robustness.patch
URL:		http://www.oracle.com/technetwork/database/berkeleydb/downloads/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.426
BuildRequires:	sed >= 4.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.0}
%{?with_rpm_robustness:Requires:	uname(release) >= 2.6.17}
%{?with_nptl:Requires:	uname(release) >= 2.6.0}
%if %{with default_db}
Provides:	db = %{version}-%{release}
Obsoletes:	db4
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{without default_db}
%define		_includedir	%{_prefix}/include/db4.2
%endif

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%description -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley db jest używana w wielu aplikacjach, w tym w
Pythonie i Perlu.

%package devel
Summary:	Header files for Berkeley database library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-devel = %{version}-%{release}
Obsoletes:	db3-devel
Obsoletes:	db4-devel
%endif

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%description devel -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera pliki nagłówkowe i dokumentację do budowania
programów używających Berkeley DB.

%package static
Summary:	Static libraries for Berkeley database library
Summary(pl.UTF-8):	Statyczne biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-static = %{version}-%{release}
Obsoletes:	db3-static
Obsoletes:	db4-static
%endif

%description static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the static libraries for building programs which
use Berkeley DB.

%description static -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera statyczne biblioteki do budowania programów
używających Berkeley DB.

%package cxx
Summary:	Berkeley database library for C++
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla C++
Group:		Libraries
%if %{with default_db}
Provides:	db-cxx = %{version}-%{release}
Obsoletes:	db4-cxx
%endif

%description cxx
Berkeley database library for C++.

%description cxx -l pl.UTF-8
Biblioteka baz danych Berkeley dla C++.

%package cxx-devel
Summary:	Header files for db-cxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-devel = %{version}-%{release}
%endif
Conflicts:	db-devel < 4.1.25-3

%description cxx-devel
Header files for db-cxx library.

%description cxx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki db-cxx.

%package cxx-static
Summary:	Static version of db-cxx library
Summary(pl.UTF-8):	Statyczna wersja biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-static = %{version}-%{release}
%endif
Conflicts:	db-static < 4.2.50-1

%description cxx-static
Static version of db-cxx library.

%description cxx-static -l pl.UTF-8
Statyczna wersja biblioteki db-cxx.

%package java
Summary:	Berkeley database library for Java
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Javy
Group:		Libraries
Requires:	jpackage-utils
%if %{with default_db}
Provides:	db-java = %{version}-%{release}
%endif

%description java
Berkeley database library for Java.

%description java -l pl.UTF-8
Biblioteka baz danych Berkeley dla Javy.

%package java-devel
Summary:	Development files for db-java library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-java
Group:		Development/Languages/Java
Requires:	%{name}-java = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-java-devel = %{version}-%{release}
%endif
Conflicts:	db-devel < 4.1.25-3

%description java-devel
Development files for db-java library.

%description java-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-java.

%package tcl
Summary:	Berkeley database library for Tcl
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Tcl
Group:		Development/Languages/Tcl
Requires:	tcl
%if %{with default_db}
Provides:	db-tcl = %{version}-%{release}
Obsoletes:	db4-tcl
%endif

%description tcl
Berkeley database library for Tcl.

%description tcl -l pl.UTF-8
Biblioteka baz danych Berkeley dla Tcl.

%package tcl-devel
Summary:	Development files for db-tcl library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-tcl
Group:		Development/Languages/Tcl
Requires:	%{name}-tcl = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-tcl-devel = %{version}-%{release}
%endif
Conflicts:	db-devel < 4.1.25-3

%description tcl-devel
Development files for db-tcl library.

%description tcl-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-tcl.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Summary(pl.UTF-8):	Narzędzia do obsługi baz Berkeley DB z linii poleceń
Group:		Applications/Databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
%if %{with default_db}
Provides:	db-utils = %{version}-%{release}
Obsoletes:	db3-utils
Obsoletes:	db4-utils
%endif

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB
databases.

%description utils -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera narzędzia do obsługi baz Berkeley DB z linii
poleceń.

%prep
%setup -q -n db-%{ver}
# official patches
%patchset_patch 1 %{patchlevel}

%{?with_rpm_robustness:%patch0 -p1}

%if %{without nptl}
sed -i -e 's,AM_PTHREADS_SHARED("POSIX/.*,:,' dist/aclocal/mutex.ac
%endif

sed -i -e '/AC_PROG_LIBTOOL/aLT_OUTPUT' dist/configure.ac

%build
cd dist
cp -f /usr/share/aclocal/libtool.m4 aclocal/libtool.ac
cp -f /usr/share/aclocal/ltoptions.m4 aclocal/ltoptions.ac
cp -f /usr/share/aclocal/ltsugar.m4 aclocal/ltsugar.ac
cp -f /usr/share/aclocal/ltversion.m4 aclocal/ltversion.ac
cp -f /usr/share/aclocal/lt~obsolete.m4 aclocal/lt~obsolete.ac
cp -f /usr/share/automake/config.sub .
cp -f /usr/share/libtool/config/ltmain.sh .
sh s_config
cd ..

%if %{with static_libs}
cp -a build_unix build_unix.static

cd build_unix.static

CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
LDFLAGS="%{rpmcflags} %{rpmldflags}"
export CC CXX CFLAGS CXXFLAGS LDFLAGS

../dist/%configure \
	--enable-compat185 \
	--disable-shared \
	--enable-static \
	--enable-rpc \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-cxx

# (temporarily?) disabled because of compilation errors:
#	--enable-dump185 \

%{__make} library_build
cd ..
%endif

cd build_unix

../dist/%configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-compat185 \
	--enable-rpc \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-cxx \
	%{?with_tcl:--enable-tcl} \
	%{?with_tcl:--with-tcl=/usr/lib} \
	%{?with_java:--enable-java} \
	--disable-static \
	--enable-shared

%{__make} library_build \
	TCFLAGS='-I$(builddir) -I%{_includedir}' \
	LIBSO_LIBS="\$(LIBS)" \
	LIBTSO_LIBS="\$(LIBS) -ltcl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}
%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%endif

%if %{with static_libs}
%{__make} -C build_unix.static library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}
%endif

%{__make} -C build_unix library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_INSTALL_FILE_LIST="" \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}

%if %{with default_db}
install -d $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/libdb-%{mver}.so $RPM_BUILD_ROOT/%{_lib}
%endif

cd $RPM_BUILD_ROOT%{_libdir}
%if %{with static_libs}
mv -f libdb.a libdb-%{mver}.a
mv -f libdb_cxx.a libdb_cxx-%{mver}.a
%endif
%if %{with java}
mv -f $RPM_BUILD_ROOT%{_libdir}/*.jar $RPM_BUILD_ROOT%{_javadir}
%endif
%if %{with default_db}
ln -sf /%{_lib}/libdb-%{mver}.so libdb.so
ln -sf /%{_lib}/libdb-%{mver}.so libdb4.so
ln -sf /%{_lib}/libdb-%{mver}.so libdb-%{mver}.so
ln -sf /%{_lib}/libdb-%{mver}.so libndbm.so
ln -sf libdb-%{mver}.la libdb.la
ln -sf libdb-%{mver}.la libdb4.la
ln -sf libdb-%{mver}.la libndbm.la
ln -sf libdb_cxx-%{mver}.so libdb_cxx.so
ln -sf libdb_cxx-%{mver}.la libdb_cxx.la
%if %{with java}
ln -sf libdb_java-%{mver}.la libdb_java.la
%endif
%if %{with tcl}
ln -sf libdb_tcl-%{mver}.so libdb_tcl.so
ln -sf libdb_tcl-%{mver}.la libdb_tcl.la
%endif
%if %{with static_libs}
ln -sf libdb-%{mver}.a libdb.a
ln -sf libdb-%{mver}.a libdb4.a
ln -sf libdb-%{mver}.a libndbm.a
ln -sf libdb_cxx-%{mver}.a libdb_cxx.a
%endif
%endif

sed -i "s/old_library=''/old_library='libdb-%{mver}.a'/" libdb-%{mver}.la
sed -i "s/old_library=''/old_library='libdb_cxx-%{mver}.a'/" libdb_cxx-%{mver}.la

cd -
rm -f examples_c*/tags
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}
cp -rf examples_c/* $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}
cp -rf examples_cxx/* $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}

%if %{with java}
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
cp -rf examples_java/* $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
%else
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/java
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/collections
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/gsg/JAVA
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/gsg_txn/JAVA
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/gsg_db_rep/JAVA
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%if %{with default_db}
%attr(755,root,root) /%{_lib}/libdb-%{mver}.so
%else
%attr(755,root,root) %{_libdir}/libdb-%{mver}.so
%endif
%dir %{_docdir}/db-%{version}-docs
%{_docdir}/db-%{version}-docs/index.html
%{_docdir}/db-%{version}-docs/license

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdb-%{mver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb-%{mver}.so
%attr(755,root,root) %{_libdir}/libdb4.so
%attr(755,root,root) %{_libdir}/libdb.so
%attr(755,root,root) %{_libdir}/libndbm.so
%{_libdir}/libdb4.la
%{_libdir}/libdb.la
%{_libdir}/libndbm.la
%else
%dir %{_includedir}
%endif
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_docdir}/db-%{version}-docs/api_c
%dir %{_docdir}/db-%{version}-docs/gsg
%{_docdir}/db-%{version}-docs/gsg/C
%dir %{_docdir}/db-%{version}-docs/gsg_txn
%{_docdir}/db-%{version}-docs/gsg_txn/C
%dir %{_docdir}/db-%{version}-docs/gsg_db_rep
%{_docdir}/db-%{version}-docs/gsg_db_rep/C
%{_docdir}/db-%{version}-docs/images
%{_docdir}/db-%{version}-docs/ref
%{_examplesdir}/db-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdb-%{mver}.a
%if %{with default_db}
%{_libdir}/libdb4.a
%{_libdir}/libdb.a
%{_libdir}/libndbm.a
%endif
%endif

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-%{mver}.so

%files cxx-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-%{mver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx.la
%endif
%{_includedir}/db_cxx.h
%{_docdir}/db-%{version}-docs/api_cxx
%{_docdir}/db-%{version}-docs/gsg/CXX
%{_docdir}/db-%{version}-docs/gsg_txn/CXX
%{_docdir}/db-%{version}-docs/gsg_db_rep/CXX
%{_examplesdir}/db-cxx-%{version}

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-%{mver}.a
%if %{with default_db}
%{_libdir}/libdb_cxx.a
%endif
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_java-%{mver}.so
%{_javadir}/db.jar

%files java-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_java-%{mver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_java.so
%{_libdir}/libdb_java.la
%endif
%{_docdir}/db-%{version}-docs/collections
%{_docdir}/db-%{version}-docs/gsg/JAVA
%{_docdir}/db-%{version}-docs/gsg_txn/JAVA
%{_docdir}/db-%{version}-docs/gsg_db_rep/JAVA
%{_docdir}/db-%{version}-docs/java
%{_examplesdir}/db-java-%{version}
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_tcl-%{mver}.so

%files tcl-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_tcl-%{mver}.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_tcl.so
%{_libdir}/libdb_tcl.la
%endif
%{_docdir}/db-%{version}-docs/api_tcl
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/berkeley_db_svc
%attr(755,root,root) %{_bindir}/db*_archive
%attr(755,root,root) %{_bindir}/db*_checkpoint
%attr(755,root,root) %{_bindir}/db*_deadlock
%attr(755,root,root) %{_bindir}/db*_dump
#%attr(755,root,root) %{_bindir}/db*_dump185
%attr(755,root,root) %{_bindir}/db*_hotbackup
%attr(755,root,root) %{_bindir}/db*_load
%attr(755,root,root) %{_bindir}/db*_printlog
%attr(755,root,root) %{_bindir}/db*_recover
%attr(755,root,root) %{_bindir}/db*_stat
%attr(755,root,root) %{_bindir}/db*_upgrade
%attr(755,root,root) %{_bindir}/db*_verify
%{_docdir}/db-%{version}-docs/utility
