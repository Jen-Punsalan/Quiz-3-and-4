from flask import render_template
from . import admin
from account.models import User
from blood.models import Donation

@admin.route('/dashboard')
def dashboard():
    total_users = User.query.count()
    total_donations = Donation.query.count()
    return render_template('admin/dashboard.html', total_users=total_users, total_donations=total_donations)
