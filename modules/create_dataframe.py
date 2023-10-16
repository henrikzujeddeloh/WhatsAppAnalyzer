import os
import pandas as pd
from progressbar import ProgressBar, Percentage, Bar

import modules.constants as const
import modules.utils as utils


def create_df(path):

    data_frame = pd.DataFrame(columns=('timestamp', 'person', 'message'))

    dirname = os.getcwd()
    directory = os.path.join(dirname, path)
    found = False
    for filename in os.listdir(directory):
        if filename == const.FILE_NAME:
            found = True
            f = os.path.join(directory, filename)
            with open(f, "r") as file:
                i = 0
                print("Reading file...")
                num_lines = sum(1 for line in open(f))
                pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=num_lines).start()
                for line in file:
                        stripped_line = line.strip()
                        if not stripped_line == "" and stripped_line[0] == '[' and stripped_line.find("omitted") == -1:
                            date = pd.to_datetime(utils.get_date(stripped_line), format='%d.%m.%y, %H:%M:%S')
                            person = utils.get_person(stripped_line[21:])
                            message = utils.get_message(stripped_line[21:])
                        elif not stripped_line == "" and stripped_line.find("omitted") == -1:
                            date = pd.to_datetime(data_frame.loc[i-1]['timestamp'], format='%d.%m.%y, %H:%M:%S')
                            person = data_frame.loc[i-1]['person']
                            message = stripped_line
                        data_frame.loc[i] = [date, person, message]
                        #print(data_frame.loc[i])
                        i += 1
                        pbar.update(i)
                pbar.finish()
    if(found == False):
        print("Chat file not found!\nMake sure '_chat.txt' is located in data folder!")
    return data_frame
