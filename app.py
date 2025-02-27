from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Front-end Engineer',
        'location': 'Remote',
        'salary': 'Rs. 7,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Munich, Germany',
        'salary': '$120,000'
    }
]

@app.route('/')
def hello_ranjith():
    return render_template('home.html', jobs=JOBS, company_name='Ranjith')

@app.route('/api/jobs')
def json_type():
    return jsonify(JOBS)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
