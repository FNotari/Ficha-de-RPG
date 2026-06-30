from data.database import Database

db = Database()

df = db.get_table("Classes")

classe = db.get_by_id("Classes",1)

print(classe)