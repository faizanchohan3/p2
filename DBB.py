import pymysql as mq

objsql=mq.connect(host="localhost",user="root",password="",database="school")
curs=objsql.cursor()


print("{:<15} {:<25}".format("id","name"))
sql="select * from student"
curs.execute(sql)
stfd=curs.fetchall()
for s in stfd:
    print("{:<15} {:<25}".format(s[0], s[1]))

try:
    std_id=str(input("enter the name"))
    sqlde="update from student where sch_id =%s"
    curs.execute(sqlde,std_id)
    objsql.commit()
    print("delete")
except:
    print("faizanS")