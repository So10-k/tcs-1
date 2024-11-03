from flask import Flask, render_template, request, redirect, url_for
from itsdangerous import URLSafeSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
serializer = URLSafeSerializer(app.config['SECRET_KEY'])

@app.route('/')
def home():
    print("Home route accessed")  # Debugging statement
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route accessed")  # Debugging statement
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username}, Password: {password}")  # Debugging statement
        # Add your authentication logic here
        if username == 'admin' and password == 'password':  # Example check
            encrypted_username = serializer.dumps(username)
            return redirect(url_for('user_home', username=encrypted_username))
        else:
            return 'Invalid credentials'
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    print("Create account route accessed")  # Debugging statement
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your account creation logic here
        print(f"New account created: Username: {username}, Password: {password}")  # Debugging statement
        return redirect(url_for('login'))
    return render_template('create_account.html')

@app.route('/user/<username>')
def user_home(username):
    decrypted_username = serializer.loads(username)
    print(f"User home route accessed for {decrypted_username}")  # Debugging statement
    return render_template('user_home.html', username=decrypted_username)

if __name__ == '__main__':
    app.run(debug=True)