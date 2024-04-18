from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Vendor, Sweet, VendorSweet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/vendors', methods=['GET'])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([{'id': v.id, 'name': v.name} for v in vendors])

@app.route('/vendors/<int:id>', methods=['GET'])
def get_vendor(id):
    vendor = Vendor.query.get(id)
    if vendor is None:
        return jsonify({"error": "Vendor not found"}), 404
    vendor_data = {
        "id": vendor.id,
        "name": vendor.name,
        "vendor_sweets": [{
            "id": vs.id,
            "price": vs.price,
            "sweet": {
                "id": vs.sweet.id,
                "name": vs.sweet.name
            },
            "sweet_id": vs.sweet_id,
            "vendor_id": vs.vendor_id
        } for vs in vendor.vendor_sweets]
    }
    return jsonify(vendor_data)

@app.route('/sweets', methods=['GET'])
def get_sweets():
    sweets = Sweet.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in sweets])

@app.route('/sweets/<int:id>', methods=['GET'])
def get_sweet(id):
    sweet = Sweet.query.get(id)
    if sweet is None:
        return jsonify({"error": "Sweet not found"}), 404
    return jsonify({"id": sweet.id, "name": sweet.name})

@app.route('/vendor_sweets', methods=['POST'])
def add_vendor_sweet():
    data = request.json
    if not data or 'price' not in data or data['price'] < 0:
        return jsonify({"errors": ["Price must be non-negative and provided."]}), 400
    new_vs = VendorSweet(price=data['price'], vendor_id=data['vendor_id'], sweet_id=data['sweet_id'])
    db.session.add(new_vs)
    db.session.commit()
    return jsonify({
        "id": new_vs.id,
        "price": new_vs.price,
        "sweet": {
            "id": new_vs.sweet.id,
            "name": new_vs.sweet.name
        },
        "sweet_id": new_vs.sweet_id,
        "vendor": {
            "id": new_vs.vendor.id,
            "name": new_vs.vendor.name
        },
        "vendor_id": new_vs.vendor_id
    }), 201

@app.route('/vendor_sweets/<int:id>', methods=['DELETE'])
def delete_vendor_sweet(id):
    vs = VendorSweet.query.get(id)
    if vs is None:
        return jsonify({"error": "VendorSweet not found"}), 404
    db.session.delete(vs)
    db.session.commit()
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
