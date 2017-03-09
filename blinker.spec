#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blinker
Version  : 1.4
Release  : 15
URL      : https://pypi.python.org/packages/source/b/blinker/blinker-1.4.tar.gz
Source0  : https://pypi.python.org/packages/source/b/blinker/blinker-1.4.tar.gz
Summary  : Fast, simple object-to-object and broadcast signaling
Group    : Development/Tools
License  : MIT
Requires: blinker-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
[![Build Status](https://travis-ci.org/jek/blinker.svg?branch=master)](https://travis-ci.org/jek/blinker)

%package python
Summary: python components for the blinker package.
Group: Default

%description python
python components for the blinker package.


%prep
%setup -q -n blinker-1.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489028832
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489028832
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
