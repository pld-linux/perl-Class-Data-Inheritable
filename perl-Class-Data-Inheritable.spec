%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Data-Inheritable
Summary:	Class::Data::Inheritable perl module
Summary(pl):	Modu³ perla Class::Data::Inheritable
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Class/Data/Inheritable.pm
%{_mandir}/man3/*
