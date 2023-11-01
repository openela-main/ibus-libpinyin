%global snapshot 0

Name:       ibus-libpinyin
Version:    1.12.0
Release:    5%{?dist}
Summary:    Intelligent Pinyin engine based on libpinyin for IBus
License:    GPLv3+
URL:        https://github.com/libpinyin/ibus-libpinyin
Source0:    http://downloads.sourceforge.net/libpinyin/ibus-libpinyin/%{name}-%{version}.tar.gz
%if %snapshot
Patch0:     ibus-libpinyin-1.12.x-head.patch
%endif

Requires:       python3-gobject
Requires:       ibus >= 1.5.11
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  lua-devel
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ibus-devel >= 1.5.11
BuildRequires:  libpinyin-devel >= 2.1.0
BuildRequires: make

# Requires(post): sqlite

Requires:   libpinyin-data%{?_isa} >= 1.5.91

Obsoletes: ibus-pinyin < 1.4.0-17

%description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) 
input method based on libpinyin for IBus.

%prep
%setup -q
%if %snapshot
%patch0 -p1 -b .head
%endif

%build
%configure --disable-static \
           --with-python=python3 \
           --disable-boost

# make -C po update-gmo
%make_build

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-libpinyin.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-libbopomofo.desktop

%install
%make_install

%py_byte_compile %{python3} $RPM_BUILD_ROOT%{_datadir}/ibus-libpinyin/setup

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/applications/ibus-setup-libpinyin.desktop
%{_datadir}/applications/ibus-setup-libbopomofo.desktop
%{_libexecdir}/ibus-engine-libpinyin
%{_libexecdir}/ibus-setup-libpinyin
%{_datadir}/ibus-libpinyin/icons
%{_datadir}/ibus-libpinyin/setup
%{_datadir}/ibus-libpinyin/base.lua
%{_datadir}/ibus-libpinyin/user.lua
%{_datadir}/ibus-libpinyin/network.txt
%{_datadir}/ibus-libpinyin/db/english.db
%{_datadir}/ibus-libpinyin/db/strokes.db
%dir %{_datadir}/ibus-libpinyin
%dir %{_datadir}/ibus-libpinyin/db
%{_datadir}/ibus/component/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.12.0-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 19 2021 Peng Wu <pwu@redhat.com> - 1.12.0-4
- Clean up ibus write-cache in scriptlet
- Resolves: #1974629

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.12.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Peng Wu <pwu@redhat.com> - 1.12.0-1
- Update to 1.12.0
- bug fixes

* Thu Oct 22 2020 Peng Wu <pwu@redhat.com> - 1.11.94-1
- Update to 1.11.94
- bug fixes

* Mon Oct 12 2020 Peng Wu <pwu@redhat.com> - 1.11.93-3
- Fixes python3-gobject warning in setup dialog

* Sun Sep 27 2020 Peng Wu <pwu@redhat.com> - 1.11.93-2
- Fixes Shift key switch issue

* Wed Aug 26 2020 Peng Wu <pwu@redhat.com> - 1.11.93-1
- Update to 1.11.93
- switch to use GPLv3+ license
- support network dictionary
- bug fixes

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.11.92-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Jul 13 2020 Peng Wu <pwu@redhat.com> - 1.11.92-2
- Switch to use py_byte_compile rpm macro

* Thu Mar 19 2020 Peng Wu <pwu@redhat.com> - 1.11.92-1
- Update to 1.11.92
- fixes desktop files

* Thu Mar 19 2020 Peng Wu <pwu@redhat.com> - 1.11.91-1
- Update to 1.11.91
- support compact display style
- bug fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Peng Wu <pwu@redhat.com> - 1.11.1-1
- Update to 1.11.1
- use gettext
- add emoji-candidate option
- fixes SuggestionEditor

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Peng Wu <pwu@redhat.com> - 1.11.0-1
- Update to 1.11.0
- fixes keypad decimal
- fixes emoji candidates
- support configurable opencc config

* Wed Oct 31 2018 Peng Wu <pwu@redhat.com> - 1.10.92-1
- Update to 1.10.92
- fixes Enter handling

* Thu Oct 11 2018 Peng Wu <pwu@redhat.com> - 1.10.91-1
- Update to 1.10.91
- support ime.register_trigger in lua extension
- support predicted candidates
- support emoji input

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Peng Wu <pwu@redhat.com> - 1.10.0-1
- Update to 1.10.0
- bug fixes

* Thu Mar 22 2018 Peng Wu <pwu@redhat.com> - 1.9.91-1
- Update to 1.9.91
- migrate to use GSettings

* Thu Feb  8 2018 Peng Wu <pwu@redhat.com> - 1.9.3-1
- Update to 1.9.3
- translate input method name in ibus menu

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep  4 2017 Peng Wu <pwu@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Mon Aug 28 2017 Peng Wu <pwu@redhat.com> - 1.9.1-2
- Fixes pinyin and bopomofo config

* Thu Aug 24 2017 Peng Wu <pwu@redhat.com> - 1.9.1-1
- Update to 1.9.1
- add sort candidate option to setup dialog

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Peng Wu <pwu@redhat.com> - 1.9.0-2
- Rebuilt for libpinyin 2.0.91

