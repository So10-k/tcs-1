# # from flask import Flask, render_template, request, redirect, url_for, session
# # from itsdangerous import URLSafeSerializer
# # from functools import wraps
# # import uuid

# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'jhih'  # Replace with your actual secret key
# # serializer = URLSafeSerializer(app.config['SECRET_KEY'])

# # # Dictionary to store user credentials and profile information
# # users = {
# #     'admin': {
# #         'password': 'admin',
# #         'is_admin': True,
# #         'name': 'Admin User',
# #         'email': 'admin@example.com',
# #         'bio': 'This is the admin user.'
# #     }
# # }  # Default admin credentials

# # # Dictionary to store website settings
# # settings = {
# #     'login_page_text': 'Welcome to the login page!'
# # }

# # # List to store chat messages
# # messages = []

# # def login_required(f):
# #     @wraps(f)
# #     def decorated_function(*args, **kwargs):
# #         if 'username' not in session:
# #             return redirect(url_for('login'))
# #         return f(*args, **kwargs)
# #     return decorated_function

# # def admin_required(f):
# #     @wraps(f)
# #     def decorated_function(*args, **kwargs):
# #         if 'username' not in session or not users.get(session['username'], {}).get('is_admin', False):
# #             return redirect(url_for('login'))
# #         return f(*args, **kwargs)
# #     return decorated_function

# # @app.context_processor
# # def inject_serializer():
# #     return dict(serializer=serializer)

# # @app.route('/')
# # def home():
# #     print("Home route accessed")  # Debugging statement
# #     return render_template('index.html', login_page_text=settings['login_page_text'])

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     print("Login route accessed")  # Debugging statement
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         print(f"Username: {username}, Password: {password}")  # Debugging statement
# #         # Check the stored credentials
# #         if username in users and users[username]['password'] == password:
# #             session['username'] = username
# #             if users[username]['is_admin']:
# #                 return redirect(url_for('admin_panel'))
# #             encrypted_username = serializer.dumps(username)
# #             return redirect(url_for('user_home', username=encrypted_username))
# #         else:
# #             return 'Invalid credentials'
# #     return render_template('index.html', login_page_text=settings['login_page_text'])

# # @app.route('/logout')
# # def logout():
# #     session.pop('username', None)
# #     return redirect(url_for('home'))

# # @app.route('/create_account', methods=['GET', 'POST'])
# # def create_account():
# #     print("Create account route accessed")  # Debugging statement
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         # Store the new account credentials
# #         users[username] = {
# #             'password': password,
# #             'is_admin': False,
# #             'name': '',
# #             'email': '',
# #             'bio': ''
# #         }
# #         print(f"New account created: Username: {username}, Password: {password}")  # Debugging statement
# #         return redirect(url_for('login'))
# #     return render_template('create_account.html')

# # @app.route('/user/<username>')
# # @login_required
# # def user_home(username):
# #     decrypted_username = serializer.loads(username)
# #     print(f"User home route accessed for {decrypted_username}")  # Debugging statement
# #     return render_template('user_home.html', username=decrypted_username, users=users)

# # @app.route('/admin')
# # @admin_required
# # def admin_panel():
# #     print("Admin panel accessed")  # Debugging statement
# #     return render_template('admin_panel.html', users=users, settings=settings)

