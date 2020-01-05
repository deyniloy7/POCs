import pymysql

class Database:
    def __init__(self):
        host = "devsecureleafdb.c2b8fclhjjzi.us-east-2.rds.amazonaws.com"
        user = "nenapu"
        password = "nenapulabs"
        db = "secureleafdb"

        self.con = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT * FROM Questions GROUP BY idquestions, company")
        result = self.cur.fetchall()
        return result
