import sqlite3 as sql


class DataBase:
    def __init__(self):
        self.con = sql.connect("data.db")
        self.checkDB()

    def checkDB(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS `image_data` (`id` STRING, `filename` STRING,`data` FLOAT)")

    def writeDB(self, data):
        id = data["id"]
        filename = data["filename"]
        data = data['data']
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"INSERT INTO `image_data` VALUES ('{id}','{filename}','{data}')")

        self.con.commit()
        cur.close()

    def readDB(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT * FROM `image_data`")
            rows = cur.fetchall()
        self.con.commit()
        cur.close()
        return rows

    def readData(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute("SELECT `data` FROM `image_data`")
            rows = cur.fetchall()
        self.con.commit()
        cur.close()
        return rows


