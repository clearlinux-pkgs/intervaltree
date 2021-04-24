#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intervaltree
Version  : 3.0.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/e8/f9/76237755b2020cd74549e98667210b2dd54d3fb17c6f4a62631e61d31225/intervaltree-3.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/f9/76237755b2020cd74549e98667210b2dd54d3fb17c6f4a62631e61d31225/intervaltree-3.0.2.tar.gz
Summary  : Editable interval tree data structure for Python 2 and 3
Group    : Development/Tools
License  : Apache-2.0
Requires: intervaltree-license = %{version}-%{release}
Requires: intervaltree-python = %{version}-%{release}
Requires: intervaltree-python3 = %{version}-%{release}
Requires: sortedcontainers
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : pytest-python
BuildRequires : sortedcontainers

%description
intervaltree
        ============
        
        A mutable, self-balancing interval tree for Python 2 and 3. Queries may be by point, by range overlap, or by range envelopment.
        
        This library was designed to allow tagging text and time intervals, where the intervals include the lower bound but not the upper bound.
        
        **Version 3 changes!**

%package license
Summary: license components for the intervaltree package.
Group: Default

%description license
license components for the intervaltree package.


%package python
Summary: python components for the intervaltree package.
Group: Default
Requires: intervaltree-python3 = %{version}-%{release}

%description python
python components for the intervaltree package.


%package python3
Summary: python3 components for the intervaltree package.
Group: Default
Requires: python3-core
Provides: pypi(intervaltree)
Requires: pypi(sortedcontainers)

%description python3
python3 components for the intervaltree package.


%prep
%setup -q -n intervaltree-3.0.2
cd %{_builddir}/intervaltree-3.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393279
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intervaltree
cp %{_builddir}/intervaltree-3.0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/intervaltree/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intervaltree/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
