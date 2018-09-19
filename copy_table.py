import MySQLdb

connection = MySQLdb.connect (host = "localhost",
                              user = "root",
                              passwd = "mummydaddy",
                              db = "ehub")
connect = MySQLdb.connect (host = "localhost",
                              user = "root",
                              passwd = "mummydaddy",
                              db = "test")

cursor = connection.cursor()
cursor1 = connect.cursor()
file1 = open("/home/saranya/test.txt","r+")
lines = file1.readlines()
for line in lines:
	line = line.replace('\n',' ')
	line = line.split(' ')
	a=line.pop(0)
	line = ", ".join(line)
	line = line[:-2]
	query1 = "Create table ehub." + a + " Like test." + a
	print(query1)
	cursor.execute(query1)
	query ="Insert into ehub." + a + "("+line + ")" + "Select " + line + " from " + "test." + a
	cursor.execute(query)
	print(query)
	
	
file1.close() 
cursor.close()
connection.commit()
connection.close()
