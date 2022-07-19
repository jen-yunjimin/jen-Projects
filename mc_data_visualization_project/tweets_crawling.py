# import twitter scrape module
!pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

tweets_list = []
# netflix 키워드 포함하는 2022-01-01 ~ 2022-01-15 트윗 크롤링
# 10000개의 트윗이 추출되면 stop
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('netflix since:2022-01-01 until:2022-01-15').get_items()):
    if i>10000:
        break
    tweets_list.append([tweet.date, tweet.content])
    
# 데이터프레임 생성
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])
tweets_df
