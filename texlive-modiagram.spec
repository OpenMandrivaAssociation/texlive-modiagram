# revision 24427
# category Package
# catalog-ctan /macros/latex/contrib/modiagram
# catalog-date 2011-10-28 19:27:59 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-modiagram
Version:	0.2
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides an environment MOdiagram and some
commands, to create molecular orbital diagrams using TikZ. For
example, the MO diagram of dihydrogen would be written as:
\begin{MOdiagram} \atom{left}{ 1s = {0;up} } \atom{right}{ 1s =
{0;up} } \molecule{ 1sMO = {1;pair, } } \end{MOdiagram} The
package also needs the l3kernel and l3packages bundles from the
LaTeX 3 experimental distribution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/modiagram/modiagram.sty
%doc %{_texmfdistdir}/doc/latex/modiagram/README
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_doc_de.pdf
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_doc_de.tex
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/modiagram/modiagram_doc_en.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
