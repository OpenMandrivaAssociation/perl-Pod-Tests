%define upstream_name Pod-Tests
%define upstream_version 1.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Extracts embedded tests and code examples from POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a specialized POD viewer to extract embedded tests and code examples
from POD. It doesn't do much more than that. pod2test does the useful work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 Changes README
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/pod2test
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.0
+ Revision: 407969
- rebuild using %%perl_convert_version

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.0
+ Revision: 235607
- update to new version 1.19

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.18-4mdv2008.1
+ Revision: 154210
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-3mdv2008.0
+ Revision: 90070
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.18-2mdv2007.0
+ Revision: 108466
- rebuild
- Import perl-Pod-Tests

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- Initial Mandriva release

