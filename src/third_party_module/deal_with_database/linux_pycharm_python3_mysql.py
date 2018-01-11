import mysql.connector


class T:
    def test(self, **kwargs):
        db = mysql.connector.connect(**kwargs)
        cursor = db.cursor()
        cursor.execute("select host from user")
        s = cursor.fetchall()
        print(s)
        cursor.close()


t = T()
t.test(host='192.168.179.1', user='root', passwd='534255', db='mysql')
