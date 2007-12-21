%define name	peksystray
%define version	0.4.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Small system tray requiring only X
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://peksystray.sourceforge.net/
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel

%description
Peksystray is a small system tray (also called notification tray) designed for
all the light window managers supporting docking. As more and more
applications use a small icon in the system tray to provide additonal
fonctionalities and information, it becomes useful for everyone to have
access to them. While "heavy" window managers (Gnome, KDE...) come with a
systrem tray embedded in the rest of the desktop, lighter window managers
(WindowMaker, fluxbox...) don't have this feature. Peksystray is a very simple
and light implementation of a system tray for any window manager supporting
docking, conforming to the System Tray Freedesktop standard.

Peksystray provides a window where icons will automatically add up depending
on the requests from the applications. Both the size of the window and the
size of the icons can be selected by the user. If the window is full, it can
automatically display another window in order to display more icons.

%prep
%setup -q

%build
%configure2_5x
make peksystray_LDADD=""
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog THANKS REFS README NEWS TODO
%{_bindir}/%name
