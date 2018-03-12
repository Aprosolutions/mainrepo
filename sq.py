import MySQLdb
db =   MySQLdb.connect("localhost","","","stud123455")
cursor=db.cursor()
#cursor.execute("DROP TABLE EMPLOYEE")
cursor.execute("CREATE TABLE EMP12234(NAME CHAR(20) NOT NULL,AGE INT)")
cursor.execute("INSERT INTO EMP12234 VALUES('ANU',20)")
cursor.execute("INSERT INTO EMP12234 VALUES('MINU',29)")
cursor.execute("INSERT INTO EMP12234 VALUES('VINU',23)")
cursor.execute("SELECT * FROM EMP12234")
data=cursor.fetchall()
for i in data:
	print('{0}|{1}'.format(i[0],i[1]))
cursor.execute("UPDATE EMP12234 SET NAME='BINU' WHERE AGE=20")
data=cursor.fetchall()
for i in data:
	print('{0}|{1}'.format(i[0],i[1]))
cursor.execute("delete from EMP12234 where AGE='23'")
cursor.execute("SELECT * FROM EMP12234")
data=cursor.fetchall()
for i in data:
	print('{0}|{1}'.format(i[0],i[1]))
cursor.execute("commit")
db.close()

