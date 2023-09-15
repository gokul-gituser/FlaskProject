from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Trivandrum,India',
    'salary' : '50k/month'
  },
   {
    'id' : 2,
    'title' : 'Software Developer',
    'location' : 'Chennai,India',
    'salary' : '50k/month'
  },
   {
    'id' : 3,
    'title' : 'Quality Analyst',
    'location' : 'Bengaluru,India',
    'salary' : '50k/month'
  },
   {
    'id' : 4,
    'title' : 'Backend Engineer',
    'location' : 'Remote',
    'salary' : '50k/month'
  },
]

@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS);


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
