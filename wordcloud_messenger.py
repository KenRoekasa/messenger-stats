import json

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def deEmojify(text):
    regrex_pattern = re.compile(pattern =
        u"\u00f0.*? ", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


def generate_tables(filename="jsons/rob.json"):
    f = open(filename)
    y = json.load(f)
    df = pd.DataFrame.from_dict(y['messages'])
    participants = []
    for name in y['participants']:
        participants.append(name['name'])
    return participants,df


participants, df = generate_tables()


def create_wordcloud(df, person):
    filter_df =df.copy()
    filter_df = filter_df[filter_df["sender_name"] == person]  # filter for the person
    messages = filter_df['content']
    messages.dropna(inplace=True)
    full_msg_string = " ".join(messages)
    full_msg_string = deEmojify(full_msg_string)
    wordcloud = WordCloud(background_color="white").generate(full_msg_string)
    return wordcloud



wordcloud = create_wordcloud(df,participants[0])

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()