import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", db="my_python" )
 

try:
    with connection.cursor() as cursor:
        # Create a new record 
        sql = "SELECT * FROM  `users`"
        cursor.execute(sql)
        print(cursor.description)
        print()
        for row in cursor:
        	print(row)
    connection.commit()    	
 
finally:
    connection.close()