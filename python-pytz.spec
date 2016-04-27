#
# Conditional build:
%bcond_without	python2	# Python 2.x modules
%bcond_without	python3	# Python 3.x modules
#
# NOTE
# - as we use system tzdata package, keeping this pkg up to the latest is
#   pointless if only data has changed, but other packages may require
#   newer version anyway, through egg dependencies
%define 	module	pytz
Summary:	pytz - Olson timezone database in Python
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2016.4
Release:	1
License:	MIT or ZPL v2.1
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/f4/7d/7c0c85e9c64a75dde11bc9d3e1adc4e09a42ce7cdb873baffa1598118709/%{module}-%{version}.tar.bz2
# Source0-md5:	e56283d61935963157aebc5135206a47
Patch0:		zoneinfo.patch
URL:		http://pytz.sourceforge.net/
BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python >= 1:2.3
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
Requires:	python >= 1:2.3
%endif
Requires:	tzdata >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher.

%description -l pl.UTF-8
pytz dodaje do Pythona moduł umożliwiający odpytywanie bazy stref
czasowych Olsona. Moduł ten umożliwia przeprowadzanie dokładnych,
niezależnych od platformy obliczeń uwzględniających strefy czasowe
przy użyciu Pythona w wersji co najmniej 2.3.

%package -n python3-%{module}
Summary:	pytz - Olson timezone database in Python 3.x
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie 3.x
Group:		Libraries/Python
Requires:	tzdata >= %{version}

%description -n python3-%{module}
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 3.x

%description -n python3-%{module} -l pl.UTF-8
pytz dodaje do Pythona moduł umożliwiający odpytywanie bazy stref
czasowych Olsona. Moduł ten umożliwia przeprowadzanie dokładnych,
niezależnych od platformy obliczeń uwzględniających strefy czasowe
przy użyciu Pythona 3.x

%prep
%setup -q -n %{module}-%{version}

# strip zones list before patching
%{__sed} -i -e "/^all_timezones = \\\\/,/^ 'Zulu'/d" \
	-e "/^common_timezones = \\\\/,/ 'UTC'/d" pytz/__init__.py

%patch0 -p1

%build
%if %{with python2}
%py_build
%py_lint
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pytz/zoneinfo
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{py_sitescriptdir}/pytz
%{py_sitescriptdir}/pytz-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{py3_sitescriptdir}/pytz
%{py3_sitescriptdir}/pytz-%{version}-py*.egg-info
%endif
