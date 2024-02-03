#wapp to read student record --> READ


from sqlite3 import *

con = None


try:
	con=connect("kc.db")
	cursor=con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print(d)
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()