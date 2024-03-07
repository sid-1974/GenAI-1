from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Landing page route
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

# Login page route
@app.route('/login')
def login():
    return render_template('login.html')

# Signup page route
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)





