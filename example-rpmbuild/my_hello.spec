Name:    my-hello
Version: 0.0.1
Release: alt1

Summary: Test package
License: GPLv3
Group:   Other
Url:     https://github.com/alxvmr/ssu_rpm/example

BuildRequires: gcc-c++ pkgconfig(glib-2.0)

Source0: %name-%version.tar

%description
This is a test package that outputs "Hello world!" to the console

%prep
%setup

%build
gcc main.c -o my_hello \
-I/usr/include/glib-2.0 \
-I/usr/lib64/glib-2.0/include \
-I/usr/include/pcre \
-lglib-2.0

%install
mkdir -p %buildroot%_bindir/
cp my_hello %buildroot%_bindir/my_hello

%files
%_bindir/my_hello

%changelog
* Tue Mar 11 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- Init build

