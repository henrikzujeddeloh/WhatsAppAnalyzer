import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

import modules.constants as const


def show_heatmap(data_frame):
    
    data_frame['weekday'] = data_frame['timestamp'].dt.day_name()

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data_frame['weekday'] = pd.Categorical(data_frame['weekday'], categories=week_days, ordered=True)
    data_frame = data_frame.sort_values('weekday')

    data_frame['hour'] = data_frame['timestamp'].dt.hour

    hour_weekday = data_frame.groupby(["weekday", "hour"]).size().unstack()

    fig_heatmap, axs_heatmap = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    sns.heatmap(hour_weekday, cmap="Blues", ax=axs_heatmap)
    axs_heatmap.set_title("Message Heatmap")


def show_date(data_frame):
    
    data_frame['date'] = data_frame['timestamp'].dt.date

    data_frame = data_frame.groupby(['date']).size()
    min_date = data_frame.index.min()
    max_date = data_frame.index.max()
    date_range = pd.date_range(min_date, max_date)
    data_frame.index = pd.DatetimeIndex(data_frame.index)
    data_frame = data_frame.reindex(date_range, fill_value=0)

    # creates plot of note creation by date
    fig_date, axs_date = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    data_frame.plot(ax=axs_date, kind='line', linewidth=1, color='#63abdb', title="Message history", xlabel="Date", ylabel="Count")

def show_person(data_frame):
    
    data_frame = data_frame.groupby(['person']).size()

    fig_person, axs_person = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    person = data_frame.plot(kind='bar', ax=axs_person, title="Messages per personn", xlabel="Person", ylabel="Count", rot=0)
    person.bar_label(person.containers[0])

def show_words(data_frame):
    

    data_frame['words'] = data_frame['message'].str.count(' ').add(1)
    
    print("Average message length: " + str(round(data_frame['words'].mean(), 1))+ " words")

    bins = np.arange(0, data_frame['words'].max()+const.BIN_WIDTH, const.BIN_WIDTH)

    fig_words, axs_words = plt.subplots(figsize=[const.WIDTH,const.HEIGHT])
    data_frame['words'].plot.hist(ax=axs_words, bins=bins)



def show_wordcloud(data_frame):
   
    ignore_list = const.IGNORE_WORDS.split()
    
    data_frame['message'] = data_frame['message'].astype('string')

    text = data_frame['message'].values
    unique_string = (" ").join(text)

    STOPWORDS.update(ignore_list)
    wordcloud = WordCloud(width=1000, height=500, background_color="white").generate(str(unique_string))

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
