%global srcname yarl

Name:           python-%{srcname}
Version:        1.4.2
Release:        3%{?dist}
Summary:        A Python module to handle URLs

License:        ASL 2.0
URL:            https://yarl.readthedocs.io
Source0:        https://github.com/aio-libs/yarl/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

%description
The module provides handy URL class for URL parsing and changing.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-cython
BuildRequires:  python3dist(multidict)
BuildRequires:  python-idna

%description -n python3-%{srcname}
The module provides handy URL class for URL parsing and changing.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/
