from datetime import datetime
def get_time():
    with open('data10.txt','r') as fp:
        content = fp.readlines()
    return content
def timesort():
    lt1 = get_time()
    lt2 = []
    for i in lt1:
        dt = datetime(int(i[6:10]),int(i[3:5]),int(i[0:2]),int(i[11:13]),int(i[14:16]),int(i[17:19]))
        lt2.append(dt.timestamp())
    lt2.sort()
    lt3 = []
    for i in lt2:
        dt1 = datetime.fromtimestamp(i)
        lt3.append(dt1.strftime('%d/%m/%Y %H:%M:%S'))
    fp = open("data10-1.txt",'w')
    for i in lt3:
        fp.write(i + '\n')
    print("data sorted finish in data10-1.txt")
    fp.close()
if __name__ == '__main__':
    timesort()