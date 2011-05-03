%define name fonts-type1-greek
%define version 2.0
%define release %mkrel 10

Summary:	Greek Type1 fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}

Url:		http://iris.math.aegean.gr/kerkis/
# date 2003-01-17
Source0:	http://iris.math.aegean.gr/kerkis/Kerkis_for_X11.tar.bz2

License: 	Distributable (Copyright (C) Department of Mathematics, University of Aegean. For use information check http://iris.math.aegean.gr/kerkis/)

Group:		System/Fonts/Type1
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	font-tools

%description
Nice Greek scalable fonts, usable for display on screen or for printing.
Please if you want to use them for publishing, read the
licence at http://iris.math.aegean.gr/kerkis/
or in the doc directory.

%prep

%setup -q -n Kerkis_for_X11 
 
%build

%install
rm -fr %buildroot

install -d %buildroot/%_datadir/fonts/type1/greek/
install -m 0644 *.pfb %buildroot/%_datadir/fonts/type1/greek
install -m 0644 *.afm %buildroot/%_datadir/fonts/type1/greek

cat fonts.scale | \
	sed 's:^\(.*\)-iso8859-7$:\1-iso8859-7#\1-iso10646-1:' | \
	tr '#' '\n' | uniq | grep '[ 	]' > fonts.scale.tmp
wc -l fonts.scale.tmp | awk '{print $1}'> fonts.scale.new
cat fonts.scale.tmp >> fonts.scale.new
install -m 0644 fonts.scale.new \
	%buildroot/%_datadir/fonts/type1/greek/fonts.scale

(
cd %buildroot/%_datadir/fonts/type1/greek
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/type1/greek \
    %{buildroot}%_sysconfdir/X11/fontpath.d/type1-greek:pri=50


%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc License.txt
%dir %_datadir/fonts/type1/greek
%_datadir/fonts/type1/greek/*.pfb
%_datadir/fonts/type1/greek/*.afm
%config(noreplace) %_datadir/fonts/type1/greek/fonts.dir
%config(noreplace) %_datadir/fonts/type1/greek/fonts.scale
%_sysconfdir/X11/fontpath.d/type1-greek:pri=50

