class FileParser(object):
  """The class will parse any txt file given to it and convert the individual data points into their appropriate data type

  So far this class converts numerical data. It does not yet convert datetime data, but leaves it as a string.
  
  This should probably be saved to a shelve
  """
  def __init__(self, file_obj):
    self.file_obj = open(file_obj,"r")
    self.file_read = self.file_obj.read()
    self.file_lines = self.file_read.split('\n')
    self.lines = []
    for line in self.file_lines:
      line = line.split(',')
      for item in range(len(line)):
        try:
          line[item] = int(line[item])
        except:
          try:
            line[item] = float(line[item])
          except:
            try:
              line[item] = line[item][:line[item].index(' ')]
            except:
              pass
      self.lines.append(line)
   
  def save_file(self):
  """This file saves the data from the file as a new file.
  
  This is useful for when I want to make operations on the data and then save them back to a new file"""
    nw_file_name = raw_input("Name the new file --> ") #Names new file name
    nw_file = open(nw_file_name + ".txt", "w") #opens new file for writing`
    for line in self.lines: #starts for loop that writes out each line
      nw_file.write(str(line)[1:-1] + '\n') #converts the lists into strings and removes the braces
    nw_file.close()
    

if __name__ == "__main__":

  print "\ntesting file_obj creation\n"
  test_fp = FileParser("Test.txt")
  
  print "\ntesting save file\n"
  print test_fp.save_file()
