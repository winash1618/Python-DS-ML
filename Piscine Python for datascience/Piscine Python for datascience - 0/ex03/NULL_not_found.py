import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, type(math.nan)):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and not isinstance(object, bool) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    else:
        print(f"Type_not_found")
    return 1