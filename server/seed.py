# First import your Flask app instance
from app import app, db
from models import Vendor, Sweet, VendorSweet

def clear_data():
    """Clears all data from the database."""
    db.session.query(VendorSweet).delete()
    db.session.query(Vendor).delete()
    db.session.query(Sweet).delete()
    db.session.commit()

def add_data():
    """Adds sample data to the database."""
    vendor1 = Vendor(name="Insomnia Cookies")
    vendor2 = Vendor(name="Cookies Cream")
    vendor3 = Vendor(name="Candyland")
    sweet1 = Sweet(name="Chocolate Chip Cookie")
    sweet2 = Sweet(name="Brownie")
    sweet3 = Sweet(name="Caramel Candy")
    vendor_sweet1 = VendorSweet(price=1.50, vendor=vendor1, sweet=sweet1)
    vendor_sweet2 = VendorSweet(price=2.00, vendor=vendor1, sweet=sweet2)
    vendor_sweet3 = VendorSweet(price=3.00, vendor=vendor2, sweet=sweet1)
    vendor_sweet4 = VendorSweet(price=1.75, vendor=vendor3, sweet=sweet3)

    db.session.add_all([vendor1, vendor2, vendor3, sweet1, sweet2, sweet3,
                        vendor_sweet1, vendor_sweet2, vendor_sweet3, vendor_sweet4])
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        clear_data()
        add_data()
        print("Database seeded successfully!")
