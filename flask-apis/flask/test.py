import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

create_table = 'create table users (id integer,username text, password text)'
cursor.execute(create_table)

user = (1,';lkj','asdf')
insert_query = 'insert into users values (?, ?, ?)'
cursor.execute(insert_query,user)

users = [
    (2,'this','this'),
    (3,'that','that')
]
cursor.executemany(insert_query,users)


select_query = 'select * from users'
for row in cursor.execute(select_query):
    print(row)


connection.commit()
connection.close()