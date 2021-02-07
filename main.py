from flask import Flask, request, render_template
from sql_funk import create_author
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/author/", methods=['GET', 'POST'])
def author():
    if request.method == 'GET':
        return render_template('author.html')
    else:
        create_author(request.form['first_name'], request.form['last_name'])
        return render_template('author.html')



if __name__ == '__main__':
    app.run()
