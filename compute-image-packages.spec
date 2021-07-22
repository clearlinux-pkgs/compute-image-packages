#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compute-image-packages
Version  : 20191210
Release  : 42
URL      : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/v20191210/compute-image-packages-20191210.tar.gz
Source0  : https://github.com/GoogleCloudPlatform/compute-image-packages/archive/v20191210/compute-image-packages-20191210.tar.gz
Source1  : google-accounts-daemon.service
Source2  : google-clock-skew-daemon.service
Source3  : google-instance-setup.service
Source4  : google-network-daemon.service
Source5  : google-shutdown-scripts.service
Source6  : google-startup-scripts.service
Summary  : Google Compute Engine python3 library
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
BuildRequires : setuptools

%description
Google Compute Engine python library for Python 3.x.

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
%setup -q -n compute-image-packages-20191210
cd %{_builddir}/compute-image-packages-20191210

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582912369
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pushd packages/python-google-compute-engine
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compute-image-packages
cp %{_builddir}/compute-image-packages-20191210/LICENSE %{buildroot}/usr/share/package-licenses/compute-image-packages/9c6aa5b2c229294d34c2537b86e453a25a38cfd2
cp %{_builddir}/compute-image-packages-20191210/packages/gce-disk-expand/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/2c41b55fcea2a6917d5e0b27d775847982c24447
cp %{_builddir}/compute-image-packages-20191210/packages/google-compute-engine/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/compute-image-packages/17949f727e27611ec2f3d6f56523b45535d71ad5
cp %{_builddir}/compute-image-packages-20191210/packages/python-google-compute-engine/LICENSE %{buildroot}/usr/share/package-licenses/compute-image-packages/9c6aa5b2c229294d34c2537b86e453a25a38cfd2
pushd packages/python-google-compute-engine
python3 -tt setup.py build  install --root=%{buildroot}
popd
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/google-accounts-daemon.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/google-clock-skew-daemon.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/google-instance-setup.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/google-network-daemon.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/google-shutdown-scripts.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/google-startup-scripts.service
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../google-accounts-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
ln -s ../google-clock-skew-daemon.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
ln -s ../google-shutdown-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
ln -s ../google-startup-scripts.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
/usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
/usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
/usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service

%files bin
%defattr(-,root,root,-)
/usr/bin/google_accounts_daemon
/usr/bin/google_clock_skew_daemon
/usr/bin/google_instance_setup
/usr/bin/google_metadata_script_runner
/usr/bin/google_network_daemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compute-image-packages/17949f727e27611ec2f3d6f56523b45535d71ad5
/usr/share/package-licenses/compute-image-packages/2c41b55fcea2a6917d5e0b27d775847982c24447
/usr/share/package-licenses/compute-image-packages/9c6aa5b2c229294d34c2537b86e453a25a38cfd2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-accounts-daemon.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-clock-skew-daemon.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-shutdown-scripts.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/google-startup-scripts.service
/usr/lib/systemd/system/google-accounts-daemon.service
/usr/lib/systemd/system/google-clock-skew-daemon.service
/usr/lib/systemd/system/google-instance-setup.service
/usr/lib/systemd/system/google-network-daemon.service
/usr/lib/systemd/system/google-shutdown-scripts.service
/usr/lib/systemd/system/google-startup-scripts.service
