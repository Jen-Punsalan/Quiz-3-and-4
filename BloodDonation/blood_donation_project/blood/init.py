from flask import Blueprint

blood = Blueprint('blood', __name__)

from . import routes  # Import routes
