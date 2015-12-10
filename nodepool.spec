Name:		nodepool
Version:	0.2.0
Release:	1%{?dist}
Summary:	Manage a pool of nodes for a distributed test infrastructure

License:	ASL 2.0
URL:		https://launchpad.net/nodepool
Source0:	http://tarballs.openstack.org/nodepool/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-gear
BuildRequires: python-jenkins
BuildRequires: python-novaclient
BuildRequires: python-pbr
BuildRequires: python-PyMySQL
BuildRequires: python-setuptools
BuildRequires: python-testresources
BuildRequires: python-testrepository

Requires: python-PyMySQL

%prep
%setup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%check
%{__python} setup.py testr

%description
Nodepool is a service used by the OpenStack CI team to deploy and manage a pool
of devstack images on a cloud server for use in OpenStack project testing.

%files
%doc LICENSE
%doc README.rst
%{_bindir}/*
%{python_sitelib}/nodepool*

%changelog
* Thu Dec 10 2015 Paul Belanger <pabelanger@redhat.com> - 0.2.0-1
- Initial packaging
