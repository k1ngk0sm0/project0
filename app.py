from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discs')
def discs():
    return render_template('discs.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == "__main__":
    app.run(debug=True)