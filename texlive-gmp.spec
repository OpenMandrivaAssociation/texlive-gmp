%global tl_name gmp
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Enable integration between MetaPost pictures and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmp
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows integration between MetaPost pictures and LaTeX. The
main feature is that passing parameters to the MetaPost pictures is
possible and the picture code can be put inside arguments to commands,
including \newcommand.

