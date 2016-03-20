#!/usr/bin/python
import os
import sqlite3

class db(object):
    def __init__(self):
        self.dbconn=sqlite3.connect(os.environ['HOME']+"/.diet/food.db")
        self.c=self.dbconn.cursor()
        pass
    def getfoods(self):
        pass
    def getmealnames(self):
        self.c.execute("""
            select name,mealnum from mealnames order by name;
        """)
        return self.c.fetchall()
    def getmeals(self):
        pass
    def getdaylog(self):
        self.c.execute(
            """
            select 
            datetime(time,'localtime'),
            name,
	    (calories) as calories,
	    (fat)as fat,
	    ("cholesterol") as cholesterol,
	    (sodium) as sodium,
	    (carbohydrate) as carbohydrate,
	    (fiber) as fiber,
	    (sugar) as sugar,
	    (protein) AS protein 
            from foodlog 
            where time between datetime("now" ,"-1 days") and datetime("now") order by (time);
            """)
        return self.c.fetchall()
    def getdaysum(self):
        self.c.execute("""
        select 
        " ",
	" ",
	SUM(calories) as calories,
	SUM(fat)as fat,
	SUM("cholesterol") as cholesterol,
	SUM(sodium) as sodium,
	SUM(carbohydrate) as carbohydrate,
	SUM(fiber) as fiber,
	SUM(sugar) as sugar,
        SUM(protein) AS protein
            from foodlog 

            where time between datetime("now" ,"-1 days") and datetime("now");
            """)
        return self.c.fetchall()
    def getLogText(self):
        log=self.getdaylog()
        text=("{0:>20s} {1:>35s} {2:>6s} {3:>6s} {4:>6s} {5:>7s} {6:>6s} {7:>6s} {8:>6s} {9:>6s}\n".
              format("Time","Name","cal","fat","clstr","NaCl","carb","fib","sugr","prot"))
        text+=("{0:>20s} {1:35s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}\n".
               format("--------------------","-----------------------------------","------"))
        if log:
            for i in log:
                text+=("{0:>20s} {1:35} {2:6.1f} {3:6.1f} {4:6.1f} {5:7.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}\n".
                   format(*i))
        text+=("{0:>20s} {1:35s} {2:>6s} {2:6s} {2:6s} {2:>7s} {2:6s} {2:6s} {2:6s} {2:6s}\n".
               format("--------------------","-----------------------------------","------"))
        if log:
            for i in self.getdaysum():
                text+="{0:>20s} {1:35} {2:6.1f} {3:6.1f} {4:6.1f} {5:7.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}".format(*i)
        return text
    def logmeal(self,mealnum,quant):
        self.c.execute("""
        insert into "foodlog" select 
	datetime("now"),
	mealnames.name,
        sum(:1*meals.quantity*foods.calories)as calories,
        sum(:1*meals.quantity*foods.Fat) as fat,
        sum(:1*meals.quantity*foods.Cholesterol)as cholesterol,
        sum(:1*meals.quantity*foods.Sodium)as sodium,
        sum(:1*meals.quantity*foods.Carbohydrate) as carbohydrates,
        sum(:1*meals.quantity*foods.Fiber) as fiber,
        sum(:1*meals.quantity*foods.Sugar)as sugar,
        sum(:1*meals.quantity*foods.Protein) as protein
        from mealnames join "meals" using(mealnum) join foods using (foodnum)  where mealnum=:2;
        """,(quant,mealnum));
        self.dbconn.commit()

        
    
if __name__=='__main__':
    a=db()
    b=a.getdaylog()
    print "{0:>20s} {1:>30s} {2:>6s} {3:>5s} {4:>5s} {5:>6s} {6:>5s} {7:>5s} {8:>5s} {9:>5s}".format("Time","Name","cal","fat","clstr","NaCl","carb","fib","sugr","prot")
    print "{0:>20s} {1:35s} {2:>6s} {2:5s} {2:5s} {2:>6s} {2:5s} {2:5s} {2:5s} {2:5s}".format("--------------------","----------------------------------------","-----")    
    for i in b:
        print "{0:>20s} {1:35} {2:6.1f} {3:5.1f} {4:5.1f} {5:6.1f} {6:5.1f} {7:5.1f} {8:5.1f} {9:5.1f}".format(*i)
    print "{0:>20s} {1:35s} {2:>6s} {2:5s} {2:5s} {2:>6s} {2:5s} {2:5s} {2:5s} {2:5s}".format("--------------------","----------------------------------------","-----")    
    for i in a.getdaysum():
        print "{0:>20s} {1:35} {2:6.1f} {3:5.1f} {4:5.1f} {5:6.1f} {6:5.1f} {7:5.1f} {8:5.1f} {9:5.1f}".format(*i)

        


