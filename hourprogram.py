# -*- coding: utf-8 -*-
"""random practice

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qgE7dpUn7tlbRT6dazSmqfC6OMJfLt4X
"""

currentHour = int(input("Enter the current hour: "))
hoursToAdd = int(input("Enter the number of hours to add: "))
remainder = hoursToAdd%24
finalTime=currentHour+remainder
if finalTime>12:
    x=(12-currentHour)
    k=remainder-x
    print(k)
else:
    print(finalTime)