# # @app.route('/admin/create_user', methods=['GET', 'POST'])
# # @admin_required
# # def admin_create_user():
# #     print("Admin create user route accessed")  # Debugging statement
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         users[username] = {
# #             'password': password,
# #             'is_admin': False,
# #             'name': '',
# #             'email': '',
# #             'bio': ''
# #         }
# #         print(f"Admin created user: Username: {username}, Password: {password}")  # Debugging statement
# #         return redirect(url_for('admin_panel'))
# #     return render_template('admin_create_user.html')

# # @app.route('/admin/delete_user/<username>')
# # @admin_required
# # def admin_delete_user(username):
# #     print(f"Admin delete user route accessed for {username}")  # Debugging statement
# #     if username in users:
# #         del users[username]
# #         print(f"User {username} deleted")  # Debugging statement
# #     return redirect(url_for('admin_panel'))

# # @app.route('/admin/edit_user/<username>', methods=['GET', 'POST'])
# # @admin_required
# # def admin_edit_user(username):
# #     print(f"Admin edit user route accessed for {username}")  # Debugging statement
# #     if request.method == 'POST':
# #         new_password = request.form['password']
# #         users[username]['password'] = new_password
# #         print(f"User {username} password updated to {new_password}")  # Debugging statement
# #         return redirect(url_for('admin_panel'))
# #     return render_template('admin_edit_user.html', username=username)

# # @app.route('/admin/assign_admin/<username>')
# # @admin_required
# # def admin_assign_admin(username):
# #     print(f"Admin assign admin route accessed for {username}")  # Debugging statement
# #     if username in users:
# #         users[username]['is_admin'] = True
# #         print(f"User {username} assigned as admin")  # Debugging statement
# #     return redirect(url_for('admin_panel'))

# # @app.route('/admin/edit_settings', methods=['GET', 'POST'])
# # @admin_required
# # def admin_edit_settings():
# #     print("Admin edit settings route accessed")  # Debugging statement
# #     if request.method == 'POST':
# #         settings['login_page_text'] = request.form['login_page_text']
# #         print(f"Login page text updated to: {settings['login_page_text']}")  # Debugging statement
# #         return redirect(url_for('admin_panel'))
# #     return render_template('admin_edit_settings.html', settings=settings)

# # @app.route('/admin/view_user/<username>')
# # @admin_required
# # def admin_view_user(username):
# #     print(f"Admin view user route accessed for {username}")  # Debugging statement
# #     if username in users:
# #         user_info = users[username]
# #         return render_template('admin_view_user.html', username=username, user_info=user_info)
# #     return redirect(url_for('admin_panel'))

# # @app.route('/admin/reset_passwords')
# # @admin_required
# # def admin_reset_passwords():
# #     print("Admin reset passwords route accessed")  # Debugging statement
# #     for username in users:
# #         users[username]['password'] = 'defaultpassword'
# #         print(f"Password for {username} reset to 'defaultpassword'")  # Debugging statement
# #     return redirect(url_for('admin_panel'))

# # @app.route('/profile/<username>')
# # @login_required
# # def profile(username):
# #     print(f"Profile route accessed for {username}")  # Debugging statement
# #     if username in users:
# #         user_info = users[username]
# #         is_admin = users.get(session['username'], {}).get('is_admin', False)
# #         can_edit = session['username'] == username or is_admin
# #         return render_template('profile.html', username=username, user_info=user_info, can_edit=can_edit)
# #     return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

# # @app.route('/profile/edit/<username>', methods=['GET', 'POST'])
# # @login_required
# # def edit_profile(username):
# #     print(f"Edit profile route accessed for {username}")  # Debugging statement
# #     if username in users:
# #         if session['username'] == username or users.get(session['username'], {}).get('is_admin', False):
# #             if request.method == 'POST':
# #                 users[username]['name'] = request.form['name']
# #                 users[username]['email'] = request.form['email']
# #                 users[username]['bio'] = request.form['bio']
# #                 print(f"User {username} profile updated")  # Debugging statement
# #                 return redirect(url_for('profile', username=username))
# #             return render_template('edit_profile.html', username=username, user_info=users[username])
# #     return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

# # @app.route('/chat')
# # @login_required
# # def chat():
# #     print("Chat route accessed")  # Debugging statement
# #     return render_template('chat.html', messages=messages, username=session['username'], users=users)

# # @app.route('/chat/post', methods=['POST'])
# # @login_required
# # def post_message():
# #     print("Post message route accessed")  # Debugging statement
# #     message_id = str(uuid.uuid4())
# #     message = {
# #         'id': message_id,
# #         'username': session['username'],
# #         'text': request.form['text']
# #     }
# #     messages.append(message)
# #     print(f"Message posted: {message}")  # Debugging statement
# #     return redirect(url_for('chat'))

# # @app.route('/chat/edit/<message_id>', methods=['GET', 'POST'])
# # @login_required
# # def edit_message(message_id):
# #     print(f"Edit message route accessed for {message_id}")  # Debugging statement
# #     message = next((msg for msg in messages if msg['id'] == message_id), None)
# #     if message and (session['username'] == message['username'] or users.get(session['username'], {}).get('is_admin', False)):
# #         if request.method == 'POST':
# #             message['text'] = request.form['text']
# #             print(f"Message {message_id} edited")  # Debugging statement
# #             return redirect(url_for('chat'))
# #         return render_template('edit_message.html', message=message)
# #     return redirect(url_for('chat'))

# # @app.route('/chat/delete/<message_id>')
# # @login_required
# # def delete_message(message_id):
# #     print(f"Delete message route accessed for {message_id}")  # Debugging statement
# #     global messages
# #     message = next((msg for msg in messages if msg['id'] == message_id), None)
# #     if message and (session['username'] == message['username'] or users.get(session['username'], {}).get('is_admin', False)):
# #         messages = [msg for msg in messages if msg['id'] != message_id]
# #         print(f"Message {message_id} deleted")  # Debugging statement
# #     return redirect(url_for('chat'))

# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, url_for, session
# from itsdangerous import URLSafeSerializer
# from functools import wraps
# import sqlite3
# import uuid

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'jhih'  # Replace with your actual secret key
# serializer = URLSafeSerializer(app.config['SECRET_KEY'])

# # Initialize the database
# def init_db():
#     with sqlite3.connect('database.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 username TEXT PRIMARY KEY,
#                 password TEXT NOT NULL,
#                 is_admin BOOLEAN NOT NULL,
#                 name TEXT,
#                 email TEXT,
#                 bio TEXT
#             )
#         ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS messages (
#                 id TEXT PRIMARY KEY,
#                 username TEXT NOT NULL,
#                 text TEXT NOT NULL,
#                 FOREIGN KEY (username) REFERENCES users (username)
#             )
#         ''')
#         conn.commit()

# init_db()

# def query_db(query, args=(), one=False):
#     with sqlite3.connect('database.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute(query, args)
#         rv = cursor.fetchall()
#         conn.commit()
#         return (rv[0] if rv else None) if one else rv

# def get_user(username):
#     user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
#     if user:
#         return {
#             'username': user[0],
#             'password': user[1],
#             'is_admin': user[2],
#             'name': user[3],
#             'email': user[4],
#             'bio': user[5]
#         }
#     return None

# def get_all_users():
#     users = query_db('SELECT * FROM users')
#     return {user[0]: {
#         'password': user[1],
#         'is_admin': user[2],
#         'name': user[3],
#         'email': user[4],
#         'bio': user[5]
#     } for user in users}

# def get_all_messages():
#     messages = query_db('SELECT * FROM messages')
#     return [{'id': msg[0], 'username': msg[1], 'text': msg[2]} for msg in messages]

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'username' not in session:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         user = get_user(session['username'])
#         if 'username' not in session or not user['is_admin']:
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# @app.context_processor
# def inject_serializer():
#     return dict(serializer=serializer)

# @app.route('/')
# def home():
#     print("Home route accessed")  # Debugging statement
#     return render_template('index.html', login_page_text='Welcome to the login page!')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("Login route accessed")  # Debugging statement
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         print(f"Username: {username}, Password: {password}")  # Debugging statement
#         user = get_user(username)
#         if user and user['password'] == password:
#             session['username'] = username
#             if user['is_admin']:
#                 return redirect(url_for('admin_panel'))
#             encrypted_username = serializer.dumps(username)
#             return redirect(url_for('user_home', username=encrypted_username))
#         else:
#             return 'Invalid credentials'
#     return render_template('index.html', login_page_text='Welcome to the login page!')

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))

