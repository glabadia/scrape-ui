def testSearch(param=""):
    returnVal = "No input entered."
    if param:
        returnVal = param
    print(returnVal)


# testSearch("test")

varDict = {"name": "unknown", "age": "| --", "address": "None"}

inputDict = {"name": "Dan unknown Goldbert", "variableHolder": 76, "reverse": 23,
             "age": "ssfsdf | --", "address": " hey you lolo none lorem ipsum"}


def checkDict(a, b):
    errors = []
    for key in a:
        if a[key].lower() in b[key].lower():
            error = f"This variable has an error on {key}"
            errors.append(error)

    return errors


print(checkDict(varDict, inputDict))
