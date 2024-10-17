Name:		texlive-notestex
Version:	45396
Release:	2
Summary:	An all-in-one LaTeX notes package for students
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/notestex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notestex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notestex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a modification of the original Jhep journal format in
order to suit the needs of students in university. The goal of
this package was to make notetaking easier for students and
offer easy support for marginnotes along with a reliable and
legible formatting structure.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/notestex
%doc %{_texmfdistdir}/doc/latex/notestex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