* Thu Apr 20 2017 Peng Wu <pwu@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Tue Mar  7 2017 Peng Wu <pwu@redhat.com> - 1.8.92-1
- Update to 1.8.92
- fixes config

* Tue Feb 28 2017 Peng Wu <pwu@redhat.com> - 1.8.91-2
- Fixes config in setup dialog

* Wed Feb 15 2017 Peng Wu <pwu@redhat.com> - 1.8.91-1
- Update to 1.8.91
- use libpinyin 1.9.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Peng Wu <pwu@redhat.com> - 1.8.1-1
- Update to 1.8.1
- change dconf key name to lower case

* Tue Nov  1 2016 Peng Wu <pwu@redhat.com> - 1.8.0-2
- Rebuilt for libpinyin 1.6.91

* Wed Sep  7 2016 Peng Wu <pwu@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Tue Aug  9 2016 Peng Wu <pwu@redhat.com> - 1.7.92-2
- Fixes crashes for Full Pinyin and Bopomofo

* Tue Aug  2 2016 Peng Wu <pwu@redhat.com> - 1.7.92-1
- Update to 1.7.92

* Mon Jul 18 2016 Peng Wu <pwu@redhat.com> - 1.7.91-1
- Update to 1.7.91

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Peng Wu <pwu@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Mon Dec 14 2015 Peng Wu <pwu@redhat.com> - 1.7.3-3
- Update patch

* Mon Dec 14 2015 Peng Wu <pwu@redhat.com> - 1.7.3-2
- Fixes crash when use "Bopomofo" engine for first time

* Tue Nov 17 2015 Peng Wu <pwu@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul  8 2015 Peng Wu <pwu@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 1.7.1-2
- Register as an AppStream component.

* Wed Mar 25 2015 Peng Wu <pwu@redhat.com> - 1.7.1-1
- Update 1.7.1

* Mon Mar  9 2015 Peng Wu <pwu@redhat.com> - 1.7.0-2
- Fixes ibus-libpinyin upstream issue #33

* Wed Mar  4 2015 Peng Wu <pwu@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Thu Feb 12 2015 Peng Wu <pwu@redhat.com> - 1.6.99.20150203-2
- Disable opencc according to upstream issue #26

* Tue Feb  3 2015 Peng Wu <pwu@redhat.com> - 1.6.99.20150203-1
- Update to 1.6.99.20150203

* Wed Jan  7 2015 Peng Wu <pwu@redhat.com> - 1.6.92-5
- Use opencc 1.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Peng Wu <pwu@redhat.com> - 1.6.92-2
- Fixes click of ibus-libpinyin indicator menu. (rhbz#1028905)

* Thu Oct 24 2013 Peng Wu <pwu@redhat.com> - 1.6.92-1
- Update to 1.6.92

* Mon Oct 14 2013 Peng Wu <pwu@redhat.com> - 1.6.91-5
- Update ibus-libpinyin-1.7.x-head.patch
- Support ibus input purpose feature, fixes bug 1016438.
- Remove pyxdg depends, fixes bug 1016941.

* Tue Oct  8 2013 Peng Wu <pwu@redhat.com> - 1.6.91-4
- Write ibus system cache when install or uninstall

* Wed Jul 31 2013 Peng Wu <pwu@redhat.com> - 1.6.91-3
- Fixes lua 5.2 compile

* Tue Jul 30 2013 Peng Wu <pwu@redhat.com> - 1.6.91-2
- Update the symbol of the ibus indicator

* Sun Apr 28 2013 Peng Wu <pwu@redhat.com> - 1.6.91-1
- Update to 1.6.91

* Tue Mar 19 2013 Peng Wu <pwu@redhat.com> - 1.5.92-1
- Update to 1.5.92

* Mon Mar  4 2013 Peng Wu <pwu@redhat.com> - 1.5.91-1
- Update to 1.5.91

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012  Peng Wu <pwu@redhat.com> - 1.4.93-4
- Fixes symbol icons

* Tue Nov 20 2012  Peng Wu <pwu@redhat.com> - 1.4.93-3
- Fixes spec file

* Mon Oct 29 2012  Peng Wu <pwu@redhat.com> - 1.4.93-2
- Fixes libpinyin Requires

* Mon Oct 15 2012  Peng Wu <pwu@redhat.com> - 1.4.93-1
- Update to 1.4.93

* Mon Sep 17 2012  Peng Wu <pwu@redhat.com> - 1.4.92-1
- Update to 1.4.92

* Thu Aug 16 2012  Peng Wu <pwu@redhat.com> - 1.4.91-1
- Update to 1.4.91

* Mon Aug 06 2012  Peng Wu <pwu@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012  Peng Wu <pwu@redhat.com> - 1.4.1-4
- Fixes obsoletes

* Wed Jul 11 2012  Peng Wu <pwu@redhat.com> - 1.4.1-3
- Update ibus-libpinyin-1.4.x-head.patch

* Tue Jul 10 2012  Peng Wu <pwu@redhat.com> - 1.4.1-2
- Update ibus-libpinyin-1.4.x-head.patch

* Wed Jul 04 2012  Peng Wu <pwu@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Jun 01 2012  Peng Wu <pwu@redhat.com> - 1.4.0-1
- The first version.
