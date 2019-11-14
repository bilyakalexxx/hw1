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

    
    """
    If @first and @second are same objects should return True
    In another case should return False
    """

    pass

def multiple_ints(first_value, second_value):
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError
    Raises:
        ValueError
    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """

    pass


def multiple_ints_with_conversion(first_value, second_value):
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError
    Args:
        first_value: number for multiply
        second_value: number for multiply
    Raises:
        ValueError
    Returns: multiple of two numbers.
    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """

    pass

def is_word_in_text(word, text):
    """
    If text contain word return True
    In another case return False.
    Args:
        word: Searchable substring
        text: Text for searching
    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False
    """


    pass

def some_loop_exercise():
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """

    pass

# data = [1, 5, -7, 8, -1]

def remove_from_list_all_negative_numbers(data):
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    
#     for i in data:
#         if i >= 0:
#             data.remove(i)
# print(remove_from_list_all_negative_numbers(data))


           

    
    
    
    pass

# def alphabet():
#     """
#     Create dict which keys is alphabetic characters. And values their number in alphabet
#     Notes You could see an implementaion of this one in test, but create another one
#     Examples:
#         alphabet()
#         >>> {1: "a", 2: "b" ...}
#     """

#     pass


# def simple_sort(data):
#     """
#     Sort list of ints without using built-in methods.
#     Examples:
#         simple_sort([2, 9, 6, 7, 3, 2, 1])
#         >>> [1, 2, 2, 3, 6, 7, 9]
#     Returns:
#     """

#     pass