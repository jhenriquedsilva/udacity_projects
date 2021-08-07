#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np

    cleaned_data = []
    predictions = np.array(predictions).tolist()
    ages = np.array(ages).tolist()
    net_worths = np.array(net_worths).tolist()
    
    """
    for age, net_worth, prediction in zip(ages,net_worths,predictions):
        cleaned_data.append((age[0],net_worth[0],net_worth[0]-prediction[0]))

    """
    errors = []
    for index in range(len(predictions)):
        error = net_worths[index][0] - predictions[index][0]
        if error > 0:
            errors.append(error)
        elif error == 0:
            errors.append(0)
        else:
            errors.append(-error)


    counter = 0
    number_of_points = len(errors) * 0.9
    
    while counter < number_of_points:
        index = errors.index(min(errors))
        age = ages.pop(index)
        net_worth = net_worths.pop(index)
        error = errors.pop(index)
        cleaned_data.append((age[0],net_worth[0],error))
        counter += 1
        
    
    return cleaned_data

