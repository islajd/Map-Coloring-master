import sys
from pprint import pprint
from build_graph import build_graph
from map_coloring_utils import mrv, degree_heuristic, lcv, get_allowed_colors, coloring

if __name__ == "__main__":

    map = 'map.txt'

    colors = ['RED', 'GREEN', 'BLUE']

    # Build graph from file
    graph = build_graph(map)

    for _ in range(len(graph)):
        print("\n")
        print("Iteration")
        cities_with_max_degree = degree_heuristic(graph)
        print("degree heuristic", cities_with_max_degree)
        cities_with_minimum_remaining_colors = mrv(graph, colors)
        print("minimum remaining value", cities_with_minimum_remaining_colors)
        much_used_colors = lcv(graph, colors)
        print("least constraining value", much_used_colors)

        # Returns a set that contains the similarity between two or more sets, than pop the first value
        selected_city = set(cities_with_max_degree).intersection(set(cities_with_minimum_remaining_colors)).pop()
        print("Selected city", selected_city)

        # Get allowed color for selected city
        colors_of_selected_city = get_allowed_colors(graph, selected_city, colors)
        print("Selected city colors", colors_of_selected_city)

        # Final chosen color
        common_color = set(much_used_colors).intersection(set(colors_of_selected_city))
        print("Common color of lcv and selected city", common_color)

        try:
            # if the algorithm find any match btw colors of selected city and lcv set, uses the first match 
            # otherwise uses one of city colors
            if common_color:
                color = common_color.pop()
            else:
                color = colors_of_selected_city.pop()

            print("City Color => ", color)
            coloring(graph, selected_city, color)
        except IndexError:
            sys.exit("Something went wrong. Perhaps there is not enough color for this map")

    alone_cities = [graph[city].append("Any Color") for city, neighbours in graph.items() if len(neighbours) == 0]
    pprint(graph)
