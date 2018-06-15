#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compute-image-packages
Version  : 20170921
Release  : 17
URL      : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/20170921.tar.gz
Source0  : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/20170921.tar.gz
Source1  : google-accounts-daemon.service
Source2  : google-clock-skew-daemon.service
Source3  : google-instance-setup.service
Source4  : google-ip-forwarding-daemon.service
Source5  : google-network-setup.service
Source6  : google-shutdown-scripts.service
Source7  : google-startup-scripts.service
Summary  : Google Compute Engine python library
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: compute-image-packages-bin
Requires: compute-image-packages-python3
Requires: compute-image-packages-config
Requires: compute-image-packages-autostart
Requires: compute-image-packages-python
Requires: boto
Requires: setuptools
BuildRequires : boto
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Google Compute Engine python library for Python 2.x.

%package autostart
Summary: autostart components for the compute-image-packages package.
Group: Default

%description autostart
autostart components for the compute-image-packages package.


%package bin
Summary: bin components for the compute-image-packages package.
Group: Binaries
Requires: compute-image-packages-config

%description bin
bin components for the compute-image-packages package.


%package config
Summary: config components for the compute-image-packages package.
Group: Default

%description config
config components for the compute-image-packages package.


%package python
Summary: python components for the compute-image-packages package.
Group: Default
Requires: compute-image-packages-python3

%description python
python components for the compute-image-packages package.


%package python3
Summary: python3 components for the compute-image-packages package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compute-image-packages package.


%prep
%setup -q -n compute-image-packages-20170921

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523287134
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/google-accounts-daemon.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/google-clock-skew-daemon.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/google-instance-setup.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/google-ip-forwarding-daemon.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/google-network-setup.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/google-shutdown-scripts.service
install -m 0644 %{SOURCE7} %{buildroot}/usr/lib/systemd/system/google-startup-scripts.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s /usr/lib/systemd/system/google-accounts-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
ln -s /usr/lib/systemd/system/google-clock-skew-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
ln -s /usr/lib/systemd/system/google-google-ip-forwarding-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-ip-forwarding-daemon.service
ln -s /usr/lib/systemd/system/google-startup-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service
ln -s /usr/lib/systemd/system/google-shutdown-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
/usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
/usr/lib/systemd/system/multi-user.target.wants/google-ip-forwarding-daemon.service
/usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
/usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service

%files bin
%defattr(-,root,root,-)
/usr/bin/google_accounts_daemon
/usr/bin/google_clock_skew_daemon
/usr/bin/google_instance_setup
/usr/bin/google_ip_forwarding_daemon
/usr/bin/google_metadata_script_runner
/usr/bin/google_network_setup
/usr/bin/optimize_local_ssd
/usr/bin/set_multiqueue

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-ip-forwarding-daemon.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service
/usr/lib/systemd/system/google-accounts-daemon.service
/usr/lib/systemd/system/google-clock-skew-daemon.service
/usr/lib/systemd/system/google-instance-setup.service
/usr/lib/systemd/system/google-ip-forwarding-daemon.service
/usr/lib/systemd/system/google-network-setup.service
/usr/lib/systemd/system/google-shutdown-scripts.service
/usr/lib/systemd/system/google-startup-scripts.service

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
