'''
You are given the array paths, where paths[i] = [cityA, cityB] means there exists a direct path going from cityA to cityB.
Return the destination city - the city without any path outgoing to another city.
'''



class Solution:
    def destCity(self, paths: List[List[str]])-> str: # Defines a method destCity within the Solution class. It takes a list of lists (paths) as an argument and returns a string.
        outgoing_count = {} # Initializes an empty dictionary to keep track of the number of outgoing paths for each city.
        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)

        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city
