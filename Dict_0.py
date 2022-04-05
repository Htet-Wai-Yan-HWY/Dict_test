

room = [ {'Name': 'Aung Ko' , 'Age' : 7, 'Gender' : 'male'},
{'Name': 'Ko Ko' , 'Age' : 8, 'Gender' : 'male'},
{'Name': 'Aye Aye' , 'Age' : 7, 'Gender' : 'female'},
{'Name': 'Htet Htet' , 'Age' : 8, 'Gender' : 'female'},
{'Name': 'Win Aung' , 'Age' : 7, 'Gender' : 'male'},
{'Name': 'Mya Mya' , 'Age' : 7, 'Gender' : 'female'},
]

p1,p2,p3,p4,p5 = room[0],room[2],room[3],room[4],room[5]


for i in room:
    if i["Gender"] == 'male':
        print(i)
    else:
        print("Female")