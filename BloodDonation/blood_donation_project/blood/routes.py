from flask import render_template, request, redirect, url_for
from . import blood
from .models import Donation
from app import db

@blood.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        description = request.form['description']
        location = request.form['location']
        new_donation = Donation(description=description, location=location)
        db.session.add(new_donation)
        db.session.commit()
        return redirect(url_for('blood.donations'))
    return render_template('blood/donation_form.html')

@blood.route('/donations')
def donations():
    donations = Donation.query.all()
    return render_template('blood/donation_list.html', donations=donations)