# @app.route('/create_account', methods=['GET', 'POST'])
# def create_account():
#     print("Create account route accessed")  # Debugging statement
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         query_db('INSERT INTO users (username, password, is_admin, name, email, bio) VALUES (?, ?, ?, ?, ?, ?)', 
#                  [username, password, False, '', '', ''])
#         print(f"New account created: Username: {username}, Password: {password}")  # Debugging statement
#         return redirect(url_for('login'))
#     return render_template('create_account.html')

# @app.route('/user/<username>')
# @login_required
# def user_home(username):
#     decrypted_username = serializer.loads(username)
#     print(f"User home route accessed for {decrypted_username}")  # Debugging statement
#     users = get_all_users()
#     return render_template('user_home.html', username=decrypted_username, users=users)

# @app.route('/admin')
# @admin_required
# def admin_panel():
#     print("Admin panel accessed")  # Debugging statement
#     users = get_all_users()
#     return render_template('admin_panel.html', users=users, settings={'login_page_text': 'Welcome to the login page!'})

# @app.route('/admin/create_user', methods=['GET', 'POST'])
# @admin_required
# def admin_create_user():
#     print("Admin create user route accessed")  # Debugging statement
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         query_db('INSERT INTO users (username, password, is_admin, name, email, bio) VALUES (?, ?, ?, ?, ?, ?)', 
#                  [username, password, False, '', '', ''])
#         print(f"Admin created user: Username: {username}, Password: {password}")  # Debugging statement
#         return redirect(url_for('admin_panel'))
#     return render_template('admin_create_user.html')

# @app.route('/admin/delete_user/<username>')
# @admin_required
# def admin_delete_user(username):
#     print(f"Admin delete user route accessed for {username}")  # Debugging statement
#     query_db('DELETE FROM users WHERE username = ?', [username])
#     print(f"User {username} deleted")  # Debugging statement
#     return redirect(url_for('admin_panel'))

# @app.route('/admin/edit_user/<username>', methods=['GET', 'POST'])
# @admin_required
# def admin_edit_user(username):
#     print(f"Admin edit user route accessed for {username}")  # Debugging statement
#     if request.method == 'POST':
#         new_password = request.form['password']
#         query_db('UPDATE users SET password = ? WHERE username = ?', [new_password, username])
#         print(f"User {username} password updated to {new_password}")  # Debugging statement
#         return redirect(url_for('admin_panel'))
#     return render_template('admin_edit_user.html', username=username)

# @app.route('/admin/assign_admin/<username>')
# @admin_required
# def admin_assign_admin(username):
#     print(f"Admin assign admin route accessed for {username}")  # Debugging statement
#     query_db('UPDATE users SET is_admin = ? WHERE username = ?', [True, username])
#     print(f"User {username} assigned as admin")  # Debugging statement
#     return redirect(url_for('admin_panel'))

# @app.route('/admin/edit_settings', methods=['GET', 'POST'])
# @admin_required
# def admin_edit_settings():
#     print("Admin edit settings route accessed")  # Debugging statement
#     if request.method == 'POST':
#         settings['login_page_text'] = request.form['login_page_text']
#         print(f"Login page text updated to: {settings['login_page_text']}")  # Debugging statement
#         return redirect(url_for('admin_panel'))
#     return render_template('admin_edit_settings.html', settings=settings)

# @app.route('/admin/view_user/<username>')
# @admin_required
# def admin_view_user(username):
#     print(f"Admin view user route accessed for {username}")  # Debugging statement
#     user_info = get_user(username)
#     if user_info:
#         return render_template('admin_view_user.html', username=username, user_info=user_info)
#     return redirect(url_for('admin_panel'))

# @app.route('/admin/reset_passwords')
# @admin_required
# def admin_reset_passwords():
#     print("Admin reset passwords route accessed")  # Debugging statement
#     query_db('UPDATE users SET password = ?', ['defaultpassword'])
#     print("All passwords reset to 'defaultpassword'")  # Debugging statement
#     return redirect(url_for('admin_panel'))

# @app.route('/profile/<username>')
# @login_required
# def profile(username):
#     print(f"Profile route accessed for {username}")  # Debugging statement
#     user_info = get_user(username)
#     if user_info:
#         is_admin = get_user(session['username'])['is_admin']
#         can_edit = session['username'] == username or is_admin
#         return render_template('profile.html', username=username, user_info=user_info, can_edit=can_edit)
#     return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

# @app.route('/profile/edit/<username>', methods=['GET', 'POST'])
# @login_required
# def edit_profile(username):
#     print(f"Edit profile route accessed for {username}")  # Debugging statement
#     if session['username'] == username or get_user(session['username'])['is_admin']:
#         if request.method == 'POST':
#             query_db('UPDATE users SET name = ?, email = ?, bio = ? WHERE username = ?', 
#                      [request.form['name'], request.form['email'], request.form['bio'], username])
#             print(f"User {username} profile updated")  # Debugging statement
#             return redirect(url_for('profile', username=username))
#         user_info = get_user(username)
#         return render_template('edit_profile.html', username=username, user_info=user_info)
#     return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

# @app.route('/chat')
# @login_required
# def chat():
#     print("Chat route accessed")  # Debugging statement
#     messages = get_all_messages()
#     users = get_all_users()
#     return render_template('chat.html', messages=messages, username=session['username'], users=users)

# @app.route('/chat/post', methods=['POST'])
# @login_required
# def post_message():
#     print("Post message route accessed")  # Debugging statement
#     message_id = str(uuid.uuid4())
#     query_db('INSERT INTO messages (id, username, text) VALUES (?, ?, ?)', 
#              [message_id, session['username'], request.form['text']])
#     print(f"Message posted: {message_id}")  # Debugging statement
#     return redirect(url_for('chat'))

# @app.route('/chat/edit/<message_id>', methods=['GET', 'POST'])
# @login_required
# def edit_message(message_id):
#     print(f"Edit message route accessed for {message_id}")  # Debugging statement
#     message = query_db('SELECT * FROM messages WHERE id = ?', [message_id], one=True)
#     if message and (session['username'] == message[1] or get_user(session['username'])['is_admin']):
#         if request.method == 'POST':
#             query_db('UPDATE messages SET text = ? WHERE id = ?', [request.form['text'], message_id])
#             print(f"Message {message_id} edited")  # Debugging statement
#             return redirect(url_for('chat'))
#         return render_template('edit_message.html', message={'id': message[0], 'username': message[1], 'text': message[2]})
#     return redirect(url_for('chat'))

# @app.route('/chat/delete/<message_id>')
# @login_required
# def delete_message(message_id):
#     print(f"Delete message route accessed for {message_id}")  # Debugging statement
#     message = query_db('SELECT * FROM messages WHERE id = ?', [message_id], one=True)
#     if message and (session['username'] == message[1] or get_user(session['username'])['is_admin']):
#         query_db('DELETE FROM messages WHERE id = ?', [message_id])
#         print(f"Message {message_id} deleted")  # Debugging statement
#     return redirect(url_for('chat'))

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session
from itsdangerous import URLSafeSerializer
from functools import wraps
import sqlite3
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhih'  # Replace with your actual secret key
serializer = URLSafeSerializer(app.config['SECRET_KEY'])

# Initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                is_admin BOOLEAN NOT NULL,
                name TEXT,
                email TEXT,
                bio TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                text TEXT NOT NULL,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        # Insert default admin user if not exists
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password, is_admin, name, email, bio)
            VALUES ('admin', 'admin', 1, 'Admin User', 'admin@example.com', 'This is the admin user.')
        ''')
        conn.commit()

init_db()

def query_db(query, args=(), one=False):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        rv = cursor.fetchall()
        conn.commit()
        return (rv[0] if rv else None) if one else rv

def get_user(username):
    user = query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
    if user:
        return {
            'username': user[0],
            'password': user[1],
            'is_admin': user[2],
            'name': user[3],
            'email': user[4],
            'bio': user[5]
        }
    return None

def get_all_users():
    users = query_db('SELECT * FROM users')
    return {user[0]: {
        'password': user[1],
        'is_admin': user[2],
        'name': user[3],
        'email': user[4],
        'bio': user[5]
    } for user in users}

def get_all_messages():
    messages = query_db('SELECT * FROM messages')
    return [{'id': msg[0], 'username': msg[1], 'text': msg[2]} for msg in messages]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_user(session['username'])
        if 'username' not in session or not user['is_admin']:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.context_processor
def inject_serializer():
    return dict(serializer=serializer)

@app.route('/')
def home():
    print("Home route accessed")  # Debugging statement
    return render_template('index.html', login_page_text='Welcome to the login page!')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route accessed")  # Debugging statement
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username}, Password: {password}")  # Debugging statement
        user = get_user(username)
        if user and user['password'] == password:
            session['username'] = username
            if user['is_admin']:
                return redirect(url_for('admin_panel'))
            encrypted_username = serializer.dumps(username)
            return redirect(url_for('user_home', username=encrypted_username))
        else:
            return 'Invalid credentials'
    return render_template('index.html', login_page_text='Welcome to the login page!')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    print("Create account route accessed")  # Debugging statement
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query_db('INSERT INTO users (username, password, is_admin, name, email, bio) VALUES (?, ?, ?, ?, ?, ?)', 
                 [username, password, False, '', '', ''])
        print(f"New account created: Username: {username}, Password: {password}")  # Debugging statement
        return redirect(url_for('login'))
    return render_template('create_account.html')

@app.route('/user/<username>')
@login_required
def user_home(username):
    decrypted_username = serializer.loads(username)
    print(f"User home route accessed for {decrypted_username}")  # Debugging statement
    users = get_all_users()
    return render_template('user_home.html', username=decrypted_username, users=users)

@app.route('/admin')
@admin_required
def admin_panel():
    print("Admin panel accessed")  # Debugging statement
    users = get_all_users()
    return render_template('admin_panel.html', users=users, settings={'login_page_text': 'Welcome to the login page!'})

@app.route('/admin/create_user', methods=['GET', 'POST'])
@admin_required
def admin_create_user():
    print("Admin create user route accessed")  # Debugging statement
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query_db('INSERT INTO users (username, password, is_admin, name, email, bio) VALUES (?, ?, ?, ?, ?, ?)', 
                 [username, password, False, '', '', ''])
        print(f"Admin created user: Username: {username}, Password: {password}")  # Debugging statement
        return redirect(url_for('admin_panel'))
    return render_template('admin_create_user.html')

@app.route('/admin/delete_user/<username>')
@admin_required
def admin_delete_user(username):
    print(f"Admin delete user route accessed for {username}")  # Debugging statement
    query_db('DELETE FROM users WHERE username = ?', [username])
    print(f"User {username} deleted")  # Debugging statement
    return redirect(url_for('admin_panel'))

@app.route('/admin/edit_user/<username>', methods=['GET', 'POST'])
@admin_required
def admin_edit_user(username):
    print(f"Admin edit user route accessed for {username}")  # Debugging statement
    if request.method == 'POST':
        new_password = request.form['password']
        query_db('UPDATE users SET password = ? WHERE username = ?', [new_password, username])
        print(f"User {username} password updated to {new_password}")  # Debugging statement
        return redirect(url_for('admin_panel'))
    return render_template('admin_edit_user.html', username=username)

@app.route('/admin/assign_admin/<username>')
@admin_required
def admin_assign_admin(username):
    print(f"Admin assign admin route accessed for {username}")  # Debugging statement
    query_db('UPDATE users SET is_admin = ? WHERE username = ?', [True, username])
    print(f"User {username} assigned as admin")  # Debugging statement
    return redirect(url_for('admin_panel'))

@app.route('/admin/edit_settings', methods=['GET', 'POST'])
@admin_required
def admin_edit_settings():
    print("Admin edit settings route accessed")  # Debugging statement
    if request.method == 'POST':
        settings['login_page_text'] = request.form['login_page_text']
        print(f"Login page text updated to: {settings['login_page_text']}")  # Debugging statement
        return redirect(url_for('admin_panel'))
    return render_template('admin_edit_settings.html', settings=settings)

@app.route('/admin/view_user/<username>')
@admin_required
def admin_view_user(username):
    print(f"Admin view user route accessed for {username}")  # Debugging statement
    user_info = get_user(username)
    if user_info:
        return render_template('admin_view_user.html', username=username, user_info=user_info)
    return redirect(url_for('admin_panel'))

@app.route('/admin/reset_passwords')
@admin_required
def admin_reset_passwords():
    print("Admin reset passwords route accessed")  # Debugging statement
    query_db('UPDATE users SET password = ?', ['defaultpassword'])
    print("All passwords reset to 'defaultpassword'")  # Debugging statement
    return redirect(url_for('admin_panel'))

@app.route('/profile/<username>')
@login_required
def profile(username):
    print(f"Profile route accessed for {username}")  # Debugging statement
    user_info = get_user(username)
    if user_info:
        is_admin = get_user(session['username'])['is_admin']
        can_edit = session['username'] == username or is_admin
        return render_template('profile.html', username=username, user_info=user_info, can_edit=can_edit)
    return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

@app.route('/profile/edit/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    print(f"Edit profile route accessed for {username}")  # Debugging statement
    if session['username'] == username or get_user(session['username'])['is_admin']:
        if request.method == 'POST':
            query_db('UPDATE users SET name = ?, email = ?, bio = ? WHERE username = ?', 
                     [request.form['name'], request.form['email'], request.form['bio'], username])
            print(f"User {username} profile updated")  # Debugging statement
            return redirect(url_for('profile', username=username))
        user_info = get_user(username)
        return render_template('edit_profile.html', username=username, user_info=user_info)
    return redirect(url_for('user_home', username=serializer.dumps(session['username'])))

@app.route('/chat')
@login_required
def chat():
    print("Chat route accessed")  # Debugging statement
    messages = get_all_messages()
    users = get_all_users()
    return render_template('chat.html', messages=messages, username=session['username'], users=users)

@app.route('/chat/post', methods=['POST'])
@login_required
def post_message():
    print("Post message route accessed")  # Debugging statement
    message_id = str(uuid.uuid4())
    query_db('INSERT INTO messages (id, username, text) VALUES (?, ?, ?)', 
             [message_id, session['username'], request.form['text']])
    print(f"Message posted: {message_id}")  # Debugging statement
    return redirect(url_for('chat'))

@app.route('/chat/edit/<message_id>', methods=['GET', 'POST'])
@login_required
def edit_message(message_id):
    print(f"Edit message route accessed for {message_id}")  # Debugging statement
    message = query_db('SELECT * FROM messages WHERE id = ?', [message_id], one=True)
    if message and (session['username'] == message[1] or get_user(session['username'])['is_admin']):
        if request.method == 'POST':
            query_db('UPDATE messages SET text = ? WHERE id = ?', [request.form['text'], message_id])
            print(f"Message {message_id} edited")  # Debugging statement
            return redirect(url_for('chat'))
        return render_template('edit_message.html', message={'id': message[0], 'username': message[1], 'text': message[2]})
    return redirect(url_for('chat'))

@app.route('/chat/delete/<message_id>')
@login_required
def delete_message(message_id):
    print(f"Delete message route accessed for {message_id}")  # Debugging statement
    message = query_db('SELECT * FROM messages WHERE id = ?', [message_id], one=True)
    if message and (session['username'] == message[1] or get_user(session['username'])['is_admin']):
        query_db('DELETE FROM messages WHERE id = ?', [message_id])
        print(f"Message {message_id} deleted")  # Debugging statement
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)