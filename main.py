from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os

from openai import OpenAI

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Sample user database
users = {
    'rak@example.com': {'username': 'Rakesh HR', 'password': '1235'},
    'sid@example.com': {'username': 'Siddartha R', 'password': '6541'}
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

client = OpenAI(api_key='')

@app.route('/chatbot')
def chatbot():
    if 'username' not in session:
        flash('You must be logged in to view the chatbot.')
        return redirect(url_for('login'))
    
    return render_template('chatbot.html', username=session['username'])
     

@app.route('/chat_with_bot', methods=['POST'])
def chat_with_bot():
    user_message = request.json['message']

    response = client.chat.completions.create(
        
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful law and legal assistant ."},
        {"role": "user", "content": user_message}
        ]
    )

    
    ai_reply = response.choices[0].message.content


    return jsonify({'message': ai_reply})



@app.route('/image_gen')
def imagegen():
    if 'username' in session:
        return render_template('image_generation.html', username=session['username'])
    return redirect(url_for('login'))




@app.route('/ai_caption_voice')
def ai_caption_voice():
    if 'username' in session:
        return render_template('ai_bytes.html', username=session['username'])
    return redirect(url_for('login'))
    

@app.route('/audio_trans')
def audio_trans():
    if 'username' in session:
        return render_template('audio_service_index.html', username=session['username'])

    return redirect(url_for('login'))
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
