#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	Pod
Summary:	Test::Pod Perl module - check for POD errors in files
Summary(pl.UTF-8):	Moduł Perla Test::Pod - szukanie błędów POD w plikach
Name:		perl-Test-Pod
Version:	1.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	472dda77746d48e6465bf62e47aeca81
URL:		https://metacpan.org/dist/Test-Pod
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Test::Builder::Tester) >= 1.02
BuildRequires:	perl-Pod-Simple >= 3.06
BuildRequires:	perl-Test-Simple >= 0.62
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for errors or warnings in a test file, using
Pod::Checker to do the heavy lifting.

%description -l pl.UTF-8
Ten moduł przeszukuje pliki POD pod kątem błędów lub ostrzeżeń w pliku
testowym, wykorzystując do tego moduł Pod::Checker.

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
%doc Changes
%{perl_vendorlib}/Test/Pod.pm
%{_mandir}/man3/Test::Pod.3pm*
