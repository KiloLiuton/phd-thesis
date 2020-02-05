#!/bin/bash
pdflatex KLR_thesis
bibtex KLR_thesis
pdflatex KLR_thesis
# bibtex KLR_thesis
pdflatex KLR_thesis
./clean.sh

