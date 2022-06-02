#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Reply
Summary:	Reply - read, eval, print, loop, yay!
Summary(pl.UTF-8):	Reply - read, eval, print, loop, yay! - przetwarzanie w pętli
Name:		perl-Reply
Version:	0.42
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DO/DOY/Reply-%{version}.tar.gz
# Source0-md5:	194495d634db7d8636e42ea49295914a
URL:		https://metacpan.org/dist/Reply
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Config-INI-Reader-Ordered
BuildRequires:	perl-Devel-LexAlias
BuildRequires:	perl-Eval-Closure >= 0.11
BuildRequires:	perl-File-HomeDir
BuildRequires:	perl-Getopt-Long >= 2.36
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Package-Stash
BuildRequires:	perl-PadWalker
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Term-ANSIColor
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NOTE: This is an early release, and implementation details of this
module are still very much in flux.

Reply is a lightweight, extensible REPL for Perl. It is plugin-based
(Reply::Plugin), and through plugins supports many advanced features
such as coloring and pretty printing, readline support, and pluggable
commands.

%description -l pl.UTF-8
UWAGA: to jest wczesne wydanie i szczegóły implementacji modułu często
się zmieniają.

Reply to lekka, rozszerzalna implementacja REPL (Read-Eval-Print-Loop,
czyli odczyt-przeliczenie-wypisanie-zapętlenie) dla Perla. Jest oparta
na wtyczkach (Reply::Plugin) i poprzez wtyczki obsługuje wiele
zaawansowanych funkcji, takich jak kolorowanie czy ładne wypisywanie,
obsługa readline i ładowalne polecenia.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/reply
%{perl_vendorlib}/Reply.pm
%{perl_vendorlib}/Reply
%{_mandir}/man1/reply.1*
%{_mandir}/man3/Reply*.3pm*
