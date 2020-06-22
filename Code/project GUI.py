from tkinter import *
import tkinter as tk
import random
w = tk.Tk()
w.title ("Fare Guide")
w.geometry("800x300")

fr = ""
towards = ""


def dijkstra (graph, fromm):
    import math
    dic={}
    for node in graph:
        if node == fromm:
            dic[node] = [node, 0]
        else:
            dic[node] = ['',math.inf]

    visited = []
    while len(visited)<len(graph):
        current_node= ''
        small = math.inf
        for node in dic:
            if node not in visited and dic[node][1] < small:
                small = dic[node][1]
                current_node = node

        visited.append(current_node)
        for n in graph[current_node]:
            node=n[0]
            if node not in visited:
                weight = n[1]
                if dic[node][1] > small + weight:
                    dic[node][1] = small + weight
                    dic[node][0] = current_node
    return dic

def shortest(G):
    global fr,towards
    cost = 0
    time = 0 

    dis = dijkstra(G,fr)
    x = towards

    lst = []

    while x!=fr:
        lst.append([dis[x][0]]+[x]+[dis[x][1]])
        x = dis[x][0]

    lst.append(fromm)
    lst.remove(lst[-1])
    lst = lst[::-1]


    drivers = ['Akram', 'Shohaib', 'Anzar', 'Salman', 'Ali', 'Umer', 'Humayn', 'Chengez']
    driver = random.choice(drivers)

    vehicle = str(veh.get())
    sum = lst[-1][-1]

    if vehicle == 'car':
        cost = sum * 15
        time = sum * 2
    elif vehicle == 'bike':
        cost = sum * 5
        time = sum * 4
    
    maps = []
    for x in lst:
        maps.append(x[0])
    maps.append(towards)
    maps = " --> ".join(maps)
    
    tk.Label(w,text = 50*'*').pack()
    tk.Label(w,text = 'MAPS:'+maps).pack()
    tk.Label(w,text = 'Kilometers travelled are ' + str(sum) + " KM.").pack()
    tk.Label(w,text = 'Your minimun fare will be ' + str(cost) + 'PKR.').pack()
    tk.Label(w,text = 'Arrival will be in ' + str(time) + ' Minutes.').pack()
    tk.Label(w,text = 'Your driving captain is ' + driver).pack()
    tk.Label(w,text = 'Happy Riding :D').pack()

    tk.Label(w,text = 50*'*').pack()


G = {
 'Clifton teen talwar': [('Garden', 8.3), ('DHA Phase 5',3.9),('Light House',3.9) , ('Korangi',10.2)],
 'Saddar': [('Garden', 3.4), ('Shahrah-e-Faisal', 6.8)],
 'Shahrah-e-Faisal': [('Saddar',6.8),('DHA Phase 5',8)],
 'Garden': [('Clifton teen talwar', 8.3),('Saddar',3.4) , ('Bahadurabad', 5.5), ('Gulshan e Iqbal', 9), ('Light House',4)],
 'DHA Phase 5': [('Clifton teen talwar', 3.9),('Shahrah-e-Faisal',8), ('Korangi',9.9),('Light House',7.5)],
 'Gulshan e Iqbal': [('Bahadurabad', 8) ,('Garden',9)],
 'Bahadurabad': [('Gulshan e Iqbal', 8),('Garden',5.5),('Light House',7.3)],
 'Korangi': [('DHA Phase 5', 9.9),('Clifton teen talwar', 10.2)],
 'Light House': [('Clifton teen talwar', 3.9), ('DHA Phase 5', 7.5),('Garden',4),('Bahadurabad',7.3)]
 }
def start(event):
    global fr
    fr = str(fromm.get())

def end(event):
    global towards 
    towards = str(to.get())    
    tk.Button(command = shortest(G)).pack()

#def vehicle(event):
 #   global veh
  #  veh = str(vh.get())    
   # 

l = tk.Label (w, text = "Fare Estimator").pack()


from tkinter.ttk import *
from tkinter import LEFT,RIGHT,CENTER

tk.Label (w, text = 'From').pack(side=LEFT)
fromm = Combobox(w)
fromm['values'] = ('Clifton teen talwar', 'Saddar', 'Shahrah-e-Faisal', 'Garden', 'DHA Phase 5', 'Gulshan e Iqbal', 'Bahadurabad', 'Korangi', 'Light House')
fromm.pack(side=LEFT)
fromm.bind("<<ComboboxSelected>>",start)

tk.Label (w, text = 'to').pack(side=RIGHT)
to = Combobox(w)
to['values'] = ('Clifton teen talwar', 'Saddar', 'Shahrah-e-Faisal', 'Garden', 'DHA Phase 5', 'Gulshan e Iqbal', 'Bahadurabad', 'Korangi', 'Light House')
to.pack(side=RIGHT)
to.bind("<<ComboboxSelected>>",end)

'''
tk.Label (w, text = 'type').pack()
vh = Combobox(w)
vh['values'] = ('Bike','car')
vh.pack()
vh.bind("<<ComboboxSelected>>",vehicle)
'''

veh = tk.StringVar()
veh.set('bike')

rb = tk.Radiobutton(w, text = 'Car', variable = veh, value = 'car').pack()
rb2 = tk.Radiobutton(w, text = 'Bike', variable = veh, value = 'bike').pack()

w.mainloop()
