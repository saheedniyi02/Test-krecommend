from curses import meta
import pandas as pd
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table


#creating a new sqlalchemy table and copying contents from the "posts_table dataframe" into the table.
df = pd.read_csv("posts_table.csv", index_col=0)
df = df.dropna()


#new sqltable
engine = create_engine("sqlite:///database.db", echo=True)
meta = MetaData()

posts = Table(
    "Posts",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("content", String),
)

meta.create_all(engine)

if __name__=="__main__":
	#copy the contents
	data = [{"title": df["title"][i], "content": df["content"][i]} for i in range(250)]
	ins = posts.insert()
	conn = engine.connect()
	result = conn.execute(ins, data)
	conn.close()
