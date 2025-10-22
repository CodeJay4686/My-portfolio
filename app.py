from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jasonjapheth265@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_message = request.form['message']

        msg = Message(
            subject=f"New message from {user_name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            reply_to=user_email,
            body=f"From: {user_name}\nEmail: {user_email}\n\nMessage:\n{user_message}"
        )

        mail.send(msg)
        return render_template('sent.html')

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)