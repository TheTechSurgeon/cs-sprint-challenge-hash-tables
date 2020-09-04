cache = {}
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #firstpass solution
    # for i in weights:
    #     for j in weights:
    #         if(j+i)==limit:
    #             return (j,i)
    # return None
    #What if the array has only one
    if length == 1:
        return None
    #add to cache
    for index, numbers in enumerate(weights):
        if numbers not in cache:
            cache[numbers]=index

    for index, item in enumerate(weights):
        indexAt = (limit-item)
        if(indexAt) in cache:
            if index == cache[(indexAt)]:
                pass
            else:
                if index > cache[(indexAt)]:
                  print(index, cache[(indexAt)])
                  return(index,cache[(indexAt)])
                else:
                    print(cache[(indexAt)], index)
                    return (cache[(indexAt)],index)
        