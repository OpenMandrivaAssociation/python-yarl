%global srcname yarl

Name:		python-%{srcname}
Version:	1.8.0
Release:	1
Summary:	A Python module to handle URLs
License:	ASL 2.0
URL:		https://yarl.readthedocs.io
Source0:	https://github.com/aio-libs/yarl/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:		yarl-1.7.2-fix-header.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python-cython
BuildRequires:	python3dist(multidict)
BuildRequires:	python-idna

%description
The module provides handy URL class for URL parsing and changing.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/%{srcname}/
%{python_sitearch}/%{srcname}-*.egg-info/
