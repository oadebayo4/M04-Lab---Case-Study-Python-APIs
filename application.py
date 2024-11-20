from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name} - {self.description}"
@app.route('/')
def index():
    return 'Hello!'
@app.route('/book')
def get_book():
    book = book.query.all()
    output = []
    for book in book:
        book_data = {'name': book.name, 'description': book.description}
        output.append(book_data)
        return {"books": output}
    @app.route('/books/<id>')
    def get_book(id):
        book = book.query.get_or_404(id)
        return {"name": book.name, "description": book.description}
@app.route('/books', methods=['POST'])
def add_book():
    book = book(name=request.json['name'],description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}