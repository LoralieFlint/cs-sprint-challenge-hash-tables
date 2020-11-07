def get_indices_of_item_weights(weights, length, limit):
    # create dictionary
    pairs = {}
        
    # storing to the dictionary (storing values as keys in pairs)
    for item in range(length):
        pairs[weights[item]] = item

    # looping to check if the result of limit - the value of weights exists in pairs
    for item in range(length):
        if limit - weights[item] in pairs:
            # returning the higher valued index first
            return (max(item, pairs[limit - weights[item]]), min(item, pairs[limit - weights[item]]))

    # if pairs dont exist return none
    return None

   
