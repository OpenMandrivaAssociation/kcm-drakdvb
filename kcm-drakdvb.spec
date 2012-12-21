%define _kde_services %{_datadir}/kde4/services

Name:           kcm-drakdvb
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching drakdvb
Version:        1.0
Release:        4
BuildArch:      noarch
Source0:        kcm_drakdvb.desktop
Suggests:       dvbsubs

%description
Drakdvb launcher for KDE Control Center

%prep

%build

%install
mkdir -p %{buildroot}%{_kde_services}
install -m 644 %{SOURCE0} %{buildroot}%{_kde_services}/

%files
%doc
%{_kde_services}/kcm_drakdvb.desktop

