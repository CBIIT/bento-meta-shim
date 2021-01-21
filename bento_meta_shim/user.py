from  .n4jdb_wcm import N4jdb_wcm

class User:
    def getUser(self, id):
        sql = 'SELECT * from users where id = %d'
        with N4jdb_wcm() as db:
            db.execute(sql, (id))
            result = db.fetchall()

        return result
 