%global srcname yarl

Name:           python-%{srcname}
Version:        1.6.2
Release:        1%{?dist}
Summary:        A Python module to handle URLs

License:        ASL 2.0
URL:            https://yarl.readthedocs.io
Source0:        https://github.com/aio-libs/yarl/archive/v%{version}/%{srcname}-%{version}.tar.gz

%description
The module provides handy URL class for URL parsing and changing.

Provides: python3-yarl

BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-cython
BuildRequires:  python3dist(multidict)
BuildRequires:  python-idna

%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/%{srcname}/
%{python_sitearch}/%{srcname}-*.egg-info/
