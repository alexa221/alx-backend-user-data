#!/usr/bin/env python3
"""
main file
"""
from user import User

from flask_sqlalchemy import SQLAlchemy
print(User.__tablename__)
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
"""
main-1.py
"""
from db import DB
from user import User
 
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)

except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)

except InvalidRequestError:
    print("Invalid") 

