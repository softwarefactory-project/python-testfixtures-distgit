%global        sum  A collection of helpers and mock objects for unit tests and doc tests.
%global        uname testfixtures

Name:          python-%{uname}
Version:       4.13.4
Release:       2%{?dist}
Summary:       %{sum}

URL:           https://pypi.python.org/pypi/%{uname}
Source:        https://pypi.io/packages/source/t/%{uname}/%{uname}-%{version}.tar.gz
License:       MIT

BuildArch:     noarch

Buildrequires: python-setuptools
Buildrequires: python2-devel
Buildrequires: python-wheel
Buildrequires: python2-twine
Buildrequires: python-sphinx
Buildrequires: python2-pkginfo

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{uname}
%{python2_sitelib}/*

%changelog
* Thu Mar 2 2017 Nicolas Hicher <nhicher@redhat.com> 4.13.4-2
- normalize spec file

* Mon Feb 28 2017 Nicolas Hicher <nhicher@redhat.com> 4.13.4-1
- initial package
