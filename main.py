from flask import Flask, request, render_template
from sql_funk import create_author, create_publisher, get_all_authors
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route("/author/", methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        create_author(request.form['first_name'], request.form['last_name'])
    data = get_all_authors()
    return render_template('author.html', authors=data)


@app.route("/publisher/", methods=['GET', 'POST'])
def publisher():
    if request.method == 'GET':
        return render_template('publisher.html')
    else:
        create_publisher(request.form['first_name'], request.form['last_name'])
        return render_template('publisher.html')


if __name__ == '__main__':
    app.run()
