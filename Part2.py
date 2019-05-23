# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:29:53 2019

@author: Patanian10
"""

#finding the shortest distance 
for i in range(1000):
    print('The possible shortest total distance is %5.2f' % measure_path(population[0]))
    draw_path(population[0])
    performance_list.append(measure_path(population[0]))
    plt.plot(performance_list,'.-')
    plt.show() 
    population = multiply(population, 10)   

city = population[0]
city = np.delete(city, 81)
for i in(city):
    if city [i] == 5:
        ankara = i
route = np.hstack ((city[ankara:], city[:ankara]))
route = np.append(route,route[0])
print ("The shortest route started from Ankara defined by number of index: ",route)   