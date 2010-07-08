
%define 	module	pytz

Summary:	pytz - Olson timezone database in Python
Summary(pl.UTF-8):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2009n
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pytz/%{module}-%{version}.tar.bz2
# Source0-md5:	7f069d7221bbe0a580c2300677e204ce
URL:		http://sourceforge.net/projects/pytz/
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pytz
%{py_sitescriptdir}/pytz-%{version}-py*.egg-info
