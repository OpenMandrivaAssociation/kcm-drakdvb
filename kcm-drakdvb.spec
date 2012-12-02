# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

Name:           kcm-drakdvb
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching drakdvb
Version:        1.0
Release:        3
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
Suggests:       dvbsubs

%description
Drakdvb launcher for KDE Control Center

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%files
%doc
%{_datadir}/kde4/services/kcm_drakdvb.desktop

