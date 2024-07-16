from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from PORTIFOLIO import mail

contactPage = Blueprint('contactPage', __name__)

@contactPage.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject,
                      sender=email,
                      recipients=[current_app.config['MAIL_DEFAULT_SENDER']])
        msg.body = message
        mail.send(msg)

        flash('Email sent successfully!', 'success')
        return redirect(url_for('contactPage.contact'))
    
    return render_template('Contact.html')