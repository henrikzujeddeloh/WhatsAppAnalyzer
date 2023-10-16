import matplotlib.pyplot as plt

from modules.create_dataframe import create_df
import modules.constants as const
import modules.input as input
import modules.output as output

arguments = input.parse_arguments()

df = create_df(const.DATA_DIR)

print(str(len(df.index)) + " messages sent")

next = ''
while(next != 'q'):
    if arguments.heatmap:
        output.show_heatmap(df)
    if arguments.date:
        output.show_date(df)
    if arguments.person:
        output.show_person(df)
    if arguments.words:
        output.show_words(df)
    if arguments.wordcloud:
        output.show_wordcloud(df)


    #print(df)
    plt.show()

    next = input.select_next_visualization()
    arguments = input.update_args(next, arguments)
