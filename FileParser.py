import fileinput
import os.path

class FileParser(object):
  """The class will parse any txt file given to it and convert the individual data points into their appropriate data type

  This class's methods will calculate different statistical values
  I will also attempt to have this file pivot by certain data points
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
   
  def save_file(self, func, arg, col):
    nw_file_name = raw_input("Name the new file --> ") #Names new file name
    nw_file = open(nw_file_name + ".txt", "w") #opens new file for writing`
    for line in self.lines: #starts for loop that writes out each line
      nw_file.write(str(line)[1:-1] + '\n') #converts the lists into strings and removes the braces
    nw_file.close()
    
  def sum_column(self, col): #col must be an integer
    returning_value = 0
    for line in self.lines:
      try:
        returning_value = line[col] + returning_value
      except:
        pass
    return returning_value

  def average_column(self, col):
    return self.sum_column(col) / float( len( self.lines))

  def variance_column(self, col):
    ret_val = 0
    avg = self.average_column(col)
    for line in self.lines:
      try:
        ret_val = (avg - line[col])**2 + ret_val
      except:
        pass
    return ret_val/len(self.lines)

  def std_dev_column(self, col):
    return self.variance_column(col)**0.5

  def pivot(self, func, arg, date):
    """This method will select a column and pivot the data by that column, it will then compute the different statistics based on that particular data point. This will be tested using the Tracking.txt file.
    """
    temp_dict = {}
    for line in self.lines:
      #line[date] gives me the date of the line, I want this to be the key for temp_dict
      temp_dict[line[date]] = 0
    for line in self.lines:
      #line[date] gives me the date of the line, I want this to be the key for temp_dict
      temp_dict[line[date]] = temp_dict[line[date]] + func(arg)
 
if __name__ == "__main__":

  print "\ntesting file_obj creation\n"
  test_fp = FileParser("TRACKING.txt")
  
  print "\ntesting save file\n"
  print test_fp.save_file(test_fp.std_dev_column, 6, 0)
