import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='pythondec'

)
def get_data():
    cursor =db.cursor()
    sql='select * from movie'
    cursor.execute(sql)
    movies=cursor.fetchall()
    yield movies
movies=get_data()
for m in movies:
    print(m)