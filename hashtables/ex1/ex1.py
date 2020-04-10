#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        key = limit - weights[i]
        print("weights[i]", weights[i])
        print("limit", limit)
        print("key", key)
        pair_index = hash_table_retrieve(ht, key)

        if pair_index is None:
            hash_table_insert(ht, weights[i], i)
        else:
            return(i, pair_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
