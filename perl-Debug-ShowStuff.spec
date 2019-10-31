#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Debug-ShowStuff
Version  : 1.16
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Debug-ShowStuff-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Debug-ShowStuff-1.16.tar.gz
Summary  : 'Debug::ShowStuff - A collection of handy debugging routines for displaying the values of variables with a minimum of coding.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Debug-ShowStuff-license = %{version}-%{release}
Requires: perl-Debug-ShowStuff-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::ISA)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(String::Util)
BuildRequires : perl(Term::ReadKey)
BuildRequires : perl(Text::TabularDisplay)
BuildRequires : perl(Tie::IxHash)

%description
NAME
Debug::ShowStuff - A collection of handy debugging routines for
displaying the values of variables with a minimum of coding.

%package dev
Summary: dev components for the perl-Debug-ShowStuff package.
Group: Development
Provides: perl-Debug-ShowStuff-devel = %{version}-%{release}
Requires: perl-Debug-ShowStuff = %{version}-%{release}

%description dev
dev components for the perl-Debug-ShowStuff package.


%package license
Summary: license components for the perl-Debug-ShowStuff package.
Group: Default

%description license
license components for the perl-Debug-ShowStuff package.


%package perl
Summary: perl components for the perl-Debug-ShowStuff package.
Group: Default
Requires: perl-Debug-ShowStuff = %{version}-%{release}

%description perl
perl components for the perl-Debug-ShowStuff package.


%prep
%setup -q -n Debug-ShowStuff-1.16
cd %{_builddir}/Debug-ShowStuff-1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Debug-ShowStuff
cp %{_builddir}/Debug-ShowStuff-1.16/LICENSE %{buildroot}/usr/share/package-licenses/perl-Debug-ShowStuff/942da4776257084f9987aeea8cacb7ce109f9313
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Debug::ShowStuff.3
/usr/share/man/man3/Debug::ShowStuff::ShowVar.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Debug-ShowStuff/942da4776257084f9987aeea8cacb7ce109f9313

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Debug/ShowStuff.pm
/usr/lib/perl5/vendor_perl/5.28.2/Debug/ShowStuff.pod
/usr/lib/perl5/vendor_perl/5.28.2/Debug/ShowStuff/ShowVar.pm
/usr/lib/perl5/vendor_perl/5.28.2/Debug/ShowStuff/ShowVar.pod
