%global snapshot_suffix .20160307git
%define debug_package %{nil}

Name: network-testing
Version: 0.0.1
Release: 0.15%{?snapshot_suffix}%{?dist}
Summary: Network application testing project
License: BSD
URL: https://sourceware.org/%{name}/
Source0: %{name}-0.0.1.tar.gz
BuildRequires: python2-devel
Requires: python-ptrace netresolve iproute
%description
Network application testing project provides a test driver written in Python
and a set of application tests. Tests are run in different network scenarios
using kernel network namespaces.

%prep
%setup

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
chmod +x %{buildroot}/usr/lib*/python*/site-packages/network_testing/data/testcases/client-server/netresolve/{client,server}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
