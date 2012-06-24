%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Data-Inheritable
Summary:	Class::Data::Inheritable Perl module
Summary(cs):	Modul Class::Data::Inheritable pro Perl
Summary(da):	Perlmodul Class::Data::Inheritable
Summary(de):	Class::Data::Inheritable Perl Modul
Summary(es):	M�dulo de Perl Class::Data::Inheritable
Summary(fr):	Module Perl Class::Data::Inheritable
Summary(it):	Modulo di Perl Class::Data::Inheritable
Summary(ja):	Class::Data::Inheritable Perl �⥸�塼��
Summary(ko):	Class::Data::Inheritable �� ����
Summary(no):	Perlmodul Class::Data::Inheritable
Summary(pl):	Modu� Perla Class::Data::Inheritable
Summary(pt):	M�dulo de Perl Class::Data::Inheritable
Summary(pt_BR):	M�dulo Perl Class::Data::Inheritable
Summary(ru):	������ ��� Perl Class::Data::Inheritable
Summary(sv):	Class::Data::Inheritable Perlmodul
Summary(uk):	������ ��� Perl Class::Data::Inheritable
Summary(zh_CN):	Class::Data::Inheritable Perl ģ��
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
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
Modu� Class::Data::Inheritable s�u�y do tworzenia dodatkowych danych
klasy (accessors/mutators), czyli do przechowywania czego� o klasie
jako ca�o�ci (zamiast o pojedynczym obiekcie). Te dane s� potem
dziedziczone przez podklasy i mog� by� przykryte innymi.

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
%{perl_sitelib}/Class/Data/
%{_mandir}/man3/*
