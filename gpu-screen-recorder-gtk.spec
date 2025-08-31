#define git 20240603
#define git2 r602.04db56a
%define date 20250126
%define tag %{version}

Name: gpu-screen-recorder-gtk
Version: 5.7.8
Release: 1
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder-gtk/about/
Group: Video
License: GPL-3.0-only
# Use... git clone --branch 5.1.2 --depth 1 https://repo.dec05eba.com/gpu-screen-recorder-gtk
# for now lets choose tag instead of commit, so use 5.1.2
# then create .xz archive gpu-screen-recorder-gtk-5.1.2.tar.xz
Source0:  gpu-screen-recorder-gtk-%{version}.tar.xz
#Source0: https://dec05eba.com/snapshot/gpu-screen-recorder-gtk.git.%{git2}.tar.gz

BuildSystem: meson
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: vulkan-headers

Requires:	gpu-screen-recorder
Provides:	gpu-screen-recorder-gui

%description
This is a gui written in GTK for screen recorder that has minimal impact on system performance 
by recording your monitor using the GPU only, similar to shadowplay on windows. 
This is the fastest screen recording tool for Linux.
This screen recorder can be used for recording your desktop offline, 
for live streaming and for nvidia shadowplay-like instant replay,
where only the last few minutes are saved.
Supported video codecs:

    H264 (default on Intel)
    HEVC (default on AMD and NVIDIA)
    AV1 (not currently supported on NVIDIA if you use GPU Screen Recorder flatpak)

%files
%{_bindir}/gpu-screen-recorder-gtk
%{_datadir}/applications/com.dec05eba.gpu_screen_recorder.desktop
%{_iconsdir}//hicolor/*x*/apps/
%{_iconsdir}//hicolor/*x*/status/
