def zip_function(l1, l2, l3):
    return zip(l1, l2, l3)

def filter_function(values):
    filtered = filter(lambda f: f[1] >= 18 and f[2] >= 80, values)
    return filtered

def map_dictionary(tuple_elements):

    mapped_elems = map(lambda m: {
            "name": m[0],
            "age": m[1],
            "score": m[2]
        }, tuple_elements
    )
    return mapped_elems

if __name__ == '__main__':
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]
    tuples = zip_function(names, ages, scores)
    filter_tuples = filter_function(tuples)
    print(list(map_dictionary(filter_tuples)))
