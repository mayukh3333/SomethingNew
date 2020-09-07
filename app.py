import flask
from flask import Flask,render_template

app = Flask(__name__)
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
