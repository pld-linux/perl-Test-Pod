#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Pod
Summary:	Test::Pod Perl module - check for POD errors in files
Summary(pl):	Modu³ Perla Test::Pod - szukanie b³êdów POD w plikach
Name:		perl-Test-Pod
Version:	1.16
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23e46084f9cbf40b8c2edb7ef59670a3
BuildRequires:	perl-devel >= 5.8
%if %{with tests}
BuildRequires:	perl-Test-Builder-Tester
BuildRequires:	perl-Pod-Simple >= 2.04
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for errors or warnings in a test file, using Pod::Checker
to do the heavy lifting.

%description -l pl
Ten modu³ przeszukuje pliki POD pod k±tem b³êdów lub ostrze¿eñ w pliku
testowym, przy u¿yciu modu³ Pod::Checker.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
