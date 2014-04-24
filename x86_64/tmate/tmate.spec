%global realname tmate

Name:           %{realname}
Version:        1.8.9
Release:        1%{?dist}
Summary:        Collaborative TMUX session server

Group:          Development/Languages
License:        MIT
URL:            https://github.com/nviennot/tmate-slave
Source0:        https://github.com/nviennot/%{realname}-slave/archive/base.tar.gz
Source100:	https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glibc
BuildRequires: glibc-devel
BuildRequires: pam-devel
BuildRequires: perl-ExtUtils-CBuilder
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kernel-devel
BuildRequires: make
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: gettext-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: ncurses
BuildRequires: ncurses-devel

BuildArch:      x86_64

%description
tmate-slave is the server side part of tmate.io.

%prep
%setup -q
%{__tar} zxf %{SOURCE100}
%setup -T -D -a 100
cd libevent-2.0.21-stable
./configure
make
make install

%build
#bash create_keys.sh > tmate-slave-footprints.txt
./autogen.sh
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/lib" make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/tmate-slave
/usr/local/share/man/man1/tmate.1

%changelog
* Thu Apr 24 2014 Mike Mackintosh <m@zyp.io> - 1.8.9-1
- Initial RPM
