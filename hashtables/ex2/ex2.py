class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create route lenght
    route = [None] * length
    # create location
    location = {}
    # loop through our tickets setting ticket source to destination and next location to none
    for ticket in tickets:
        location[ticket.source] = ticket.destination

    next = location["NONE"]
    # loop over length setting the route index to the next location and the next to the next location in the list 
    for i in range(0, length):
        route[i] = next
        next = location[next]

    return route