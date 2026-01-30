f = open("score.txt", 'r')
line = f.readline()
s = line.split(':')[1].strip()
print(s)