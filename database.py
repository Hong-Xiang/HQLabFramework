from hqlf import db
from hqlf.models.user import User

db.create_all()
adam = User('Adam', 'pass', 'test@test.com')
eve = User('Eve', 'pass', 'test2@test.com')
db.session.add(eve)
db.session.add(adam)
db.session.commit()
u = User.query.get(1)
print(u)
print(u.get_id())
print(u.email)
print(u.password)