# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:21:10 2019

@author: Weijun
"""
#%%
import numpy as np
import pandas as pd


#!pip install twitter

from twitter import Twitter
from twitter import OAuth

from pandas.io.json import json_normalize


apikey='LmWo260maj5KsmP3wnigGiymR'
apisecretkey='wdFhGB3XV79csLvSI57R1OFavsXNntbdtmlJzy2spNdMIFbnxn'
accesstoken='4012083173-pdPffs50tApeBURWR9QQt22rlhEp0sdEaCFwBvR'
accesstokensecret='PVwr62zsdUF0QQpcRMkPDBLxJ4HhAG4Cjccy49GwPv8pK'

oauth = OAuth(accesstoken,accesstokensecret,apikey,apisecretkey)
api = Twitter(auth=oauth)

#####  new imports ##################
import pip

#!pip install wordcloud

from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import matplotlib.pyplot as plt
#%%
stop =stopwords.words('english')

#%%
df = pd.DataFrame()
mid = 0 
for i in range(34):
    if i == 0:
        tjson = api.statuses.user_timeline(scree_name = 'realDonaldTrump', tweet_mode = 'extended', count = 200)
    else:
        tjson = api.statuses.user_timeline(scree_name = 'realDonaldTrump', tweet_mode = 'extended', count = 200,
                                           max_id = mid)
    if len(tjson) > 0:
        dftrump = json_normalize(tjson)
        mid = dftrump['id'].min()
        mid = mid - 1 
        df = pd.concat([df,dftrump], ignore_index=True)


#%%
wordcloud = WordCloud().generate(df.loc[0,'full_text'])
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#%%
wordcloud = WordCloud(stopwords=['the','has','of','lost','news']).generate(df.loc[0,'full_text'])
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#%%
wordcloud2 = WordCloud(background_color="white",stopwords=stop).generate(df.loc[0,'full_text'])
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()

#%%
type(df.full_text)

#%%
# ERROR ! ! 
wordcloud2 = WordCloud(background_color="white",stopwords=stop).generate(df.full_text)
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()

#%%
# Display the generated image:
tx2=df.full_text.str.cat(sep=' ')

#%%
wordcloud3 = WordCloud(stopwords=stop).generate(tx2)
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis("off")
plt.show()

#%%
stop.append('RT')
stop.append('co')
stop.append('https')
stop.append('amp')

#%%
wordcloud4 = WordCloud(background_color="white",stopwords=stop,max_words=1000).generate(tx2)
plt.imshow(wordcloud4, interpolation='bilinear')
plt.axis("off")
plt.show()


#%%
wordcloud4 = WordCloud(background_color="white",stopwords=stop,max_words=10).generate(tx2)
plt.imshow(wordcloud4, interpolation='bilinear')
plt.axis("off")
plt.show()



