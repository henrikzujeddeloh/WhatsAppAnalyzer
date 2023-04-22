import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_DIR = "data/"
FILE_NAME = "_chat.txt"

BIN_WIDTH = 5

WIDTH = 10
HEIGHT = 5

def get_date(line):
    return line[line.find('[')+1:line.find(']')]

def get_person(line):
    return line[0:line.find(':')]

def get_message(line):
    return line[line.find(':')+2:]

def create_df(path):

    data_frame = pd.DataFrame(columns=('timestamp', 'person', 'message'))

    dirname = os.getcwd()
    directory = os.path.join(dirname, path)
    for filename in os.listdir(directory):
        if filename == FILE_NAME:
            f = os.path.join(directory, filename)
            with open(f, "r") as file:
                i = 0
                for line in file:
                        stripped_line = line.strip()
                        if not stripped_line == "" and stripped_line[0] == '[':
                            date = pd.to_datetime(get_date(stripped_line), format='%d.%m.%y, %H:%M:%S')
                            person = get_person(stripped_line[21:])
                            message = get_message(stripped_line[21:])
                        elif not stripped_line == "":
                            date = pd.to_datetime(data_frame.loc[i-1]['timestamp'], format='%d.%m.%y, %H:%M:%S')
                            person = data_frame.loc[i-1]['person']
                            message = stripped_line

                        data_frame.loc[i] = [date, person, message]
                        #print(data_frame.loc[i])
                        i += 1
    return data_frame

def show_heatmap(data_frame):
    
    data_frame['weekday'] = data_frame['timestamp'].dt.day_name()

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data_frame['weekday'] = pd.Categorical(data_frame['weekday'], categories=week_days, ordered=True)
    data_frame = data_frame.sort_values('weekday')

    data_frame['hour'] = data_frame['timestamp'].dt.hour

    hour_weekday = data_frame.groupby(["weekday", "hour"]).size().unstack()

    fig_heatmap, axs_heatmap = plt.subplots(figsize=[WIDTH,HEIGHT])
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
    fig_date, axs_date = plt.subplots(figsize=[WIDTH,HEIGHT])
    data_frame.plot(ax=axs_date, kind='line', linewidth=1, color='#63abdb', title="Message history", xlabel="Date", ylabel="Count")

def show_person(data_frame):
    
    data_frame = data_frame.groupby(['person']).size()

    fig_person, axs_person = plt.subplots(figsize=[WIDTH,HEIGHT])
    person = data_frame.plot(kind='bar', ax=axs_person, title="Messages per personn", xlabel="Person", ylabel="Count", rot=0)
    person.bar_label(person.containers[0])

def show_words(data_frame):
    

    data_frame['words'] = df['message'].str.count(' ').add(1)
    
    print("Average message length: " + str(round(data_frame['words'].mean(), 1))+ " words")

    bins = np.arange(0, data_frame['words'].max()+BIN_WIDTH, BIN_WIDTH)

    fig_words, axs_words = plt.subplots(figsize=[WIDTH,HEIGHT])
    data_frame['words'].plot.hist(ax=axs_words, bins=bins)


parser = argparse.ArgumentParser()
parser.add_argument("--heatmap", help="output heatmap of message send time", action="store_true")
parser.add_argument("--date", help="output history of messsage send time", action="store_true")
parser.add_argument("--person", help="output messages sent by person", action="store_true")
parser.add_argument("--words", help="output average words per message by person", action="store_true")
args = parser.parse_args()



df = create_df(DATA_DIR)

print(str(len(df.index)) + " messages sent")

if args.heatmap:
    show_heatmap(df)
if args.date:
    show_date(df)
if args.person:
    show_person(df)
if args.words:
    show_words(df)

#print(df)
plt.show()
