%define 	module	pytz
Summary:	pytz - Olson timezone database in Python
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2010l
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pytz/%{module}-%{version}.tar.bz2
# Source0-md5:	8ea38ffd627f2169b597442928ea5967
Patch0:		zoneinfo.patch
URL:		http://sourceforge.net/projects/pytz/
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
Requires:	tzdata
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher.

%description -l pl.UTF-8
pytz dodaje do Pythona moduł umożliwiający odpytywanie bazy stref
czasowych Olsona. Moduł ten umożliwia przeprowadzanie dokładnych,
niezależnych od platformy obliczeń uwzględniających strefy czasowy
przy użyciu Pythona w wersji co najmniej 2.3.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/pytz/zoneinfo

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pytz
%{py_sitescriptdir}/pytz-%{version}-py*.egg-info
