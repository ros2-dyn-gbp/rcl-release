%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rcl
Version:        6.0.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rcl package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       libyaml-devel
Requires:       ros-iron-libyaml-vendor
Requires:       ros-iron-rcl-interfaces
Requires:       ros-iron-rcl-logging-interface
Requires:       ros-iron-rcl-logging-spdlog
Requires:       ros-iron-rcl-yaml-param-parser
Requires:       ros-iron-rcutils
Requires:       ros-iron-rmw
Requires:       ros-iron-rmw-implementation
Requires:       ros-iron-rosidl-runtime-c
Requires:       ros-iron-service-msgs
Requires:       ros-iron-tracetools
Requires:       ros-iron-type-description-interfaces
Requires:       ros-iron-ros-workspace
BuildRequires:  libyaml-devel
BuildRequires:  ros-iron-ament-cmake-ros
BuildRequires:  ros-iron-libyaml-vendor
BuildRequires:  ros-iron-rcl-interfaces
BuildRequires:  ros-iron-rcl-logging-interface
BuildRequires:  ros-iron-rcl-logging-spdlog
BuildRequires:  ros-iron-rcl-yaml-param-parser
BuildRequires:  ros-iron-rcutils
BuildRequires:  ros-iron-rmw-implementation
BuildRequires:  ros-iron-rosidl-runtime-c
BuildRequires:  ros-iron-service-msgs
BuildRequires:  ros-iron-tracetools
BuildRequires:  ros-iron-type-description-interfaces
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
BuildRequires:  ros-iron-launch
BuildRequires:  ros-iron-launch-testing
BuildRequires:  ros-iron-launch-testing-ament-cmake
BuildRequires:  ros-iron-mimick-vendor
BuildRequires:  ros-iron-osrf-testing-tools-cpp
BuildRequires:  ros-iron-rcpputils
BuildRequires:  ros-iron-rmw
BuildRequires:  ros-iron-rmw-implementation-cmake
BuildRequires:  ros-iron-test-msgs
%endif

%description
The ROS client library common implementation. This package contains an API which
builds on the ROS middleware API and is optionally built upon by the other ROS
client libraries.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.1-2
- Autogenerated by Bloom

* Tue Apr 18 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.1-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Audrow Nash <audrow@openrobotics.org> - 5.9.0-2
- Autogenerated by Bloom

