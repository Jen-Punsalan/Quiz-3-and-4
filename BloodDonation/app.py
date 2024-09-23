from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import blueprints
from account import account as account_blueprint
from blood import blood as blood_blueprint
from admin import admin as admin_blueprint

app.register_blueprint(account_blueprint, url_prefix='/account')
app.register_blueprint(blood_blueprint, url_prefix='/blood')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
import sys
print(sys.path)
