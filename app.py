from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactme')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(port=9192)
