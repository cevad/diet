#!python
#!/usr/biin/python

import os
import sqlite3

db=sqlite3.connect(os.environ['HOME']+"/.diet/food.db")
crs=db.cursor()
crs.execute(
"""
select date(time,"localtime")as t,
    sum("calories"),
    sum(fat),
    sum(cholesterol),
    sum(sodium),
    sum(carbohydrate),
    sum(fiber),
    sum(sugar),
    sum(protein)
    from foodlog group by (t);
"""
)
    
print ("{0:>20s} {2:>6s} {3:>6s} {4:>6s} {5:>7s} {6:>6s} {7:>6s} {8:>6s} {9:>6s}".
              format("Time","","cal","fat","clstr","NaCl","carb","fib","sugr","prot"))
print( "{0:>20s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}".
               format("--------------------","", "------"))
for i in crs.fetchall():
#    print i
    print ("{0:>20s} {1:6.1f} {2:6.1f} {3:6.1f} {4:7.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f}".
           format(*i))

db.close()

