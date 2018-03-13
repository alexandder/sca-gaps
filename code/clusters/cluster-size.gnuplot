set terminal pdfcairo transparent enhanced fontscale 0.9 size 15.00cm, 10.00cm 
set output 'cluster-size.pdf'
set format y "%.0f%%" 
set xlabel "gap introduction probability" 
set ylabel "percentage of isolated gaps" 
set grid
set bmargin 3.5
plot 'cluster_size.dat' u 1:(100*$2) w l title 'minimum', '' u 1:(100*$3) w l title 'average', '' u 1:(100*$4) w l title 'maximum', 50 w l notitle
