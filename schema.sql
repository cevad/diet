CREATE TABLE foods (
       foodnum INTEGER PRIMARY KEY,
       name VARCHAR(100),
       calories REAL,
       servingsperpkg REAL,
       Fat REAL,
       cholesterol REAL,
       sodium REAL,
       carbohydrate REAL,
       fiber REAL,
       sugar REAL,
       protein REAL
);
CREATE TABLE "mealnames" (
    "mealnum" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL
);
CREATE TABLE "meals" (
    "foodnum" INTEGER NOT NULL,
    "quantity" REAL NOT NULL DEFAULT (1.0),
    "mealnum" INTEGER NOT NULL,
    FOREIGN KEY(foodnum) REFERENCES foods(foodnum),
    FOREIGN KEY(mealnum) REFERENCES mealnames(mealnum)
);
CREATE TABLE "foodlog" (
	time TEXT ,
	name TEXT,
	calories REAL,
	fat REAL,
	cholesterol REAL,
	sodium REAL,
	carbohydrate REAL,
	fiber REAL,
	sugar REAL,
	protein REAL
);
