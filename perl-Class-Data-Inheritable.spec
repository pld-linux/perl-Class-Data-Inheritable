#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Data-Inheritable
Summary:	Class::Data::Inheritable - inheritable, overridable class data
Summary(pl.UTF-8):	Class::Data::Inheritable - dziedziczona, przykrywalna klasa danych
Name:		perl-Class-Data-Inheritable
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc0fe65926eb8fb932743559feb54eb9
URL:		http://search.cpan.org/dist/Class-Data-Inheritable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Data::Inheritable is for creating accessor/mutators to class
data.  That is, if you want to store something about your class as
a whole (instead of about a single object).  This data is then
inherited by your subclasses and can be overriden.

%description -l pl.UTF-8
Moduł Class::Data::Inheritable służy do tworzenia dodatkowych danych
klasy (accessors/mutators), czyli do przechowywania czegoś o klasie
jako całości (zamiast o pojedynczym obiekcie). Te dane są potem
dziedziczone przez podklasy i mogą być przykryte innymi.

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
%{perl_vendorlib}/Class/Data/Inheritable.pm
%{_mandir}/man3/Class::Data::Inheritable.3pm*
