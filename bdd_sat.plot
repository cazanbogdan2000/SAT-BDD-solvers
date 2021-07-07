   ###########################
   # plotting script example
   ###########################
   
   reset
   set xrange [5:17]
   set yrange [0:15]
   c = 2.45
   f(x) = c**(x - 14)
   
   plot "bdd_sat.dat", f(x)