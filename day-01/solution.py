"""
Day 1: Chronal Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""


# PART 1

def part1():
    frequencies = list(get_input())
    return sum(frequencies)


def get_input():
    with open('input.txt') as f:
        for line in f:
            yield int(line)



# PART 1

def part2():
    frequency_changes = list(get_input())
    seen_frequencies = set()
    current_frequency = 0
    for change in get_next_change(frequency_changes):
        current_frequency += change
        if current_frequency in seen_frequencies:
            return current_frequency

        seen_frequencies.add(current_frequency)

    return seen_frequencies


def get_next_change(frequencies):
    length = len(frequencies)
    idx = 0
    while idx < length:
        yield frequencies[idx]
        idx += 1
        if idx == length:
            idx = 0


if __name__ == '__main__':
    solution_part1 = part1()
    print(solution_part1)

    solution_part2 = part2()
    print(solution_part2)
