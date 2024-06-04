from flask import Flask, render_template, request, redirect, url_for, session
from user import Usuario

app = Flask(__name__)
app.secret_key = 'supersecretkey'

usuario1 = Usuario('admin', 'admin')
# Ruta


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == usuario1.username and password == usuario1.password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Datos incorrectos, intentelo de nuevo'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
