def get_date(line):
    return line[line.find('[')+1:line.find(']')]

def get_person(line):
    return line[0:line.find(':')]

def get_message(line):
    return line[line.find(':')+2:]
