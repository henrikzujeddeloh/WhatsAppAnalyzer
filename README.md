# WhatsApp Analyzer
A program to analyze a WhatsApp chat and generate some interesting statistics and visualizations.

## Usage

Export the WhatsApp chat by going to the chat details > Export Chat > Without Media and save it to the `data/` directory in this repo.

Run ´python main.py´ with any arguments of visualizations you want to generate.

A list of possible arguments are listed below.

### Arguments

| Argument | Description |
| --- | --- |
| `--heatmap` | shows heatmap of messages sent per week day and hour |
|`--date` | shows graph of messages sent per day |
|`--person`| shows bar graph of number of messages sent per person |
|`--words` | shows histogram of message word length |

