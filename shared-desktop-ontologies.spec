Summary:    Semantic web to the desktop in terms of vocabulary
Name:	  	shared-desktop-ontologies
Version:	0.7.52
Release:	2
License:	BSD
Group:		System/Base 
Source0: 	%name-%version.tar.bz2
URL:		http://sourceforge.net/projects/oscaf/
BuildRequires: kde4-macros
BuildArch:     noarch

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
%_kde_datadir/ontology

#--------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %name

%description  devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%_kde_datadir/pkgconfig/shared-desktop-ontologies.pc
%_kde_datadir/cmake/SharedDesktopOntologies

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name
