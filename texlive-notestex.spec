%global tl_name notestex
%global tl_revision 45396

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	An all-in-one LaTeX notes package for students
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/notestex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notestex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notestex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a modification of the original Jhep journal format in order to
suit the needs of students in university. The goal of this package was
to make notetaking easier for students and offer easy support for
marginnotes along with a reliable and legible formatting structure.

