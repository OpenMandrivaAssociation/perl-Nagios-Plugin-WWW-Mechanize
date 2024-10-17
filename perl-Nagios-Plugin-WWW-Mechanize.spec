%define upstream_name    Nagios-Plugin-WWW-Mechanize
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Summary:	Login to a web page as a user and get data as a Nagios plugin
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Nagios/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Nagios::Plugin)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(WWW::Mechanize)
BuildArch:	noarch

%description
This module ties Nagios::Plugin with WWW::Mechanize so that there's less
code in your perl script and the most common work is done for you.

For example, the plugin will automatically call nagios_exit(CRITICAL, ...)
if a page is unavailable or a submit_form fails. The plugin will also keep
a track of the time for responses from the remote web server and output
that as performance data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/Nagios

%changelog
* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 461331
- update to 0.13

* Thu Oct 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-2mdv2010.0
+ Revision: 458765
- ensure backportability

* Tue Sep 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 443244
- import perl-Nagios-Plugin-WWW-Mechanize


* Tue Sep 15 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
