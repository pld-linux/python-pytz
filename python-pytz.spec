# NOTE
# - as we use system tzdata package, keeping this pkg up to the latest is
#   pointless if only data has changed
%define 	module	pytz
Summary:	pytz - Olson timezone database in Python
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2012c
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pytz/%{module}-%{version}.tar.bz2
# Source0-md5:	660e0cee7f6c419ca2665db460f65131
Patch0:		zoneinfo.patch
URL:		http://sourceforge.net/projects/pytz/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python >= 1:2.3
BuildRequires:	rpmbuild(macros) >= 1.469
Requires:	python >= 1:2.3
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

%prep
%setup -q -n %{module}-%{version}

# strip zones list before patching
mv pytz/__init__.py pytz/__init__.py.old
cat pytz/__init__.py.old | \
%{__sed} -e "/^all_timezones = \\\/,/^ 'WET',/d" | %{__sed} -e "/^common_timezones = \\\/,/ 'UTC'/d" \
> pytz/__init__.py

%patch0 -p1

%build
%{__python} setup.py build
%py_lint

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT \

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pytz/zoneinfo

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{py_sitescriptdir}/pytz
%{py_sitescriptdir}/pytz-%{version}-py*.egg-info
