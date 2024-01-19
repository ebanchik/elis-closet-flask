from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # Use SQLite for simplicity
db = SQLAlchemy(app)

class Post(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 title = db.Column(db.String(80), nullable=False)
 content = db.Column(db.Text, nullable=False)

 def __repr__(self):
     return '<Post %r>' % self.title

@app.route('/post', methods=['POST'])
def create_post():
 title = request.json['title']
 content = request.json['content']
 post = Post(title=title, content=content)
 db.session.add(post)
 db.session.commit()
 return jsonify({'message': 'Post created'}), 201

if __name__ == '__main__':
  with app.app_context():
      db.create_all()
  app.run()
