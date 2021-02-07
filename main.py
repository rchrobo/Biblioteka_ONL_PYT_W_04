from flask import Flask, request, render_template
from sql_funk import create_author, create_publisher, get_all_authors, \
    get_all_publishers, get_author_by_id, update_author_by_id
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


@app.route("/autor/<int:id>/", methods=['GET', 'POST'])
def edit_author(id):
    if request.method == "POST":
        update_author_by_id(request.form['first_name'], request.form['last_name'],id)
    author = get_author_by_id(id)
    return render_template('author_edit.html', author=author)


@app.route("/publisher/", methods=['GET', 'POST'])
def publisher():
    if request.method == 'GET':
        create_publisher(request.form['first_name'], request.form['last_name'])

    data = get_all_publishers()
    return render_template('publisher.html', publishers=data)


if __name__ == '__main__':
    app.run()
