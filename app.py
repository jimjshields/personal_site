from flask import Flask, render_template, request
from app import db
# from app.models import Data

app = Flask(__name__)
app.debug = True
app.secret_key = None

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()