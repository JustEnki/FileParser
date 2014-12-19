file = open("Test.txt", "r").read()
file_lines = file.split('\n')
HEADERS = file_lines[0]
HEADERS = HEADERS.split(',')
dict = {}
for head in HEADERS:
  dict[head] = []

for line in file_lines[1:]:
  print line.split(',')
  for i in range(len(file_lines)-1):
    for j in range(len(dict)):
      print line[i][j]
      
      
