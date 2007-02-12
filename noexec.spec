Summary:	Run a process unable to create childs
Summary(pl.UTF-8):	Uruchamianie procesu bez możliwości tworzenia potomków
Name:		noexec
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/noexec/%{name}-%{version}.tar.gz
# Source0-md5:	288680a3ac5dc237f0881e3967aa844d
URL:		http://noexec.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You want to run a process which will be unable to create a child (for
example you want run less via sudo and disable escaping to the shell).

%description -l pl.UTF-8
Ten program pozwala na uruchomienie procesu bez możliwości tworzenia
potomków (na przykład żeby uruchomić less przez sudo bez możliwości
wyskoczenia do powłoki).

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/noexec
%attr(755,root,root) %{_libdir}/*.so
%{_mandir}/man?/*
