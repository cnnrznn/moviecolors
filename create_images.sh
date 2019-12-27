#!/bin/bash

N=8

for f in movie
do
    ((i=i%N)); ((i++==0)) && wait

    {
      fn=$(basename $f)
      basefn=${fn%.mp4}
      python3 colorscan_avg.py $f >${basefn}_colors.txt
      python3 bands.py ${basefn}_colors.txt ${basefn}_colors.svg
      inkscape -z -e ${basefn}_colors.png -w 2000 -h 10000 ${basefn}_colors.svg
    } &
done

