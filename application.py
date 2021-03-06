from flask import Flask, render_template, request, url_for
# from application import db
# from application.models import Data

application = Flask(__name__)
application.debug = True
application.secret_key = None

class Projects(object):
	"""Represents all of my projects."""

	def __init__(self):
		self.projects = []

	def add_project(self, var_name, name, description, url):
		project = {
			'var_name': var_name, 
			'name': name, 
			'description': description,
			'url': url
		}
		self.projects.append(project)

	def get_projects(self):
		return self.projects

all_projects = Projects()

all_projects.add_project('tiny', 'Tiny', 'A web framework built in Python.', 'https://github.com/jimjshields/tiny')
all_projects.add_project('thank_the_academy', 'Thank the Academy', 'Randomly generate an Oscar acceptance speech.', 'http://thanktheacademy.herokuapp.com')
all_projects.add_project('heatmap', 'Box Office Heatmap', 'Get a heatmap of the weekly box office, from 1999 to now.', 'projects/heatmap')
all_projects.add_project('speech_analysis', 'Oscar Speech Analysis', 'Interactive visualization of all Oscar speeches since 1966.', 'http://thanktheacademy.herokuapp.com/analysis')
all_projects.add_project('rt_cli', 'Rotten Tomatoes CLI', 'A command-line interface for Rotten Tomatoes\' API.', 'https://github.com/jimjshields/rotten_tomatoes_CLI')
all_projects.add_project('best_picture', 'Scraping the Best Picture\'s Budgets', 'A scraper that grabs all of the available budgets of all Best Picture winners from Wikipedia.', 'https://github.com/jimjshields/best_picture')
all_projects.add_project('myvcs', 'My VCS', 'A simple, not-quite-finished version control system.', 'https://github.com/jimjshields/myvcs')

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html')

@application.route('/projects')
@application.route('/projects/<project>')
def projects(project=None):
	if not project:
		return render_template('projects.html', project=project, all_projects=all_projects.get_projects())
	else:
		return render_template('{}.html'.format(project), project=project, all_projects=all_projects.get_projects())

if __name__ == '__main__':
	application.run(debug=True)