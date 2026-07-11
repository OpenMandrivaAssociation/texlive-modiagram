%global tl_name modiagram
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3a
Release:	%{tl_revision}.1
Summary:	Drawing molecular orbital diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modiagram
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modiagram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment MOdiagram and some commands, to
create molecular orbital diagrams using TikZ. For example, the MO
diagram of dihydrogen would be written as: \begin{MOdiagram}
\atom{left}{ 1s = {0;up} } \atom{right}{ 1s = {0;up} } \molecule{ 1sMO =
{1;pair, } } \end{MOdiagram} The package also needs the l3kernel and
l3packages bundles from the LaTeX 3 experimental distribution.

