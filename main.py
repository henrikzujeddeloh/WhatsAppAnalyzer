import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_DIR = "data/"
FILE_NAME = "_chat.txt"

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

df = create_df(DATA_DIR)

print(df)

