#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Pod
Summary:	Test::Pod - check for POD errors in files
Summary(pl):	Modu� Test::Pod - szukaj�cy b��d�w POD w plikach
Name:		perl-Test-Pod
Version:	0.95
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b2a233f5f443f5b5789a5cca449d4f4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Test-Manifest
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-IO-Null
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for errors or warnings in a test file, using Pod::Checker
to do the heavy lifting.

THIS IS ALPHA SOFTWARE.

%description -l pl
Ten modu� przeszukuje pliki POD pod k�tem b��d�w lub ostrze�e� w pliku
testowym, przy u�yciu modu� Pod::Checker. Uwaga: wersja ALPHA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
