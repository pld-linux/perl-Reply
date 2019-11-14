#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Reply
%include	/usr/lib/rpm/macros.perl
Summary:	Reply - read, eval, print, loop, yay!
Name:		perl-Reply
Version:	0.42
Release:	1
License:	mit
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DO/DOY/Reply-%{version}.tar.gz
# Source0-md5:	194495d634db7d8636e42ea49295914a
URL:		http://search.cpan.org/dist/Reply/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Config::INI::Reader::Ordered)
BuildRequires:	perl(Devel::LexAlias)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl-Eval-Closure >= 0.11
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Package-Stash
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NOTE: This is an early release, and implementation details of this
module are still very much in flux. Feedback is welcome!

Reply is a lightweight, extensible REPL for Perl. It is plugin-based
(see Reply::Plugin), and through plugins supports many advanced
features such as coloring and pretty printing, readline support, and
pluggable commands.

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
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Reply/
%{_mandir}/man1/reply.1*
%{_mandir}/man3/*
