from FileParser import *

print "\ntesting file_obj creation\n"
test_fp = FileParser("TRACKING.txt")

print "\ntesting sum column\n"
print test_fp.sum_column(5)
print test_fp.sum_column(6)
print test_fp.sum_column(7)

print "\ntesting average column\n"
print test_fp.average_column(5)
print test_fp.average_column(6)
print test_fp.average_column(7)
 
print "\ntesting variance column\n"
print test_fp.variance_column(5)
print test_fp.variance_column(6)
print test_fp.variance_column(7)
  
print "\ntesting std dev column\n"
print test_fp.std_dev_column(5)
print test_fp.std_dev_column(6)
print test_fp.std_dev_column(7)
