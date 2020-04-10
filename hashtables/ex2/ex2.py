#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # route = [None] * length

    """
    YOUR CODE HERE
    """
    # fill hashtable with tickets key = source and value = destination
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    answer = []
    # find the first ticket and start there
    current_end = hash_table_retrieve(hashtable, "NONE")

    while current_end is not "NONE":
        # append next
        answer.append(current_end)
        # update current
        current_start = hash_table_retrieve(hashtable, current_end)
        current_end = current_start

    return answer
