%define upstream_name Pod-Tests
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Extracts embedded tests and code examples from POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a specialized POD viewer to extract embedded tests and code examples
from POD. It doesn't do much more than that. pod2test does the useful work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 Changes README
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/pod2test
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
