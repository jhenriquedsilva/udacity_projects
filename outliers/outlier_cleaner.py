#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    errors = []
    print(predictions)
    print(ages)
    print(net_worths)

    for prediction, net_worths in zip(predictions,net_worths):
        error = net_worths - prediction
        if error > 0:
            errors.append(error)
        elif error == 0:
            errors.append(0)
        else:
            errors.append(-error)

    counter = 0
    while counter < len(errors) * 0.9:
        index = errors.index(min(errors))
        age = ages.pop(index)
        net_worth = net_worth.pop(index)
        error = errors.pop(index)
        cleaned_data.append((age,net_worth,error))
    
    return cleaned_data

