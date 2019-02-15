#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compute-image-packages
Version  : 20190124
Release  : 26
URL      : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/20190124.tar.gz
Source0  : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/20190124.tar.gz
Source1  : google-accounts-daemon.service
Source2  : google-clock-skew-daemon.service
Source3  : google-instance-setup.service
Source4  : google-ip-forwarding-daemon.service
Source5  : google-network-setup.service
Source6  : google-shutdown-scripts.service
Source7  : google-startup-scripts.service
Summary  : Google Compute Engine python library
Group    : Development/Tools
License  : Apache-2.0
Requires: compute-image-packages-autostart = %{version}-%{release}
Requires: compute-image-packages-bin = %{version}-%{release}
Requires: compute-image-packages-license = %{version}-%{release}
Requires: compute-image-packages-python = %{version}-%{release}
Requires: compute-image-packages-python3 = %{version}-%{release}
Requires: compute-image-packages-services = %{version}-%{release}
Requires: boto
Requires: distro
Requires: setuptools
BuildRequires : boto
BuildRequires : buildreq-distutils3
BuildRequires : distro
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
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
Requires: compute-image-packages-license = %{version}-%{release}
Requires: compute-image-packages-services = %{version}-%{release}

%description bin
bin components for the compute-image-packages package.


%package license
Summary: license components for the compute-image-packages package.
Group: Default

%description license
license components for the compute-image-packages package.


%package python
Summary: python components for the compute-image-packages package.
Group: Default
Requires: compute-image-packages-python3 = %{version}-%{release}

%description python
python components for the compute-image-packages package.


%package python3
Summary: python3 components for the compute-image-packages package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compute-image-packages package.


%package services
Summary: services components for the compute-image-packages package.
Group: Systemd services

%description services
services components for the compute-image-packages package.


%prep
%setup -q -n compute-image-packages-20190124

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550193427
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compute-image-packages
cp LICENSE %{buildroot}/usr/share/package-licenses/compute-image-packages/LICENSE
cp debian/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/debian_copyright
cp gce-disk-expand/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/gce-disk-expand_packaging_debian_copyright
cp google_compute_engine_oslogin/packaging/debian10/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian10_copyright
cp google_compute_engine_oslogin/packaging/debian8/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian8_copyright
cp google_compute_engine_oslogin/packaging/debian9/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian9_copyright
python3 -tt setup.py build  install --root=%{buildroot}
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
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s /usr/lib/systemd/system/google-accounts-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
ln -s /usr/lib/systemd/system/google-clock-skew-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
ln -s /usr/lib/systemd/system/google-google-ip-forwarding-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-ip-forwarding-daemon.service
ln -s /usr/lib/systemd/system/google-startup-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service
ln -s /usr/lib/systemd/system/google-shutdown-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
## install_append end

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
/usr/bin/google_metadata_script_runner
/usr/bin/google_network_daemon
/usr/bin/google_optimize_local_ssd
/usr/bin/google_set_multiqueue

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compute-image-packages/LICENSE
/usr/share/package-licenses/compute-image-packages/debian_copyright
/usr/share/package-licenses/compute-image-packages/gce-disk-expand_packaging_debian_copyright
/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian10_copyright
/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian8_copyright
/usr/share/package-licenses/compute-image-packages/google_compute_engine_oslogin_packaging_debian9_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
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
