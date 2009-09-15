%define upstream_name    Nagios-Plugin-WWW-Mechanize
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Login to a web page as a user and get data as a Nagios plugin
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Nagios/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Nagios::Plugin)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(WWW::Mechanize)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/Nagios

