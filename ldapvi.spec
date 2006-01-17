Summary:	LDAP LDIF Editor
Summary(pl):	Edytor LDAP LDIF
Name:		ldapvi
Group:		Networking/Utilities
License:	GPL v2
Version:	1.5
Release:	2
Source0:	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	e98f9fbd5596aac81373a849888a87f1
URL:		http://www.lichteblau.com/src.html
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	ncurses-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAPvi allows retrieving LDAP database records, edit them in LDIF
format within a text editor and store the changed records back via
LDAP.

%description -l pl
LDAPvi jest narzêdziem do obróbki rekordów katalogu LDAP. Pozwala
modyfikowaæ je w formacie LDIF edytorem tekstowym i zachowywaæ zmiany
z powrotem w LDAP-ie.

%prep
%setup -q

%build
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
