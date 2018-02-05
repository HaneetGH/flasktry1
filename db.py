import MySQLdb

myDB = MySQLdb.connect(host="208.11.220.249",port=3306,user="XXXXX",passwd="XXXXX",db="XXXXX")
cHandler = myDB.cursor()
cHandler.execute("SHOW DATABASES")
results = cHandler.fetchall()
for items in results:
    print (items[items])