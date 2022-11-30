import mysql.connector
mycn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="excel_project")
cursor=mycn.cursor()
query="select * from data_csv1"
cursor.execute(query)
data=cursor.fetchall()
for i in data:
    print(i)
