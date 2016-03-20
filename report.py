#!python
#!/usr/biin/python

import os
import sqlite3

db=sqlite3.connect(os.environ['HOME']+"/.diet/food.db")
crs=db.cursor()
crs.execute(
"""
select      datetime(b.time,'localtime'),
            b.name,
	    (b.calories) as calorie,
	    (b.fat)as fat,
	    (b.cholesterol) as cholesterol,
	    (b.sodium) as sodium,
	    (b.carbohydrate) as carbohydrate,
	    (b.fiber) as fiber,
	    (b.sugar) as sugar,
	    (b.protein) AS protein,
            b.rowid,
     a.* from 
  (select rowid, 
   date(time,"-7 hours")as t1,  
   *
   from foodlog order by time) as b
left join 
   (select time, rowid, date(time,"localtime")as t,
    sum("calories"),
    sum(fat),
    sum(cholesterol),
    sum(sodium),
    sum(carbohydrate),
    sum(fiber),
    sum(sugar),
    sum(protein)
    from foodlog group by (t))as a
using(rowid);
"""
)
#j=0
#print [i[0] for i in crs.description]
#print
#desc={crs.description[i][0]:i for i in range(0,len(crs.description))}
#print desc
#print

    
print ("{0:>20s} {1:>35s} {2:>6s} {3:>6s} {4:>6s} {5:>7s} {6:>6s} {7:>6s} {8:>6s} {9:>6s}".
              format("Time","Name","cal","fat","clstr","NaCl","carb","fib","sugr","prot"))
print( "{0:>20s} {1:35s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}".
               format("--------------------","-----------------------------------","------"))
for i in crs.fetchall():
    print ("{0:>20s} {1:35s} {2:6.1f} {3:6.1f} {4:6.1f} {5:7.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}".
                   format(*(i[0:10])))
    if i[11]:
        print ("{0:>20s} {1:35s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}".
               format("--------------------","-----------------------------------","------"))
        print ("{0:>20s} {1:35} {2:6.1f} {3:6.1f} {4:6.1f} {5:7.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}\n".
              format(i[13],"",*i[14:]))
        print ("{0:>20s} {1:>35s} {2:>6s} {3:>6s} {4:>6s} {5:>7s} {6:>6s} {7:>6s} {8:>6s} {9:>6s}".
              format("Time","Name","cal","fat","clstr","NaCl","carb","fib","sugr","prot"))
        print( "{0:>20s} {1:35s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}".
               format("--------------------","-----------------------------------","------"))

db.close()

