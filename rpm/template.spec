Name:           ros-indigo-sr-ronex-controllers
Version:        0.11.0
Release:        0%{?dist}
Summary:        ROS sr_ronex_controllers package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://www.shadowrobot.com/products/ronex
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-controller-manager-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-ros-ethercat-model
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sr-ronex-drivers
Requires:       ros-indigo-sr-ronex-hardware-interface
Requires:       ros-indigo-sr-ronex-msgs
Requires:       ros-indigo-sr-ronex-utilities
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-controller-manager-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-ros-ethercat-model
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sr-ronex-drivers
BuildRequires:  ros-indigo-sr-ronex-hardware-interface
BuildRequires:  ros-indigo-sr-ronex-msgs
BuildRequires:  ros-indigo-sr-ronex-utilities
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

%description
Contains different useful controllers to use with the RoNeX.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 20 2015 Shadow Robot's software team <software@shadowrobot.com> - 0.11.0-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Shadow Robot's software team <software@shadowrobot.com> - 0.10.0-0
- Autogenerated by Bloom

