import pandas as pd
from krecommend.recommend import KRecommend

#posts_table.csv is a csv file is a f containg webscraped information on s news site, a "title" column which is the title/headline of the news and a content column which is the main content of the news.
df = pd.read_csv("posts_table.csv", index_col=0)
print(df.shape)
#fitting
recommender = KRecommend(k=2)
recommender.fit(df, text_columns=["content","title"])

#test with a particular index
index = 421
test_content=df["content"][index]
test_title=df["title"][index]

#get reçommemdations
recommendations=recommender.predict([test_title,test_content])
print(recommendations)