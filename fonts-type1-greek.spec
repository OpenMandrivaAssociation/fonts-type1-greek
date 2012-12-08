%define name fonts-type1-greek
%define version 2.0
%define release %mkrel 13

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
BuildRequires: fontconfig
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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-12mdv2011.0
+ Revision: 675433
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-11
+ Revision: 675192
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0-10
+ Revision: 664342
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-9mdv2011.0
+ Revision: 605208
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.0-8mdv2010.1
+ Revision: 494124
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.0-7mdv2009.1
+ Revision: 351150
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0-6mdv2009.0
+ Revision: 220958
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2008.1
+ Revision: 150076
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.0-4mdv2008.0
+ Revision: 48748
- fontpath.d conversion (#31756)
- minor cleanups

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 2.0-3mdv2008.0
+ Revision: 18892
- rebuild for new era
- clean spec
- drop hideous live generation of README using lynx (whoever came up with this probably eats kittens)
- bzip2 source


* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0-2mdk
- Fix prereq
- don't package fontconfig cache

* Fri May 14 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 2.0-1mdk
- changed the version number so it is in synch with the kerkis font
  version number, it makes things less misleading.

* Wed Mar 05 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-4mdk
- added *-iso10646-1 lines so the fonts can be used by old programs
  when in el_GR.UTF-8 locale

* Tue Feb 18 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-3mdk
- proper use of fc-cache

