#
# Conditional build:
%bcond_without	python2	# Python 2.x modules
%bcond_without	python3	# Python 3.x modules
%bcond_without	tests	# unit tests
#
# NOTE:
# - as we use system tzdata package, keeping this pkg up to the latest is
#   pointless if only data has changed
# - ...but other packages may require newer version anyway, through egg dependencies
%define 	module		pytz
%define 	pypi_name	pytz
%define 	olsonver	2019c
Summary:	pytz - Olson timezone database in Python
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2019.3
Release:	1
License:	MIT or ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytz/
Source0:	https://files.pythonhosted.org/packages/source/p/pytz/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	c3d84a465fc56a4edd52cca8873ac0df
Patch0:		zoneinfo.patch
URL:		http://pytz.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with python2}
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.4
Requires:	tzdata-zoneinfo >= %{olsonver}
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
Requires:	python3-modules >= 1:3.2
Requires:	tzdata-zoneinfo >= %{olsonver}

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
v=$(sed -rne "s/^OLSON_VERSION = '(.+)'/\1/p" pytz/__init__.py)
test "$v" = "%{olsonver}"

%if %{with python2}
%py_build
%py_lint

%if %{with tests}
%{__python} -munittest discover -s pytz/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -munittest discover -s pytz/tests
%endif
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

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pytz/zoneinfo
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py_sitescriptdir}/pytz
%{py_sitescriptdir}/pytz-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py3_sitescriptdir}/pytz
%{py3_sitescriptdir}/pytz-%{version}-py*.egg-info
%endif
