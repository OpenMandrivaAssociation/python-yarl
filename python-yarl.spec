%global debug_package %{nil}
%define module yarl

Name:		python-yarl
Version:	1.23.0
Release:	1
Summary:	A Python module to handle URLs
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/aio-libs/yarl
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem: python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(expandvars)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(multidict)
BuildRequires:	python%{pyver}dist(idna)
BuildRequires:	python%{pyver}dist(wheel)
%rename python3-yarl

%description
The module provides handy URL class for URL parsing and changing.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc CHANGES.rst README.rst
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
