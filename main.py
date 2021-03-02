import face_recognition


f = open('config.txt', 'r')
lines = f.readlines()
config = []

for line in lines:
    line = line.split(':')
    config.append(line[1])

face_recognition.face_recognize(config)