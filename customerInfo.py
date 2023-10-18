from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing-page.html')

@app.route('/submit', methods=['POST'])
def submit():
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    phone = request.form.get('phone')

    with open('customers.csv', 'a', newline='') as csvfile:
        fieldnames = ['firstName', 'lastName', 'email', 'phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'firstName': firstName, 'lastName': lastName, 'email': email, 'phone': phone})

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')
    
if __name__ == '__main__':
    app.run(debug=True)