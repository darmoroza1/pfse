# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:01:05 2022

@author: User
"""
import math
import numpy as np
import matplotlib.pyplot as plt
arr = []
arr.append([])
arr.append([])
name = input('Введіть назву файлу: ')
file = open(name, mode="r")
i = int(0)
m = int(-1)
with open(name, "r") as file:
    for line in file.readlines():
        if (i > 0):
            arr[0].append(float(line.split('	')[0].split(',')[0]+'.'+line.split('	')[0].split(',')[1]))
            arr[1].append(int(line.split('	')[1]))
        else:
            m = int(line)
        i = i + 1
file.close()
output_name = 'output'+str(m)+'.txt'
def task1():
    plt.scatter(arr[0], arr[1], label = 'Діаграма розкиду даних')
    with open(output_name, "a") as f:
        f.write('Завдання 1\n')
        b = float(0)
        sum = float(0)
        avX = float(0)
        avY = float(0)
        for i in range(0, len(arr)):
            avX = avX + arr[0][i]
            avY = avY + arr[1][i]
        avX = avX/m
        avY = avY/m
        for i in range(0, len(arr)):
            sum = sum + (arr[0][i]-avX)*(arr[1][i]-avY)
        sum2 = float(0)
        for i in range(0, len(arr)):
            sum2 = sum2 + (arr[0][i] - avX)*(arr[0][i] - avX)
        b = (sum)/sum2
        a1 = avY - b*avX
        if (b > 0):
            f.write('Тренд позитивний\n')
        elif (b < 0):
            f.write('Тренд негативний\n')
        else:
            f.write('Немає тренду\n')
        x = np.arange(0, 10)
        y = a1 + b * x
        plt.plot(x, y, lw=4, color = 'orange', label = 'Лінія тренду')
        f.write('\n')
def task2():
    with open(output_name, "a") as f:
        avX = float(0)
        avY = float(0)
        for i in range(0, len(arr)):
            avX = avX + arr[0][i]
            avY = avY + arr[1][i]
        avX = avX/m
        avY = avY/m
        f.write('Завдання 2\n')
        f.write('Центр ваги: G(' + str(round(avX, 3)) + ', ' + str(avY) + ')\n')
        f.write('Коваріація: ')
        cov = float(0)
        for i in range(0, m):
            cov = cov + ((arr[0][i]-avX)*(arr[1][i]-avY))
        cov = round(cov/m, 3)
        f.write(str(cov) + '\n')
        f.write('\n')
        varx = float(0)
        for i in range(0, m):
            varx = varx + (arr[0][i]*arr[0][i]-avX*avX)
        varx = varx/m
        b1 = cov/varx
        b = avY - b1*avX
        x = np.arange(0, m)
        y = b + b1 * x
        #plt.plot(x, y, lw=1, color = 'red', label = 'Лінія регресії')
def task3():
    with open(output_name, "a") as f:
        avX = float(0)
        avY = float(0)
        for i in range(0, len(arr)):
            avX = avX + arr[0][i]
            avY = avY + arr[1][i]
        avX = avX/m
        avY = avY/m
        cov = float(0)
        for i in range(0, m):
            cov = cov + ((arr[0][i]-avX)*(arr[1][i]-avY))
        cov = round(cov/m, 3)
        b = float(0)
        sum = float(0)
        varX = float(0)
        for i in range(0, m):
            varX = varX + (arr[0][i]*arr[0][i]-avX*avX)
        varX = varX/m
        b1 = cov/varX
        for i in range(0, len(arr)):
            sum = sum + (arr[0][i]-avX)*(arr[1][i]-avY)
        sum2 = float(0)
        for i in range(0, len(arr)):
            sum2 = sum2 + (arr[0][i] - avX)*(arr[0][i] - avX)
        b = (sum)/sum2
        f.write('Завдання 3\n')
        f.write('Рівняння лінії регресії: y = ' + str(round(b1, 3)) + 'x + ' + str(round(b, 3)) + '\n')
        f.write('\n')
        f.write('Завдання 4\n')
        f.write('Коефіцієнт кореляції між даними: ')
        sx = float(0)
        sy = float(0)
        for i in range(0, m):
            sx = sx + (arr[0][i]-avX)*(arr[0][i]-avX)
        sx = sx/(m)
        sx = math.sqrt(sx)
        for i in range(0, m):
            sy = sy + (arr[1][i]-avY)*(arr[1][i]-avY)
        sy = sy/(m)
        sy = math.sqrt(sy)
        r = cov/(sx*sy)
        f.write(str(round(r, 3)))
        f.write('\n')
        r0 = math.sqrt(3) / 2
        if r == 1 or r == -1:
            f.write("Точки лежать на лінії регресії")
            f.write('\n') 
        elif r > r0 or r < -r0:
            f.write("Між даними існує сильна лінійна залежність")
            f.write('\n')
        elif r == 0:
            f.write("Дані лінійно незалежні")
            f.write('\n\n')
        else:
            f.write("Між даними існує слабка лінійна залежність")
            f.write('\n')        
        if r < 0:
            f.write("Залежність є негативною")
            f.write('\n\n')
        elif r > 0:
            f.write("Залежність є позитивною")
            f.write('\n\n')


task1() 
task2() 
task3()
plt.legend()
plt.grid(True)
plt.savefig('output_figure_'+str(m)+'.png')