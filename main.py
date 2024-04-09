from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Sample user database
users = {
    'rak@example.com': {'username': 'raki', 'password': '1235'},
    'sid@example.com': {'username': 'sidd', 'password': '6541'}
}

# Landing page route
@app.route('/')
def landing_page():
    return render_template('landing_page.html')



@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            session['username'] = users[email]['username']
            return redirect(url_for('home'))
        flash('Invalid email or password', 'error')
    return render_template('login.html')




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            flash('Email already exists', 'error')
        else:
            username = 'user' + str(len(users) + 1)
            users[email] = {'username': username, 'password': password}
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('signup.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/about_us1')
def aboutus1():
    return render_template('about_us1.html')


@app.route('/chatbot')
def chat_bot():
    if 'username' in session:
        return render_template('chatbot.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/image_gen')
def imagegen():
    if 'username' in session:
        return render_template('image_generation.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/audio_trans')
def audio_gen():
    return render_template('audio_gen.html')



@app.route('/voice_audio')
def ai_voice():
    return render_template('voice_aud.html')


if __name__ == '__main__':
    app.run(debug=True)
