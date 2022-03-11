'''
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are numbers.
The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

('Tom',19,80) ('John',20,90) ('Jony',17,91) ('Jony',17,93) ('Json',21,85)

Output:

[('John', '20', '90'), ('Jony', '17', '91'),
 ('Jony', '17', '93'), ('Json', '21', '85'),
 ('Tom', '19', '80')]
'''


def sort_tuple_by_index(tups, index):
    """
    Sorts tuples by score
    Args:
        tups (list): List of tuples

    Returns:
        None
    """
    tups.sort(key=lambda tups: tups[index])


def sort_tuples_with_priority(tups):
    """
    Sorts tuples based on priority(name > age > score).
    Args:
        tups (list): List of tuples

    Returns:
        None

    Note:
        Updates the original tuples list
    """
    sort_tuple_by_index(tups, 2)
    sort_tuple_by_index(tups, 1)
    sort_tuple_by_index(tups, 0)


def main():
    tups = input('\nPlease enter tuples seprated by space: \n')
    tups = [eval(i) for i in tups.split(' ')]

    print('\nSorted tuples with priority(name> age> score):')
    sort_tuples_with_priority(tups)
    print(tups)


if __name__ == '__main__':
    main()
