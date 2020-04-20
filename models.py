from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)


# For any table inside of the database, there is one class defined inside models.py.

# Adding db.Model in parentheses after class names indicates that these classes ‘inherit’ from db.Model. 
# The details of inheritance are unimportant right now; simply, this allows for the class to have some built-in relationship with SQLAlchemy to interact with the database.

# __tablename__ naturally corresponds with the table name inside the database.

# Every property is defined as a db.Column, which will become columns in the table. 
# The arguments to db.Column are naturally similar to those use for table creation in SQL.

# Note that flights.id is marked as a foreign key using the __tablename__ flights, not the class name Flight.