#!/usr/bin/env python3
"""
main file
"""
from user import User

from flask_sqlalchemy import SQLAlchemy
print(User.__tablename__)
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

