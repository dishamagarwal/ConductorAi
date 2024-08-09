
from NlpFindNum import findLargestNumber
from SimpleSolution import findSimpleLargestNumber
import time 
from datetime import timedelta

def Main():
    # timer to time runtime
    begin = time.time() 
    file_path = "FY25 Air Force Working Capital Fund.pdf"
    
    NPL_largest_num = findLargestNumber(file_path=file_path)
    print("NPL_largest_num: ", NPL_largest_num)

    # for the simpler solution without language processing libraries
    # largest_num = findSimpleLargestNumber(file_path)
    # print("Simple_largest_num: ", largest_num)

    elapsed = (time.time() - begin)

    print(f"Total runtime of the program is {str(timedelta(seconds=elapsed))}") 

if __name__ == '__main__':
    Main()