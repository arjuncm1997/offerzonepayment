from OfferZone import db,login_manager,app
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    usertype = db.Column(db.String)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return self.username+","+self.email

class Mall(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    ownerid = db.Column(db.String)
    owner = db.Column(db.String)
    name = db.Column(db.String(40), unique=False, nullable=False)
    desc = db.Column(db.String(200))
    addr1 = db.Column(db.String(100))
    addr2 = db.Column(db.String(100))
    addr3 = db.Column(db.String(100))
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    phone=db.Column(db.String(25))
    open_time=db.Column(db.String(10))
    close_time=db.Column(db.String(10))
    latitude = db.Column(db.String(40))
    Logitude = db.Column(db.String(40))
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    place = db.Column(db.String)
    status = db.Column(db.String(40))
    sho = db.relationship('Shop', backref='malll', lazy=True)
   
    def __repr__(self):
        return str(self.id)


class Shop(db.Model,UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        owner = db.Column(db.String)
        name = db.Column(db.String(40), unique=False, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        phoneno=db.Column(db.String(25))
        desc = db.Column(db.String(200))
        image = db.Column(db.String(20), nullable=False, default='default.jpg')
        category=db.Column(db.String(50))
        mallid = db.Column(db.Integer, db.ForeignKey('mall.id'),
            nullable=False)
        pro = db.relationship('Product', backref='shop', lazy=True)
   
        def __repr__(self):
            return str(self.id)
        
       

class Product(db.Model,UserMixin):
     id = db.Column(db.Integer,primary_key=True)
     owner1 = db.Column(db.String)
     name = db.Column(db.String(40),unique=False,nullable=False)
     owner = db.Column(db.String(40))
     price = db.Column(db.Integer)
     desc = db.Column(db.String(199))
     img = db.Column(db.String(20), nullable=False, default='default.jpg')
     shopid = db.Column(db.Integer, db.ForeignKey('shop.id'),
            nullable=False)

     
     offers = db.relationship('Offer', backref='product', lazy=True)
   
     def __repr__(self):
            return str(self.id)
   

class Offer(db.Model,UserMixin):
     id = db.Column(db.Integer,primary_key=True)
     owner = db.Column(db.String)
     name = db.Column(db.String(40),unique=False,nullable=False)
     price =  db.Column(db.Integer)
   
     desc = db.Column(db.String(199))
     dis = db.Column(db.Integer)
     image = db.Column(db.String(20), nullable=False, default='default.jpg')

     productid = db.Column(db.Integer, db.ForeignKey('product.id'),
            nullable=False)
   
   
#class TrackUser(db.Model,UserMixin):
    # id = db.Column(db.Integer,primary_key=True)
   #  productid = db.Column(db.Integer, db.ForeignKey('product.id')
   #         nullable=False)
   #  userid = db.Column(db.Integer, db.ForeignKey('user.id'),
   #         nullable=False)
  #   track = db.relationship('Product', backref='trackuser', lazy=True)
  #   def __repr__(self):
  #          return str(self.id)
   
   


class Gallery(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.VARCHAR)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')

class Contact(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String(120))
    message = db.Column(db.String(120))
    usertype = db.Column(db.String(120))


class Place(db.Model,UserMixin):
     id = db.Column(db.Integer,primary_key=True)
     place = db.Column(db.String(40),unique=False,nullable=False)


class Purchase(db.Model,UserMixin):
     id = db.Column(db.Integer,primary_key=True)
     userid = db.Column(db.String)
     productid = db.Column(db.String)
     uname = db.Column(db.String(40))
     unumber = db.Column(db.Integer)
     uaddress = db.Column(db.String(199))
     method = db.Column(db.String(199))
     tracking = db.Column(db.String(100))
     