%global debug_package %{nil}
%define module yarl

Name:		python-yarl
Version:	1.22.0
Release:	1
Summary:	A Python module to handle URLs
License:	Apache-2.0
URL:		https://github.com/aio-libs/yarl/
Group:		Development/Python
Source0:	https://github.com/aio-libs/yarl/releases/download/v%{version}/%{module}-%{version}.tar.gz
BuildSystem: python

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(expandvars)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(multidict)
BuildRequires:	python%{pyver}dist(idna)
%rename python3-yarl

%description
The module provides handy URL class for URL parsing and changing.

%files
%{python_sitearch}/%{module}/
%{python_sitearch}/%{module}-%{version}.dist-info/
%license LICENSE
%doc CHANGES.rst README.rst
