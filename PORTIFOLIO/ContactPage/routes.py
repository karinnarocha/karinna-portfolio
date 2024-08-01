from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Message
from PORTIFOLIO import mail

contactPage = Blueprint('contactPage', __name__)

@contactPage.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        subject = request.form['subject']
        user_email = request.form['email']
        body = request.form['message']

        try:
            # Set a no-reply address as the sender
            no_reply_address = "no-reply@example.com"  # Replace with your no-reply address

            # Create the message
            msg = Message(subject, sender=no_reply_address, recipients=["karinna.rocha2@gmail.com"])
            msg.body = f"From: {user_email}\n\n{body}"

            # Set the reply-to to the user's email
            msg.reply_to = user_email

            # Send the email
            mail.send(msg)
            flash('Message sent successfully!')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Error: {str(e)}')

        return redirect(url_for('contactPage.contact'))
    
    return render_template('Contact.html')