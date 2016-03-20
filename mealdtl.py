#!python
#!/usr/biin/python

import os
import sqlite3

db=sqlite3.connect(os.environ['HOME']+"/.diet/food.db")
crs=db.cursor()
crs.execute(
"""
select mealnames.name, quantity, foods.name from meals 
join mealnames using (mealnum)
join foods using(foodnum)
order by mealnames.name;
"""
)
plast=""
for i in crs.fetchall():
    current=i[0]
    if plast == current:
        current=""
    plast=i[0]
    print "{:>34} {:5.1f} {:30}".format(current,*i[1:])


