# import sqlite3
# import datetime

# now = datetime.datetime.now()
# nowdatetime = now.strftime('%Y-%m-%d')

# print(nowdatetime)
# print(sqlite3.version)
# print(sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
# conn = sqlite3.connect(r'C:\study\neca\resource\database.db', isolation_level=None)
# c = conn.cursor()
# # # print(type(c))

# 테이블 생성(Date Type : TEXT NYMERIC INTEGER REAL BLOB)
# c.execute("create table if not exists users(id integer primary key, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("Insert into users values(1, 'kim', 'kim@naver.com', '000-0000-0000', 'kim.com', ?)", (nowdatetime,))
# c.execute("insert into users(id, username, email, phone, website, regdate) values (?,?,?,?,?,?)", (2, 'park', 'park@daum.net', '010-0000-0000', 'park.com', nowdatetime))

# # # # many 삽입(튜플, 리스트)
# userlist = (
#     (3, 'lee', 'lee@naver.com', '010-0000-0000', 'lee.com', nowdatetime),
#     (4, 'kee', 'kee@naver.com', '010-0000-0000', 'kee.com', nowdatetime),
#     (5, 'joo', 'joo@naver.com', '010-0000-0000', 'joo.com', nowdatetime),
#     )

# c.executemany("insert into users(id, username, email, phone, website, regdate) values (?,?,?,?,?,?)", userlist)

# # 테이블 데이터 삭제
# conn.execute("delete from users")
# print("users db deleted : ", conn.execute("delete from users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# 롤백
# conn.rollback()
# 접속 해제
# conn.close()

# C, R, U, D

# conn = sqlite3.connect(r'C:\study\neca\resource\database.db')
# c = conn.cursor()
# print(dir(c.execute("select * from users")))



# # 1개 로우 선택
# print(c.fetchone())

# # 지정 로우 선택
# print(c.fetchmany(size=3))

# 전체 로우 선택
# print(c.fetchall())

# onemore

# 순회 1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회 2
# for row in c.fetchall():
#     print('retrieve1 > ', row)

# 순회 3
# for row in c.execute('select * from users order by id desc'):
#     print('retrieve3 > ', row)

# where retrieve1
# param1 = (3,)
# c.execute('select * from users where id=?', param1)
# print('param1 > ', c.fetchone())
# print('param1 > ', c.fetchall())

# # where retrieve2
# param2 = 4
# c.execute('select * from users where id=%s' % str(param2))
# print('param2 > ', c.fetchone())
# print('param2 > ', c.fetchall())

# # where retrieve3
# param3 = {}
# c.execute('select * from users where id=:ID', {"ID": 5})
# print('param3 > ', c.fetchone())
# print('param3 > ', c.fetchone())


# # where retrieve4
# param4 = (3,5)
# c.execute('select * from users where id in(?,?)', param4)
# print('param4 > ', c.fetchall())

# # where retrieve5
# param5 = (3,5)
# c.execute('select * from users where id in("%d","%d")' % param5)
# print('param5 > ', c.fetchall())


# c.execute('select id, username from users where id=:id1 or id=:id2', {"id1": 2, "id2": 5})
# print('param6 > ', c.fetchall())

# # Dump 출력
# with conn:
#     with open(r'c:\study\neca\resource\dump.sql', 'w') as f:
#         for line in conn.iterdump():
#             f.write('%s\n' % line)
#         print('Dump Print Complete')

# conn.close() f.close()

# conn = sqlite3.connect(r'C:\study\neca\resource\database.db')

# 커서 연결
# c = conn.cursor()

# update
# c.execute('update users set username = ? where id = ?',('niceman', 2))

# c.execute('update users set username = :name where id = :id', {"name":"kim_bok_man", "id":1})

# c.execute('update users set username = "%s" where id = "%s"' % ('badboy', 3))


# row delete
# c.execute('delete from users where id = ?', (2,))
# c.execute('delete from users where id = :id', {"id":5})
# c.execute('delete from users where id = "%s"' % 4)

# for user in c.execute('select * from users'):
    # print(user)

# 테이브 전체 삭제
# print("users db deleted : ", c.execute('delete from users').rowcount, "rows")

# conn.commit()
# conn.close()
