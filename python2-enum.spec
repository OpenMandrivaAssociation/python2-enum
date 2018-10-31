%global _python_bytecompile_build 0
%define pyname enum34

Name:           python2-enum
Version:        1.1.6
Release:        2
Summary:        Port of the python 3.4+ enum module to 2.6+
Group:          Development/Python
License:        Python
URL:            https://pypi.python.org/pypi/%{pyname}/%{version}
Source0:        https://pypi.python.org/packages/source/e/%{pyname}/%{pyname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)
BuildRequires:	python2-pkg-resources

%description
Python 3.4 Enum backported to 2.x

%prep
%setup -q -n %{pyname}-%{version}

%build
%__python2 setup.py build

%install
%__python2 setup.py install --skip-build --root=%{buildroot}

%files
%{python2_sitelib}/*
