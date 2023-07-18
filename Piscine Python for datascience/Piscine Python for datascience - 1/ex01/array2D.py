def slice_me(family: list, start: int, end: int) -> list:
    shape = (len(family), len(family[0]))
    print("My shape is : ", shape)
    new_family = family[start: end]
    shape = (len(new_family), len(new_family[0]))
    print("My new shape is : ", shape)
    return(new_family)