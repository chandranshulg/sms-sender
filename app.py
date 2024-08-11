from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    receiver_email = request.form['receiver_email']
    subject = request.form['subject']
    message = request.form['message']
    password = request.form['password']

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
