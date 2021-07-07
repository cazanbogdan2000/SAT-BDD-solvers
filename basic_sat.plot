   ###########################
   # plotting script example
   ###########################
   
   reset
   set xrange [5:16]
   set yrange [0:15]
   c = 2.45
   f(x) = c**(x - 12)
   
   plot "basic_sat.dat", f(x)