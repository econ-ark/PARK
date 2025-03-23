%%
%% This is file `cfpbpresentation.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% cfpbpresentation.dtx  (with options: `class')
%% 
%% IMPORTANT NOTICE:
%% 
%% For the copyright see the source file.
%% 
%% Any modified versions of this file must be renamed
%% with new filenames distinct from cfpbpresentation.cls.
%% 
%% For distribution of the original source see the terms
%% for copying and modification in the file cfpbpresentation.dtx.
%% 
%% This generated file may be distributed as long as the
%% original source files, as listed above, are part of the
%% same distribution. (The sources need not necessarily be
%% in the same archive or directory.)
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cfpbpresentation}
[2015/05/04 v1.02 CFPB Beamer class]
\newif\if@CFPB@confidential
\@CFPB@confidentialtrue
\DeclareOption{public}{\@CFPB@confidentialfalse}
\DeclareOption{confidential}{\@CFPB@confidentialtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions\relax
\LoadClass[t]{beamer}
\newif\if@CFPB@useTTF
\@CFPB@useTTFfalse
\RequirePackage{ifxetex}
\RequirePackage{optional}
\ifxetex\@CFPB@useTTFtrue\fi
\RequirePackage{ifluatex}
\ifluatex\@CFPB@useTTFtrue\fi
\ifx\HCode\UnDef
  \if@CFPB@useTTF
    \RequirePackage{fontspec}
    \setsansfont{arial.ttf}[
      Ligatures = TeX,
      BoldFont = arialbd.ttf,
      ItalicFont = ariali.ttf,
      BoldItalicFont = arialbi.ttf
    ]
    \setmainfont{arial.ttf}[
      Ligatures = TeX,
      BoldFont = arialbd.ttf,
      ItalicFont = ariali.ttf,
      BoldItalicFont = arialbi.ttf
    ]
  \else
    \RequirePackage[scaled=1.04]{helvet}% sans serif
    \renewcommand\rmdefault{phv}%
    \usepackage{arevmath}%
  \fi
\fi
\RequirePackage{microtype}
\setbeamertemplate{sidebar left}
{
\vfill
\hspace{.15in}\insertlogo\vskip0.15in%
}

\setbeamertemplate{sidebar right}
{
  \vfill%
  \llap{\if@CFPB@confidential\footnotesize\color{CFPBGreen}%
    Sensitive and Pre-Decisional.  Not For Public Disclosure\fi\hskip0.2in}%
  \vskip.21in%
}
\logo{\href{http://www.consumerfinance.gov/}{\includegraphics[height=0.2in]{CFPBLogo}}}
\setbeamertemplate{itemize item}{\tiny\raise1.7pt\hbox{\donotcoloroutermaths$\blacksquare$}}
\setbeamertemplate{itemize subitem}{\tiny\raise1.5pt\hbox{\donotcoloroutermaths$\square$}}
\setbeamertemplate{itemize subsubitem}{\tiny\raise1.5pt\hbox{\donotcoloroutermaths$-$}}
\setbeamertemplate{title page}
{
  \vbox{}
  \vfill
  \begingroup
  \raggedright
    \begin{beamercolorbox}{title}
      \usebeamerfont{title}\inserttitle\par%
      \ifx\insertsubtitle\@empty%
      \else%
        \vskip0.25em%
        {\usebeamerfont{subtitle}\usebeamercolor[fg]{subtitle}\insertsubtitle\par}%
      \fi%
    \end{beamercolorbox}%
    \vskip2em\par
    \begin{beamercolorbox}{author}
      \usebeamerfont{author}\insertauthor
    \end{beamercolorbox}
    \begin{beamercolorbox}{institute}
      \usebeamerfont{institute}\insertinstitute
    \end{beamercolorbox}
    \begin{beamercolorbox}{date}
      \usebeamerfont{date}\insertdate
    \end{beamercolorbox}\vskip0.5em
    {\usebeamercolor[fg]{titlegraphic}\inserttitlegraphic\par}
  \endgroup
  \vfill
}
\setbeamersize{text margin left=.15in}
\setbeamersize{text margin right=.15in}
\setbeamertemplate{frametitle}{%
    \vspace{.15in}%
    \insertframetitle
}
\definecolor{CFPBGreen}{cmyk}{.77, 0, 1, 0}
\definecolor{CFPBGreenMidtone}{cmyk}{.32,0,.52,0}
\definecolor{CFPBGreenTint}{cmyk}{.14,0,.20,0}
\setbeamercolor{structure}{fg=CFPBGreen}
\def\SetPublic{\@CFPB@confidentialfalse}
\def\SetConfidential{\@CFPB@confidentialtrue}
\normalsize\normalfont
\endinput
%%
%% End of file `cfpbpresentation.cls'.
