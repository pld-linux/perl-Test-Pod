#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Pod
Summary:	Test::Pod - check for POD errors in files
Summary(pl):	Modu³ Test::Pod - szukaj±cy b³êdów POD w plikach
Name:		perl-Test-Pod
Version:	0.61
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Test-Manifest
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for errors or warnings in a test file, using Pod::Checker
to do the heavy lifting.

THIS IS ALPHA SOFTWARE.

%description -l pl
Ten modu³ przeszukuje pliki POD pod k±tem b³êdów lub ostrze¿eñ w pliku
testowym, przy u¿yciu modu³ Pod::Checker. Uwaga: wersja ALPHA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
