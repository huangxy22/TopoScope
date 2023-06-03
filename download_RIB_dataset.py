import os

command = "mkdir data/RIB/2021ripe"
os.system(command)
for i in range(0,30):
    command = "wget https://data.ris.ripe.net/rrc"+ str(i).zfill(2) +"/2021.04/bview.20210430.1600.gz  -O ./data/RIB/2021ripe/rrc"+ str(i).zfill(2)+"_20210430.gz"
    os.system(command)
    # 下面两行似乎有问题
    #command = "bgpdump -m rrc"+ str(i).zfill(2) +"_20210430.gz > rrc"+ str(i).zfill(2) +"_20210430.txt"
    #print(command)

print("ripe dataset downloaded!")

link_file = open('./data/RIB/link_list.txt','r')
link_list = link_file.readlines()
link_file.close()
command = "mkdir data/RIB/2021routeviews"
os.system(command)
for link_name in link_list:
    link_name = link_name.strip('\n').split(',')
    #print(link_name)
    command = "wget "+ link_name[0] +" -O ./data/RIB/2021routeviews/"+ link_name[1]+".bz2"
    os.system(command)
    #command = "bgpdump -m "+ link_name[1]+".bz2 > "+ link_name[1]+".txt"
    #print(command)
print("routeviews dataset downloaded!")