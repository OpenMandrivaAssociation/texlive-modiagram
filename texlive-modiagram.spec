Name:		texlive-modiagram
Version:	56886
Release:	2
Summary:	Drawing molecular orbital diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modiagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
