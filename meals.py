#!python

import os
import sqlite3

db=sqlite3.connect(os.environ['HOME']+"/.diet/food.db")
crs=db.cursor()
crs.execute(
"""
select 
	mealnames.name,
        sum(:1*meals.quantity*foods.calories)as calories,
        sum(:1*meals.quantity*foods.Fat) as fat,
        sum(:1*meals.quantity*foods.Cholesterol)as cholesterol,
        sum(:1*meals.quantity*foods.Sodium)as sodium,
        sum(:1*meals.quantity*foods.Carbohydrate) as carbohydrates,
        sum(:1*meals.quantity*foods.Fiber) as fiber,
        sum(:1*meals.quantity*foods.Sugar)as sugar,
        sum(:1*meals.quantity*foods.Protein) as protein
        from meals join "foods" using (foodnum) join "mealnames" using(mealnum) 
        group by (mealnum) order by mealnames.name  ;
""", (1,))
mn=""
print "               Name                    Cal    Fat   Chol  Sodium Carbs Fiber Sugar  Prot"
print "___________________________________  _______  _____  _____ _______ _____ _____ _____ _____"
for i in  crs.fetchall():
    if not(mn == i[0]):
         print "{0:36s} {1:7.1f} {2:6.1f} {3:6.1f} {4:7.1f} {5:5.1f} {6:5.1f} {7:5.1f} {8:5.1f}".format(*i)
#    print "{0:30s} {1:7.1f}".format("",i[1])
    mn=i[0]
print "___________________________________  _______  _____  _____ _______ _____ _____ _____ _____"
