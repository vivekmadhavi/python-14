
from sqlite3 import *
con=None


try:
	con=connect("kit.db");
	cursor=con.cursor();
	sql ="select *  from emp"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("id=",d[0],"  name =",d[1],"  salary =",d[2])
except Exception as e:
	print("isseu",e)
finally:
	if con is not None:
		con.close()