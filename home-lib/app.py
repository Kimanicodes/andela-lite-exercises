from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play/<name>')
def play(name):
    return 'Hello ' + name

if __name__ == '__main__':
    app.run(debug=True)
