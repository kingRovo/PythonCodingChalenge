import sqlite3
con=sqlite3.connect("updesh.db")
c=con.cursor()
#c.execute("create table employee(name text,age integer,sly integer)")
c.execute("insert into employee values('updesh',19,3400)")

c.execute("select *from employee where sly <2000")
print(c.fetchall())
con.commit()
con.close()
