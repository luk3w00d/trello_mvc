from init import db, ma

class User(db.Model):   # This is for aurtherisation of the user
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)  # nullable means you can not leave this blank for the email
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)   # is_admin the "is" means its a boolean value

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')