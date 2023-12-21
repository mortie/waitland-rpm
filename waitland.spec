Name:    waitland
Version: 1.0.0
Release: %autorelease
Summary: Tool to wait for a Wayland compositor connection to close
License: MIT
URL:     https://github.com/mortie/waitland
Source:  https://github.com/mortie/waitland/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: wayland-devel

Requires: libwayland-client

%description
Waitland lets you wait for a Wayland compositor to die in a script,
or run a program when the compositor dies.

%prep
%autosetup

%build
%make_build BINDIR=%{_bindir}

%install
%make_install BINDIR=%{_bindir}

%files
%{_bindir}/waitland

%license LICENSE

%changelog
%autochangelog
