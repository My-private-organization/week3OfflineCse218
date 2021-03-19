from function import my_function


def bisectionMethod(lowerLimit, upperLimit, e, numberOfIteration):

    if my_function(lowerLimit) * my_function(upperLimit) >= 0:
        return

    newLowerLimit = lowerLimit
    newUpperLimit = upperLimit
    middleValue = None

    for n in range(0, numberOfIteration):

        if n > 1:
            middleValueOld = middleValue

        middleValue = (newLowerLimit + newUpperLimit) / 2
        valueOfmiddle = my_function(middleValue)

        if n > 1:
            eA = abs((middleValue - middleValueOld) / middleValue)
            if eA <= e:
                return middleValue

        if my_function(newLowerLimit) * valueOfmiddle < 0:
            newUpperLimit = middleValue

        elif my_function(newUpperLimit) * valueOfmiddle < 0:
            newLowerLimit = middleValue
        elif valueOfmiddle == 0:
            print("Exact solution found !!!")
            return middleValue
        else:
            return

    return middleValue


sol = bisectionMethod(0, 0.999999999, 0.005, 25)

if sol is not None:
    print(sol)
else:
    print("Solution is not possible using bi-section method")
