%define real_name Pod-Tests

Summary:	Extracts embedded tests and code examples from POD
Name:		perl-%real_name
Version:	0.18
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a specialized POD viewer to extract embedded tests and code examples
from POD. It doesn't do much more than that. pod2test does the useful work.

%prep

%setup -q -n %{real_name}-%{version} 

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
