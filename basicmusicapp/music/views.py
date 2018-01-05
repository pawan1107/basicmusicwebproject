from django.shortcuts import render
from django.http import HttpResponse
import pymysql
def index(request):
	connection = pymysql.connect(host="localhost", user="root", password="", db="my_python" )
	 

	try:
	    with connection.cursor() as cursor:
	        # Create a new record 
	        sql = "SELECT * FROM  `users`"
	        cursor.execute(sql)
	        print(cursor.description)
	        print()
	        for row in cursor: 
			return HttpResponse("<h1>row</h1>")
	    connection.commit()    	
	 
	finally:
	    connection.close()

 
