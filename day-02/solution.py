"""
Day 2: Inventory Management System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import collections as _collections


# PART 1

def part1():
    ids = list(get_input())
    two_appearances = 0
    three_appearances = 0
    for id_ in ids:
        frequencies = character_frequencies(id_)
        if character_appearing_twice(frequencies):
            two_appearances += 1

        if character_appearing_three_times(frequencies):
            three_appearances += 1

    return two_appearances * three_appearances


def get_input():
    with open('input.txt') as f:
        for line in f:
            yield line.replace('\n', '')


def character_frequencies(id_):
    frequencies = _collections.defaultdict(lambda : 0)
    for character in id_:
        frequencies[character] += 1

    return frequencies


def character_appearing_twice(frequencies):
    return 2 in frequencies.values()


def character_appearing_three_times(frequencies):
    return 3 in frequencies.values()


# PART 2

def part2():
    for id1 in get_input():
        for id2 in get_input():
            differences_count = string_differences(id1, id2)
            if differences_count == 1:
                correct_id = ''
                for idx in range(len(id1)):
                    if id1[idx] == id2[idx]:
                        correct_id += id1[idx]

                return correct_id


def string_differences(string1, string2):
    assert len(string1) == len(string2)
    difference_count = 0
    for idx in range(len(string1)):
        if string1[idx] != string2[idx]:
            difference_count += 1

    return difference_count


if __name__ == '__main__':
    solution_part1 = part1()
    print(solution_part1)

    solution_part2 = part2()
    print(solution_part2)
