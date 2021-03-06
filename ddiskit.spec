Name:           ddiskit
Version:        3.5
Release:        1%{?dist}
Summary:        Tool for Red Hat Enterprise Linux Driver Update Disk creation

License:        GPLv3
URL:            https://github.com/orosp/ddiskit
Source0:        https://github.com/orosp/ddiskit/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?fedora} >= 25
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%else
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%endif

Requires:       rpm createrepo genisoimage
%if 0%{?fedora} >= 23
Suggests:       quilt git
Recommends:     kernel-devel redhat-rpm-config rpm-build
Recommends:     mock
%else
Requires:       kernel-devel redhat-rpm-config rpm-build
Requires:       mock
%endif

%description -n %{name}
Ddiskit is a little framework for simplifying creation of proper
Driver Update Disks (DUD) used for providing new or updated out-of-tree
kernel modules.

%prep
%autosetup -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
find %{buildroot} -size 0 -delete

%check
%{__python} setup.py test

%files -n %{name}
%defattr(-,root,root,-)
%doc README
%license COPYING
%{python_sitelib}/*
%{_bindir}/ddiskit
%{_mandir}/man1/ddiskit.1*
%{_datadir}/bash-completion/completions/ddiskit

%dir %{_datadir}/ddiskit
%dir %{_datadir}/ddiskit/keyrings
%dir %{_datadir}/ddiskit/keyrings/rh-release
%dir %{_datadir}/ddiskit/profiles
%dir %{_datadir}/ddiskit/templates
%{_datadir}/ddiskit/templates/spec
%{_datadir}/ddiskit/templates/config
%{_datadir}/ddiskit/profiles/*
%{_datadir}/ddiskit/keyrings/rh-release/*.key
%{_datadir}/ddiskit/ddiskit.config

%config(noreplace) /etc/ddiskit.config

%changelog
* Mon Jun 26 2017 Petr Oros <poros@redhat.com> - 3.5-1
- New upstream release

* Thu Jun 22 2017 Petr Oros <poros@redhat.com> - 3.4-1
- New upstream release

* Mon Apr 24 2017 Petr Oros <poros@redhat.com> - 3.3-1
- New upstream release

* Tue Mar 14 2017 Petr Oros <poros@redhat.com> - 3.2-1
- New upstream release

* Tue Feb 28 2017 Petr Oros <poros@redhat.com> - 3.1-1
- New upstream release

* Mon Feb 13 2017 Petr Oros <poros@redhat.com> - 3.0-2
- Bump version after few important fixes

* Mon Sep 5 2016 Petr Oros <poros@redhat.com> - 3.0-1
- Initial package.

