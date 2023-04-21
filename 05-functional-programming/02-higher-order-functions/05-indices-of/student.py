def indices_of(xs, condition):
    truth_list = list()
    for x in xs:
        if condition(x):
            truth_list.append(xs.index(x))

    return truth_list