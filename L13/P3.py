#wapp to select into student
import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected")
	
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	for d in data:
		print("rno= ", d[0] , "name= ", d[1])

except cx_Oracle.DatabaseError as e:
	con.rollback()
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("disconnected")