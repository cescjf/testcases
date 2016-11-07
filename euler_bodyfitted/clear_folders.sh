#/usr/bin/bash!

#clear all files named DEFAULT.*
find . -type f -regex '.*DEFAULT\..*' -delete

#clear all files that are inside a folder names results
find . -type f -regex '.*/results/.*' -delete

#clear all files with the ending .der
find . -type f -regex '.*\.der.*' -delete

#clear all files with the ending .vmo
find . -type f -regex '.*\.vmo.*' -delete

#clear naca.nodefile which ic created by SDESIGN
find . -type f -regex '.*\.nodefile' -delete
