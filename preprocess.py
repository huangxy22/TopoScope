import os
import datetime

start=datetime.datetime.now()

directory = r'./data/RIB/dump2022/'
filenames=os.listdir(directory)
output = []

cnt = 0
sum = len(filenames)
for filename in filenames:
    fulldir = directory+filename
    file = open(fulldir,'r')
    text = file.read()
    file.close()
    text = text.split('\n')
    for line in text:
        line = line.split('|')
        if len(line) < 7:
            continue
        aspath = line[6]
        prefix = line[5]
        if '{' in aspath or '(' in aspath:
            continue
        if ":" not in prefix:
            #output.append(aspath.replace(' ', '|'))
            output.append(aspath.replace(' ', '|') + '&' + prefix)
    cnt += 1
    print(filename,"complete",cnt/sum,"time:",(datetime.datetime.now()-start))

output_file = open("aspaths_2022.txt",'w')
output_file.write('\n'.join(output))