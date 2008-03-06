#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UTF8BOM
Summary:	UTF8BOM - handling Byte Order Mark for UTF-8 files
Name:		perl-UTF8BOM
Version:	1.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/L/LY/LYOKATO/UTF8BOM-%{version}.tar.gz
# Source0-md5:	9347f9157119cb1a2361a71b7be94eef
URL:		http://search.cpan.org/dist/UTF8BOM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules allows you to insert UTF8's BOM into strings and files,
or remove it from them easily.

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
%attr(755,root,root) %{_bindir}/utf8bom
%{perl_vendorlib}/*.pm
%{_mandir}/man1/utf8bom.1p*
%{_mandir}/man3/UTF8BOM.3pm*
