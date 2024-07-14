# 6.0002 Problem Set 2 Fall 2020
# Graph Optimization
# Name: Joy Bhattacharya
# Collaborators:
# Time: 

#
# Finding shortest paths to drive from home to work on a road network
#

from graph import DirectedRoad, Node, RoadMap


# PROBLEM 2: Building the Road Network
#
# PROBLEM 2a: Designing your Graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the times
# represented?
#
#
#


# PROBLEM 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a road map (graph).

    Parameters:
        map_filename : String
            name of the map file

    Assumes:
        Each entry in the map file consists of the following format, separated by spaces:
            src_node dest_node travel_time road_type

        Note: mountain road types always are uphill in the source to destination direction and
              downhill in the destination to the source direction. Downhill travel takes
              half as long as uphill travel. The travel_time represents the time to travel 
              from source to destination (uphill).

        e.g.
            N0 N1 10 interstate
        This entry would become two directed roads; one from 'N0' to 'N1' on an interstate highway with 
        a weight of 10, and another road from 'N1' to 'N0' on an interstate using the same weight.

        e.g. 
            N2 N3 7 mountain 
        This entry would become to directed roads; one from 'N2' to 'N3' on a mountain road with 
        a weight of 7, and another road from 'N3' to 'N2' on a mountain road with a weight of 3.5.

    Returns:
        a directed road map representing the inputted map
    """
    pass # replace with your code

# PROBLEM 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out after testing

# road_map = load_map("maps/test_load_map.txt") 



# PROBLEM 3: Finding the Shortest Path using Optimized Search Method



# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:


# PROBLEM 3b: Implement find_optimal_path
def find_optimal_path(roadmap, start, end, restricted_roads, has_traffic=False):
    """
    Finds the shortest path between nodes subject to constraints.

    Parameters:
    roadmap - RoadMap
        The graph on which to carry out the search
    start - Node
        node at which to start
    end - Node
        node at which to end
    restricted_roads - list[strings]
        Road Types not allowed on path
    has_traffic - boolean
        flag to indicate whether to get shortest path during heavy or normal traffic 

    Returns:
    A tuple of the form (best_path, best_time).
        The first item is the shortest-path from start to end, represented by
        a list of nodes (Nodes).
        The second item is an number(float), the length (time traveled)
        of the best path.

    If there exists no path that satisfies constraints, then return None.
    """

    raise NotImplementedError # replace with your code

# PROBLEM 4a: Implement optimal_path_no_traffic
def optimal_path_no_traffic(filename, start, end):
    """
    Finds the shortest path from start to end during ideal traffic conditions.

    You must use find_optimal_path and load_map.

    Parameters:
    filename - name of the map file that contains the graph
    start - Node, node object at which to start
    end - Node, node object at which to end
    
    Returns:
    list of Node objects, the shortest path from start to end in normal traffic.
    If there exists no path, then return None.
    """
    raise NotImplementedError # replace with your code

# PROBLEM 4b: Implement optimal_path_restricted
def optimal_path_restricted(filename, start, end):
    """
    Finds the shortest path from start to end when local roads and mountain roads cannot be used.

    You must use find_optimal_path and load_map.

    Parameters:
    filename - name of the map file that contains the graph
    start - Node, node object at which to start
    end - Node, node object at which to end
    
    Returns:
    list of Node objects, the shortest path from start to end given the aforementioned conditions,
    If there exists no path that satisfies constraints, then return None.
    """
    raise NotImplementedError # replace with your code
    

# PROBLEM 4c: Implement optimal_path_heavy_traffic
def optimal_path_heavy_traffic(filename, start, end):
    """
    Finds the shortest path from start to end in heavy traffic,
    i.e. when local roads take twice as long. 

    You must use find_optimal_path and load_map.

    Parameters:
    filename - name of the map file that contains the graph
    start - Node, node object at which to start
    end - Node, node object at which to end; you may assume that start != end
    
    Returns:
    The shortest path from start to end given the aforementioned conditions, 
    represented by a list of nodes (Nodes).

    If there exists no path that satisfies the constraints, then return None.
    """
    raise NotImplementedError # replace with your code
    
if __name__ == '__main__':
    # UNCOMMENT THE FOLLOWING LINES TO DEBUG
    pass
    # rmap = load_map('maps/road_map.txt')
    
    # start = Node('N0')
    # end = Node('N9')
    # restricted_roads = ['']
    
    # print(find_optimal_path(rmap, start, end, restricted_roads))
