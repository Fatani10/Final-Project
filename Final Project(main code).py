# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:50:26 2019

@author: Patanian10
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd 

#part 1 store as NumPy array 
coordinates = xlrd.open_workbook(r"C:\Users\Patanian10\Desktop\Final\Coordinates.xlsx")
distancematrix = xlrd.open_workbook(r"C:\Users\Patanian10\Desktop\Final\distancematrix.xls")

note1 = coordinates.sheet_by_index(0)
note2 = distancematrix.sheet_by_index(0)

n = 81
distance_list = []
performance_list = []

#calculate distance matrix
for i in range(n): 
    for j in range(n):
        value = note2.cell_value(i+3,j+2)
        distance_list.append(value)

#reshape the distance_list into square matrix 
value = np.arange(0,6562,81)
for i in range(n):
    distance_list[value[i] + i] = 0        
distance_matrix = np.reshape(distance_list,(81,81)) #81 represented cities in Turkey

list_of_cities = []
vertical_coordinate  = []
horizontal_coordinate  = []

#matrix Coordinate
for i in range (n) : 
    city = note1.cell_value(i+1, 1) 
    v_coordinate = note1.cell_value(i+1, 2)
    h_coordinate = note1.cell_value(i+1, 3)
    
    list_of_cities.append(city)
    vertical_coordinate.append(v_coordinate)
    horizontal_coordinate.append(h_coordinate)

matrix_coordinates = np.zeros((81, 2))
for i in range(81):
    matrix_coordinates[i][0] = vertical_coordinate[i]
    matrix_coordinates[i][1] = horizontal_coordinate[i]
    
for i in range(n) :
    plt.plot((horizontal_coordinate[i]), (vertical_coordinate[ i ]), '.-')

#trip
trip_list = []
for i in range(n):
    trip = distance_matrix[i,:n]
    trip_list.append(trip)

shortest_trip = [] 
for i in range(n):
    tr = np.sort(trip_list[i])
    shortest_trip.append(tr)
#print(shortest_trip)

#part 4 genetic algorithm 
def get_a_path(n):
    rand_path = np.arange(n)
    np.random.shuffle(rand_path)
    rand_path = np.append(rand_path,rand_path[0])
    return rand_path

def measure_path(path):
    def distance(i, j):
        return distance_matrix[i][j]
    total_distance = 0
    for i,j in zip(path[:-1], path[1:]):
        dist = distance(i,j)
        total_distance = total_distance + dist
    return total_distance

def draw_path(path0):
    for i,j in zip(path0[:-1],path0[1:]):
        plt.plot([matrix_coordinates[i][1],matrix_coordinates[j][1]]
        ,[matrix_coordinates[i][0],matrix_coordinates[j][0]],'-o')
    plt.show()

def crossover(path1, path2):
    
    path1 = path1[:-1]
    path2 = path2[:-1] #using these two path to creat path 3
    rand_int = np.random.randint(0,n)
    path3 = np.hstack((path1[:rand_int], path2[rand_int:])) #creating children 
    unique, counts = np.unique(path3, return_counts=True)
    dictionary = dict(zip(unique, counts))
    replacewith = []
    for i in dictionary:
        if dictionary[i] == 2:
            replacewith.append(i)    
    if len(set(path3))!=len(set(path2)):
        missing = list(set(path1)-set(path3))
#        print(missing)
        for i,j in zip(replacewith,missing):
            if np.random.rand() > 0.5:
                index = np.where(path3 == i)[0][0]
            else:
                index = np.where(path3 == i)[0][1]            
            path3[index] = j
  
#mutaion 
    if np.random.rand() > 0.1:
        a, b = np.random.randint(0, n, 2)
        path3[a], path3[b] = path3[b], path3[a]
    path3 = np.append(path3, path3[0]) 
    return path3
# in mutation 4 funcion need to be defined
def get_fitness_population(population):
    perf_list = []
    for i in population:
        perf_list.append(measure_path(i))
    return np.array(perf_list)

def sort_population(population):
    performance = get_fitness_population(population)
    i = np.argsort(performance)
    return population[i]

def create_initial_population(n):
    population_list = []
    cities_in_Turkey = 81 
    for i in range(n):   
        pop = get_a_path(cities_in_Turkey)
        population_list.append(pop)
    population_list = np.array(population_list)
    population_list = sort_population(population_list)
    return population_list

population  = create_initial_population(100)

def multiply(population, n):
    population = population[:n]
    new_population_list = []
    for i in population:
        for j in population:
            new_population_list.append(crossover(i, j))
    new_population_list = np.array(new_population_list)
    new_population_list = sort_population(new_population_list)
    return new_population_list

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