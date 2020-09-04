#  Hint:  You may not need all of these.  Remove the unused functions.
#A Node class
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = []
    for items in tickets:
        if items not in cache:
            cache[items.source] = items.destination

    for items in tickets:
        if items.source == "NONE":
            route.append(items.destination)
    
    while route[-1] != "NONE":
        route.append(cache[route[-1]])

    return route
