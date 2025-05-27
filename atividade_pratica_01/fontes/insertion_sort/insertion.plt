set title "Insertion Sort"
set xlabel "Tamanho do vetor"
set ylabel "Tempo (segundos)"
set grid
set key left top
set datafile separator whitespace

plot "insertion_sort_tb.txt" using 1:2 with lines title "Melhor Caso", \
     "insertion_sort_tw.txt" using 1:2 with lines title "Pior Caso", \
     "insertion_sort_ta.txt" using 1:2 with lines title "Caso Medio"
