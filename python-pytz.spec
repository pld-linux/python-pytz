
%define 	module	pytz

Summary:	pytz - Olson timezone database in Python
Summary(pl):	pytz - baza stref czasowych Olsona w Pythonie
Name:		python-%{module}
Version:	2006g
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pytz/%{module}-%{version}.tar.bz2
# Source0-md5:	051d34831b7e4cceb1d94f48ebd896f6
URL:		http://sourceforge.net/projects/pytz/
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher.

%description -l pl
pytz dodaje do Pythona modu³ umo¿liwiaj±cy odpytywanie bazy stref
czasowych Olsona. Modu³ ten umo¿liwia przeprowadzanie dok³adnych,
niezale¿nych od platformy obliczeñ uwzglêdniaj±cych strefy czasowy
przy u¿yciu Pythona w wersji co najmniej 2.3.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pytz
