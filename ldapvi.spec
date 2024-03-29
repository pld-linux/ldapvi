Summary:	LDAP LDIF Editor
Summary(pl.UTF-8):	Edytor LDAP LDIF
Name:		ldapvi
Version:	1.7
Release:	14
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	6dc2f5441ac5f1e2b5b036e3521012cc
Patch0:		%{name}-getline.patch
Patch1:		%{name}-vim-syntax.patch
URL:		http://www.lichteblau.com/ldapvi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	ncurses-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAPvi allows retrieving LDAP database records, edit them in LDIF
format within a text editor and store the changed records back via
LDAP.

%description -l pl.UTF-8
LDAPvi jest narzędziem do obróbki rekordów katalogu LDAP. Pozwala
modyfikować je w formacie LDIF edytorem tekstowym i zachowywać zmiany
z powrotem w LDAP-ie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i -e 's#curses ncurses#tinfo curses ncurses#g' configure.in

%build
%{__aclocal}
%{__autoconf}
%configure \
	 CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ldapvi $RPM_BUILD_ROOT%{_bindir}
install ldapvi.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/ldapvi
%{_mandir}/man?/*
