def has_negatives(a):
    # create dictionary
    posPairs = {}
    # creates array of results
    result = []

    # for each index in a 
    for num in a:
        # if index has a negative pair append to result array
        if -num in posPairs:
            result.append(abs(num))
        else:
            posPairs[num] = "value"
    # returns all indexs with pairs of positive and negaitve integers
    # in case below will return [ 1, 2, 4 ]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
