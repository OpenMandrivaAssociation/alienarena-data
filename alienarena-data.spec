#Based on Fedora's package
Name:		alienarena-data
Summary:	Data files for Alien Arena 2011
Version:	20120106
Release:	3
License:	Redistributable, no modification permitted
Group:		Games/Arcade
URL:		http://icculus.org/alienarena/
# Subversion:  https://svn.icculus.org/alienarena/trunk/?sortby=date
# Upstream seems too inept to provide a simple source only tarball, so we use svn.
#   svn export svn://svn.icculus.org/alienarena/tags/7.51/ alienarena-7.51/
# These windows files are useless to us.
#   rm -rf alienarena-7.51/*.exe alienarena-7.51/*.dll alienarena-7.51/Tools/aaradiant.exe
# These bundled zips are also pretty useless.
#   rm -rf alienarena-7.51/lib_zipfiles/
# We don't want the bundled ode code.
#   rm -rf alienarena-7.51/source/unix/ode/
# arena/ botinfo/ data1/ live in the alienarena-data package
#   mkdir alienarena-data-20101216
#   mv alienarena-7.51/arena/ alienarena-7.51/botinfo/ alienarena-7.51/data1/ alienarena-data-20110323/
#   rm -f alienarena-data-20110323/{arena,data1}/game.so
# This data tarball is used for the alienarena-data package
#   tar -cvJf alienarena-data-20110323.tar.xz alienarena-data-20110323
# This source tarball is used for the alienarena package
#   tar -cvjf alienarena-7.51.tar.bz2 alienarena-7.51
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
Data files (audio, maps, etc) for Alien Arena 2011.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/alienarena/
cp -ap arena botinfo data1 %{buildroot}/%{_datadir}/alienarena/

%files
%{_datadir}/alienarena/


%changelog
* Fri Jan 20 2012 Andrey Bondrov <abondrov@mandriva.org> 20120106-1mdv2011.0
+ Revision: 762928
- New version 20120106

* Mon Oct 17 2011 Andrey Bondrov <abondrov@mandriva.org> 20111014-1
+ Revision: 704987
- New version 20111014 (7.52)

* Wed Apr 27 2011 Juan Luis Baptiste <juancho@mandriva.org> 20110323-1
+ Revision: 659564
- Added missing BuildRoot
- Added missing clean build root on %%install and %%clean.
- Fixed group.
- import alienarena-data

