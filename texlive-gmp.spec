Name:		texlive-gmp
Version:	21691
Release:	2
Summary:	Allow integration between MetaPost pictures and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows integration between MetaPost pictures and
LaTeX. The main feature is that passing parameters to the
MetaPost pictures is possible and the picture code can be put
inside arguments to commands, including \newcommand.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmp/gmp.sty
%doc %{_texmfdistdir}/doc/latex/gmp/README
%doc %{_texmfdistdir}/doc/latex/gmp/gmp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gmp/gmp.dtx
%doc %{_texmfdistdir}/source/latex/gmp/gmp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
