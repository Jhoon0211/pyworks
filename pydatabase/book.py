# testdb -> book 테이블
import sqlite3

def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/testdb.db")
    return conn

print(getconn(), "연결 객체 생성")

# 테이블 생성
def create():
    conn = getconn()
    cursor = conn.cursor() # sql을 조작하는 cursor 함수
    # AUTOINCREMENT(오라클 : create sequence) : 시퀸스 자동 생성
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            page INTEGER
        )
    """
    cursor.execute(sql) # 실행
    conn.commit()  # 커밋 완료
    conn.close()

# 책 추가
def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO book(title, author, page) " \
          "VALUES(?, ?, ?)"
    #cursor.execute(sql, ('혼자 공부하는 자바', '신용권', 600))
    cursor.execute(sql, ('python projects', '켄 유엔스', 500))
    conn.commit()
    conn.close()

# 책 검색
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)   # 리스트로 출력
    for i in rs:  # 튜플로 출력 ex) 1, 2
        print(i)
    conn.close()

# 책 1권 검색
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = 2"
    cursor.execute(sql, (2, ))
    rs = cursor.fetchone()
    print(rs)
    conn.close()

# 책 수정
def update():
    conn = getconn()
    cursor = conn.cursor()
    # 책 번호가 2번인 책의 페이지를 650로 페이지로 번경하기
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (650, 2))
    conn.commit()
    conn.close()

# 책 삭제
def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 책 번호가 1번인 책 삭제
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1, ))
    conn.commit()
    conn.close()

#create()
#insert()
#select_one()
#update()
select()
#delete()