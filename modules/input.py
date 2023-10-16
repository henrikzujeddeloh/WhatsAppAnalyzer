import argparse


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("--heatmap", help="output heatmap of message send time", action="store_true")
    parser.add_argument("--date", help="output history of messsage send time", action="store_true")
    parser.add_argument("--person", help="output messages sent by person", action="store_true")
    parser.add_argument("--words", help="output average words per message by person", action="store_true")
    parser.add_argument("--wordcloud", help="outputs wordcloud of all words written", action="store_true")

    args = parser.parse_args()

    return args


def select_next_visualization():
    print("Select a visualization to output (1-5) or 'q' to quit.")
    selection = input("1 - heatmap\n2 - date\n3 - person\n4 - words\n5 - wordcloud\n")
    
    return selection


def update_args(selection, args):

    args.heatmap = False
    args.date = False
    args.perosn = False
    args.words = False
    args.wordcloud = False

    if selection == '1':
        args.heatmap = True
    if selection == '2':
        args.date = True
    if selection == '3':
        args.person = True
    if selection == '4':
        args.words = True
    if selection == '5':
        args.wordcloud = True

    return args
