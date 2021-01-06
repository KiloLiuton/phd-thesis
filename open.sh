#!/bin/sh
nvim -c "b4" -c "VimtexCompile" ./KLR_thesis.tex tex/chapter*tex tex/references.bib
