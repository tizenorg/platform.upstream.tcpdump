#
# spec file for package tcpdump
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%ifarch s390 s390x
  install -D -m 755 $RPM_SOURCE_DIR/tcpdump-qeth %{buildroot}%{_sbindir}
%endif

%files
%defattr(-,root,root)
%doc CHANGES CREDITS LICENSE README *.awk
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
