#!/bin/bash

rule_max=255
alpha=$1

echo "set term pdfcairo size 10cm,10cm font 'Helvetica,12';
set termopt enhanced;
set output 'heatmap-$alpha.pdf';
set view map;
set pm3d map;
set pm3d corners2color c1;
set palette defined(0 'black', 0.1 'dark-blue', 0.5 'blue', 0.9 'light-blue', 1 'white');
set xrange[0:$rule_max];
set yrange[0:255];
set xlabel 'A_1';
set ylabel 'A_2';
unset key;
set xtics 0,32,256;
set ytics 0,32,256;
set xtics add ('255' 255);
set ytics add ('255' 255);
splot 'data-$alpha.dat' u 1:2:3 with pm3d;
set term png size 1000, 1000;
set output 'heatmap-$alpha.png';
replot;
" | gnuplot

