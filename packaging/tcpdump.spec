Name:           tcpdump
Version:        4.3.0
Release:        0
License:        BSD-3-Clause
Summary:        A Packet Sniffer
Url:            http://www.tcpdump.org/
Group:          Productivity/Networking/Diagnostic
Source:         http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:        tcpdump-qeth
Patch0:         tcpdump-4.0.0-prototypes.patch
Patch2:         tcpdump-4.0.0-aliasing.patch
Patch3:         tcpdump-4.0.0-uninitialized.patch
BuildRequires:  libpcap-devel
BuildRequires:  libsmi-devel
BuildRequires:  openssl-devel

%description
This program can "read" all or only certain packets going over the
ethernet. It can be used to debug specific network problems.

%prep
%setup -q
%patch0
%patch2
%patch3

%build
export CFLAGS="%{optflags} -Wall -DGUESS_TSO -fstack-protector -fno-strict-aliasing"
%configure \
  --enable-ipv6
make

%install
%make_install

%files
%defattr(-,root,root)
%doc LICENSE README *.awk
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
