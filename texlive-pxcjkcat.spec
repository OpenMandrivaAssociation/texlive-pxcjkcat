# revision 27780
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pxcjkcat
Version:	20131019
Release:	5
Summary:	TeXLive pxcjkcat package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxcjkcat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxcjkcat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pxcjkcat package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pxcjkcat/pxcjkcat.sty
%doc %{_texmfdistdir}/doc/latex/pxcjkcat/LICENSE
%doc %{_texmfdistdir}/doc/latex/pxcjkcat/README
%doc %{_texmfdistdir}/doc/latex/pxcjkcat/README-ja

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
