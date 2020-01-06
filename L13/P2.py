#wapp to insert into student
import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected")
	rno = int(input("enter rno "))
	name = input("enter name")

	cursor = con.cursor()
	sql = "insert into student values('%d','%s')"
	args =(rno , name)
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount,"records inserted ")
except cx_Oracle.DatabaseError as e:
	con.rollback()
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("disconnected")