import MySQLdb
db = MySQLdb.connect("localhost","","","stud12345" )
cursor = db.cursor()
#cursor.execute("CREATE TABLE EMP (NAME CHAR(20) NOT NULL,AGE INT,SEX CHAR(1),INCOME FLOAT)")
cursor.execute("INSERT INTO EMP VALUES('ANNA',24,'F',20000)")
cursor.execute("INSERT INTO EMP VALUES('ANU',20,'M',25000)")
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
for i in data:
	print('{0:4}|{1}|{2}|{3}'.format(i[0],i[1],i[2],i[3]))
cursor.execute("UPDATE EMP SET NAME= 'ARYA' WHERE AGE=24")
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
for i in data:
	print('{0:4}|{1}|{2}|{3}'.format(i[0],i[1],i[2],i[3]))
cursor.execute("DELETE  FROM EMP WHERE AGE=20")
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall()
for i in data:
	print('{0:4}|{1}|{2}|{3}'.format(i[0],i[1],i[2],i[3]))
cursor.execute("commit")
db.close()
