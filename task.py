"""
This is a list of functions that should be completed.
"""

def have_objects_same_value(first, second):

    return (first == second)
    

def is_objects_same_type(first, second):
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return (type(first) == type(second))
    

def is_objects_the_same(first, second):

    return (first is second)
    # """
    # If @first and @second are same objects should return True
    # In another case should return False
    # """

    # pass

def multiple_ints(first_value, second_value):

    if any([not isinstance(first_value, int),not isinstance(second_value, int)]):
        raise ValueError
    else:
        return first_value * second_value


def multiple_ints_with_conversion(first_value, second_value):
    
    try:
        if not isinstance(first_value, int):
            first_value = int(first_value)
        if not isinstance(second_value, int):
            second_value = int(second_value)
        return multiple_ints(first_value, second_value)
    except ValueError:
        print("Not valid input data")

def is_word_in_text(word, text):
    
    if word in text:
        return True
    else:
        return False


def some_loop_exercise():

    for x in range(0,12):
        print (x)
    return 

print (some_loop_exercise())

    
    # """
    # Use loop to create list that contain int values from 0 to 12 except 6 and 7
    # """

    # pass



def remove_from_list_all_negative_numbers(data):
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """

    pass

def alphabet():
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {1: "a", 2: "b" ...}
    """

    pass


def simple_sort(data):
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:
    """

    pass