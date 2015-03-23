from flask import Flask, render_template, request
# from application import db
# from application.models import Data

application = Flask(__name__)
application.debug = True
application.secret_key = None

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	application.run(debug=True)