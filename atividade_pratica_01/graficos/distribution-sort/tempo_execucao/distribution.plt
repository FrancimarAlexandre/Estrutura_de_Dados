set title "Distribution Sort"
set xlabel "Tamanho do vetor"
set ylabel "Tempo (segundos)"
set grid
set key left top
set datafile separator whitespace

plot "distribution_sort.txt" using 1:2 with linespoints title "counting", \

