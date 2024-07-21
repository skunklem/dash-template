from database.model import db
from database.tables import User, Address
# from dash import get_app

def table_search(table,**kwargs):
    """Returns rows from `table` where each kwarg (field_name=value) has been fullfilled, if possible

    Args:
        table (db.Model): Class of a particular table of interest
        kwargs: key, value pairs of attributes and their desired value

    Returns:
        (Result): a row or set of rows that satisfy the input conditions for a given table
    """
    stmt = db.select(table)
    for k,v in kwargs.items():
        print("kwargs:",k,v)
        stmt = stmt.where(getattr(table,k)==v)
    result = db.session.execute(stmt)
    return result

def item_exists(table,**kwargs):
    return bool(table_search(table,**kwargs).all())

def item_exists_once(table,**kwargs):
    result = table_search(table,**kwargs)
    return len(result) == 1

def insert_test_data():
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(
        name="patrick",
        fullname="Patrick Star",
        addresses=[Address(email_address="patty@sqlalchemy.org")],
        )
    users_to_add = [u for u in [spongebob, sandy, patrick] if not item_exists(User,name=u.name)]
    db.session.add_all(users_to_add)
    db.session.commit()
