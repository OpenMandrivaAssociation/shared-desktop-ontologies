Name:		shared-desktop-ontologies
Version:	0.10.0
Release:	1
Summary:	Semantic web to the desktop in terms of vocabulary
Group:		System/Base
License:	BSD
URL:		http://sourceforge.net/projects/oscaf/
Source0:	http://sourceforge.net/projects/oscaf/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
Open Semantic Collaboration Architecture Foundation (OSCAF) ontologies 
and reference code development. This project is used maintainers from 
open source projects to maintain standards for the interoperability 
of desktop and web applications.

The shared-desktop-ontologies package brings the semantic web to the desktop
in terms of vocabulary. It contains the well known core ontologies such as RDF
and RDFS as well as the Nepomuk ontologies which are used by projects like KDE
or Strigi.

%files
%{_kde_datadir}/ontology

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{name}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_datadir}/pkgconfig/shared-desktop-ontologies.pc
%{_kde_datadir}/cmake/SharedDesktopOntologies

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.10.0-1
- Add source url

* Mon Jun 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.0-1
+ Revision: 682936
- New version 0.7.0

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-3
+ Revision: 669977
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-2mdv2011.0
+ Revision: 607536
- rebuild

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5-1mdv2010.1
+ Revision: 544268
- New version 0.5

* Sat Jan 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2-1mdv2010.1
+ Revision: 487927
- Add build fix from Luc menut
- New version

* Wed Dec 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-2mdv2010.1
+ Revision: 472731
- Fix requires on the devel package
- Fix licence

* Thu Nov 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-1mdv2010.1
+ Revision: 470275
- import shared-desktop-ontologies


