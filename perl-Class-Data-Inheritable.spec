#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Data-Inheritable
Summary:	Class::Data::Inheritable - inheritable, overridable class data
Summary(pl):	Class::Data::Inheritable - dziedziczona, przykrywalna klasa danych
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	4
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3a9fff92ede1085643341179fd9263b
BuildRequires:	perl-devel >= 5.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Data::Inheritable is for creating accessor/mutators to class
data.  That is, if you want to store something about your class as
a whole (instead of about a single object).  This data is then
inherited by your subclasses and can be overriden.

%description -l pl
Modu³ Class::Data::Inheritable s³u¿y do tworzenia dodatkowych danych
klasy (accessors/mutators), czyli do przechowywania czego¶ o klasie
jako ca³o¶ci (zamiast o pojedynczym obiekcie). Te dane s± potem
dziedziczone przez podklasy i mog± byæ przykryte innymi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Class/Data/
%{_mandir}/man3/*
