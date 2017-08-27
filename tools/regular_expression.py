import re
import os
import string

def myregular_expression():
    test = "jason 1 . 010-78639493. ? 456"
    pattern1 = re.compile('(^jason)[\.\s\w\d\-]*([$6])')
    pattern2 = re.compile('[\d\-\d\w\.\s]+[$?]')
    pattern3 = re.compile('[\w\s\-\.\d]*[$?]')
    result1 = pattern1.search(test)
    result2 = pattern2.search(test)
    result3 = pattern3.search(test)
    print result1.group(0)
    print result1.group(1)
    print result1.group(2)
    print result2.group(0)
    print result3.group(0)


def main():
    myregular_expression()

if __name__ == '__main__':
    main()
