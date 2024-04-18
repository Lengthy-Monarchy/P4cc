from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='vendor', cascade='all, delete-orphan')

class Sweet(db.Model):
    __tablename__ = 'sweets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='sweet', cascade='all, delete-orphan')

class VendorSweet(db.Model):
    __tablename__ = 'vendor_sweets'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id', ondelete='CASCADE'))
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweets.id', ondelete='CASCADE'))
    vendor = db.relationship('Vendor', back_populates='vendor_sweets')
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')

    @db.validates('price')
    def validate_price(self, key, price):
        assert price is not None and price >= 0, "Price must have a value and cannot be negative"
        return price
