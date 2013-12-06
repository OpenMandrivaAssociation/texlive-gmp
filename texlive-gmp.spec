# revision 21691
# category Package
# catalog-ctan /macros/latex/contrib/gmp
# catalog-date 2011-03-11 00:02:27 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-gmp
Version:	1.0
Release:	5
Summary:	Allow integration between MetaPost pictures and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmp
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmp.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752362
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718566
- texlive-gmp
- texlive-gmp
- texlive-gmp
- texlive-gmp

