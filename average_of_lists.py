import numpy as np

def main():
    a = [4, 5, 6]
    b = [6, 7, 8]
    c = [8, 9, 10]

    avg = average(a, b, c)
    average_w = weighted_average([0.5, 0.25, 0.25], a, b, c)
    print(avg)
    print(average_w)

def check_data(data_lists, data_weights=None):
    '''
    This function checks the data for the same length
    and the correct number of weights were applied
    '''
    # check if all of the data is the same length
    for i, d in enumerate(data_lists[1:],1):
        if len(d) != len(data_lists[i-1]):
            raise ValueError('The data arrays are not all the same length.')

    # check if the correct number of weights has been applied
    if data_weights and len(data_lists) != len(data_weights):
        raise ValueError('Number of weight values does not match length of data.')
    

def average(*argv):
    check_data(argv)
    data = np.array(argv)
    return list(np.average(data, axis=0))


def weighted_average(*argv, data_weights=None):
    '''
    This function reports an area weighted average
    '''
    if not data_weights:
        # straight average weights
        data_weights = [1] * len(argv)
    
    check_data(argv, data_weights)
    # transpose the data
    argvTransposed = list(map(list, zip(*argv)))
    data = np.array(argvTransposed)
    return np.average(data, axis=1, weights=data_weights)

if __name__ == '__main__':
    main()