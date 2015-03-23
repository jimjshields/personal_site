from application import db

class WeeklyBoxOfficeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, unique=False)
    dates = db.Column(db.String(50), unique=False)
    top_12_gross = db.Column(db.Integer, unique=False)
    top_12_change = db.Column(db.Float, unique=False)
    total_gross = db.Column(db.Integer, unique=False)
    total_change = db.Column(db.Float, unique=False)
    total_movies = db.Column(db.Integer, unique=False)
    top_movie = db.Column(db.String(128), unique=False)
    week_num = db.Column(db.Integer, unique=False)
    inflation_adj_total_gross = db.Column(db.Integer, unique=False)
    
    def __init__(self):
        pass

    def __repr__(self):
        return '<Data {year} - Week {week_num}>'.format(year=self.year, week_num=self.week_num)