import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#creating a new sqlalchemy table and copying contents from the "posts_table dataframe" into the table.
df = pd.read_csv("posts_table.csv", index_col=0)
df = df.dropna()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db = SQLAlchemy(app)


"""a table with name 'Posts', primary_key 'id', text (string) columns 'title' and 'content' ' """
class Posts(db.Model):
    __tablename__="Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.String(64))






if __name__=="__main__":
	db.create_all()
	db.session.add_all([Posts(title=df["title"][i],content=df["content"][i]) for i in range(250)])
	db.session.commit()