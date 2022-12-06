# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:00:24 2022

@author: User
"""
from math import sqrt
import matplotlib.pyplot as plt
fileName1 = input('Введіть назву файлу ')
def SortOfArray(data):
    for index in range(0, len(data)):
        min = index
        for comp in range(index + 1, len(data)):
            if data[comp] < data[min]:
                min = comp
        if min != index:
            data[index], data[min] = data[min], data[index]
    return data
def GetData(fileName):
    f = open(fileName, 'r')
    s = f.readline()
    n = int(s)
    arr=[]
    for line in f:
        data = line.split(' ')
        for s in data:
            if s != '':
                arr = arr+[int(s)]
    print(arr)
    return SortOfArray(arr)
n=GetData(fileName1)
output_name = 'output_'+str(len(n))+'.txt'
freqDict = {}
def FreqTable(arr):
    a=[]
    for num in arr:
        if num in freqDict:
            freqDict[num] += 1
        else:
            freqDict[num] = 1
    l=Cumulative(freqDict)
    i=0
    k=0  
    print('Таблиця частот\n')
    for key in freqDict:
        print(f"{key}:{str(freqDict[key])}:{str(l[i])}")
        i=i+1
    with open(output_name, "a") as f:
        f.write('Таблиця частот\n')
        for key in freqDict:
            f.write(f"{key}:{str(freqDict[key])}:{str(l[k])}\n")
            k=k+1

def Cumulative(freqDict):
    l=[]
    l=list(freqDict.values())
    for i in range (1, len(l)):
        l[i]=l[i]+l[i-1]
    return l
def findMedian(arr):
    n=len(arr)
    index =n//2
    if n % 2:
        return arr[index]
    print("Медіана", sum(arr[index-1:index+1])/2)
    h=sum(arr[index-1:index+1])/2
    with open(output_name, "a") as f:
        f.write('Медіанa: '+str(sum(arr[index-1:index+1])/2)+'\n')
def findMode():
    a=list(freqDict.values())
    k=max(a)
    if(k!=1):
        for j in freqDict.keys():
            if(k==freqDict[j]):
                print('Мода вибірки: ', j)
                with open(output_name, "a") as f:
                    f.write(f"Мода вибірки:")
                    f.write(str(j))
def MostViewed(a):
    max_value = []
    maximum = max(a)
    for i in range (1, len(a)+1):
        if (a[i - 1] == maximum):
            max_value.append(i)
    if (len(max_value) == len(a)):
        print('Усі фільми мають однакову кількість переглядів\n')
        with open(output_name, "a") as f:
            f.write('Усі фільми мають однакову кількість переглядів\n')
    elif (len(max_value) == 1):
        print('Найчастіше було переглянуто Фільм №'+str(max_value[0])+'\n')
        with open(output_name, "a") as f:
            line = 'Найчастіше було переглянуто Фільм №'+str(max_value[0])+'\n'
            f.write(line)
    else:
        print('Найчастіше було переглянуто фільми №'.strip())
        with open(output_name, "a") as f:
            line = 'Найчастіше було переглянуто фільми №'.strip()
            f.write(line)
        for i in range (0, len(max_value)):
            if (i != len(max_value) - 1):
                print((str(max_value[i]) + ', ').strip())
                with open(output_name, "a") as f:
                    line = (str(max_value[i]) + ', ').strip()
                    f.write(line)
            else:
                print(max_value[i]+'\n')
                with open(output_name, "a") as f:
                    f.write(max_value[i]+'\n')

def func1(a):   
    x = []
    for i in range (1, len(a) + 1):
        x.append(i)
    fig, axes = plt.subplots(1, 1)
    axes.bar(x, a)
    #plt.show()
    plt.savefig('output_figure_'+str(len(n))+'.png')
def variance():
    data=SortedArray
    n = len(data)
    mean = sum(data)/n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    print("Дисперсія: ", variance)
    print ("Відхилення: ", sqrt(variance))
    with open(output_name, "a") as f:
        f.write("Дисперсія: "+str(variance)+'\n')
        f.write ("Відхилення: "+ str(sqrt(variance))+'\n')
SortedArray = GetData(fileName1)
Median=findMedian(SortedArray)
print(SortedArray)
print(Median)
variance()
FreqTable(SortedArray)
MostViewed(SortedArray)
findMode()
#func(SortedArray)
func1(freqDict.values())
