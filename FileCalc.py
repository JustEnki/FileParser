import FileParser

class FileCalc(object):
  """This class will contain methods to manipulate and calculate values from a FileParser object.
  
  Need to identify a unique key so that the calculations use that as the basis, create method that changes unique key
  
  IDEA: What if I had a header and made those into a dictionary and made every data point a part of a list within that dictionary? Let's try it out.
  """
  def __init__(self, file, unique_key = 0):
    self.fp = FileParser.FileParser(file)
    self.unique_key = unique_key
    
  def change_key(self, nw_key):
    try:
      self.unique_key = nw_key
      for line in self.fp:
        x = line[self.unique_key]
    except:
      pass
  
  
  def sum_column(self, col): 
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
 