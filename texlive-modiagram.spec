# revision 30169
# category Package
# catalog-ctan /macros/latex/contrib/modiagram
# catalog-date 2013-04-28 23:24:16 +0200
# catalog-license lppl1.3
# catalog-version 0.2c
Name:		texlive-modiagram
Version:	0.2c
Release:	6
Summary:	Drawing molecular orbital diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modiagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment MOdiagram and some
commands, to create molecular orbital diagrams using TikZ. For
example, the MO diagram of dihydrogen would be written as:
\begin{MOdiagram} \atom{left}{ 1s = {0;up} } \atom{right}{ 1s =
{0;up} } \molecule{ 1sMO = {1;pair, } } \end{MOdiagram} The
package also needs the l3kernel and l3packages bundles from the
LaTeX 3 experimental distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/modiagram/modiagram.sty
%doc %{_texmfdistdir}/doc/latex/modiagram/README
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_en.pdf
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
