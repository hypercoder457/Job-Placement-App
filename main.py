from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

class JobPost(db.Model):
    # Job title, Job summary, qualifications, responsibilites + duties, benefits, Job ID needed as primary key else error will occur
    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.String, nullable=False)
    duties = db.Column(db.String, nullable=False)
    qualifications = db.Column(db.String, nullable=False)
    benefits = db.Column(db.String, nullable=False)
    c_name = db.Column(db.String, nullable=False)
    c_img = db.Column(db.String(20), nullable=False, default='images/default-logo.png')

    def __str__(self) -> str:
        return f"Job: {self.job_title} at {self.c_name}"

@app.route("/")
def home(): return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
