Summary:	Greek Type1 fonts
Name:		fonts-type1-greek
Version:	2.0
Release:	2mdk

Url:		http://iris.math.aegean.gr/kerkis/
# date 2003-01-17
Source0:	http://iris.math.aegean.gr/kerkis/Kerkis_for_X11.zip

License: distributable (Copyright (C) Department of Mathematics, Univeristy of Aegean. For use information check http://iris.math.aegean.gr/kerkis/)

Group:		System/Fonts/Type1
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	font-tools, lynx
Requires(post):	chkfontpath
Requires(postun):chkfontpath
Requires(post):	fontconfig
Requires(postun):fontconfig

%description
Nice Greek scalable fonts, usable for display on screen or for printing.
Please if you want to use them for publishing, read the
licence at http://iris.math.aegean.gr/kerkis/
or in the doc directory.

%prep

%setup -q -n Kerkis_for_X11 
 
%build

if [ ! -r README ] ; then
	echo -e "\nThis is a dump of the web page at" > README
	echo -e "%{url}\n\n" >> README
	lynx -dump "%{url}" >> README
fi

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

%post
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/fonts/type1/greek
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_sbindir/chkfontpath ] && \
   %_sbindir/chkfontpath -q -r %_datadir/fonts/type1/greek
   [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc README License.txt
%dir %_datadir/fonts/type1/greek
%_datadir/fonts/type1/greek/*.pfb
%_datadir/fonts/type1/greek/*.afm
%config(noreplace) %_datadir/fonts/type1/greek/fonts.dir
%config(noreplace) %_datadir/fonts/type1/greek/fonts.scale

