from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Message
from PORTIFOLIO import mail

contactPage = Blueprint('contactPage', __name__)

@contactPage.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        subject = request.form['subject']
        sender = request.form['email']
        body = request.form['message']

        try:
            msg = Message(subject, sender=sender, recipients=["karinna.rocha2@gmail.com"])
            msg.body = body
            mail.send(msg)
            flash('Message sent successfully!')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Error: {str(e)}')

        return redirect(url_for('contactPage.contact'))
    
    return render_template('Contact.html')