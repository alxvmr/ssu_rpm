Name:    my-hello
Version: 0.0.1
Release: alt1

Summary: Test package
License: GPLv3
Group:   Other
Url:     https://github.com/alxvmr/ssu_rpm/example

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ pkgconfig(glib-2.0)

Source0: %name-%version.tar

%description
This is a test package that outputs "Hello world!" to the console

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/my_hello

%changelog
* Tue Mar 11 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Init build

