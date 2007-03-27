#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Pod
Summary:	Test::Pod Perl module - check for POD errors in files
Summary(pl.UTF-8):	Moduł Perla Test::Pod - szukanie błędów POD w plikach
Name:		perl-Test-Pod
Version:	1.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f259135656ac4549b65a4f14f07b7c6
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Builder-Tester >= 1.02
BuildRequires:	perl-Pod-Simple >= 2.04
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for errors or warnings in a test file, using Pod::Checker
to do the heavy lifting.

%description -l pl.UTF-8
Ten moduł przeszukuje pliki POD pod kątem błędów lub ostrzeżeń w pliku
testowym, przy użyciu moduł Pod::Checker.

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
