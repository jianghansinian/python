#!/bin/bash
import os, re
import time
import string
import numpy as np
import matplotlib.pyplot as plt

def countProcessMemoey(processName, data):
    #pattern = re.compile('[^jason\s+][\d{3,5}\s+][\d\.\d\s+][\d\.\d][\d{3,6}\s+][\d{3,5}][$\s]')
    pattern1 = re.compile('[^jason][\w\s\-\.\d]*pts')
    pattern2 = re.compile('[^jason][\w\s\-\.\d]*[$?]')
    #pattern = re.compile('[\w\s\-\.\d]*[$?]')
    cmd = 'ps aux|grep ' + processName
    result = os.popen(cmd).read()
    resultList = result.split("jason")
    print 22222
    print result
    print 22222

    for Line in resultList:
        #srcLine = "".join(Line.split('jason'))
        #if len(srcLine) == 0:
        #    print 0
        #    break
        temp1 = pattern1.search(Line)
        temp2 = pattern2.search(Line)
        if temp1 == None:
            print 'pattern1 none'
        else: 
            aim1 = temp1
            string = re.split('\s+',aim1.group(0))
            data.append(int(string[len(string) - 2]))
            print temp1.group(0)
            print string[len(string) - 2]
        if temp2 == None:
            print 'pattern2 none'
        else:
            aim2 = temp2
            string = re.split('\s+',aim2.group(0))
            data.append(int(string[len(string) - 2]))
            print temp2.group(0)
            print string[len(string) - 2]
        if temp1 == None and temp2 == None:
            print 'none'

if __name__ == '__main__':
    ProcessName = 'firefox'
    now = time.time()
    data = [0]
    while time.time() - now < 10:
        countProcessMemoey(ProcessName, data)
        time.sleep(0.5)
    print data
    plt.plot(data)
    plt.show()
