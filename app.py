from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "haidar_trust_secret_key" # Required for flashing messages

@app.route('/')
def home():
    # This renders the index.html file from the /templates folder
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        # Logic to handle form submission (e.g., sending an email)
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real app, you would use Flask-Mail here
        flash("Thank you for reaching out! We will get back to you soon.", "success")
        return redirect(url_for('home'))

if __name__ == '__main__':
    # Set debug=True for development; change to False for production
    app.run(host = "0.0.0.0", port = 8000)