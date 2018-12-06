"""
Day 3: No Matter How You Slice It
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import collections as _collections


Claim = _collections.namedtuple(
    'Claim', ['id', 'x', 'y', 'width', 'height']
)

# PART 1

def part1():
    claims = list(get_input())
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        for height_offset in range(claim.height):
            height_idx = claim.y + height_offset
            for width_offset in range(claim.width):
                width_idx = claim.x + width_offset
                fabric[height_idx][width_idx] += 1

    no_claims = 0
    one_claim = 0
    multiple_claims = 0
    for row in fabric:
        for square_inch in row:
            if square_inch == 0:
                no_claims += 1
            elif square_inch == 1:
                one_claim += 1
            elif square_inch > 1:
                multiple_claims += 1
            else:
                raise ValueError()

    return no_claims, one_claim, multiple_claims


def get_input():
    with open('input.txt') as f:
        for line in f:
            yield parse_line(line.replace('\n', ''))


def parse_line(line):
    """
    >>> parse_line('#123 @ 3,2: 5x4')
    Claim(id=123, x=3, y=2, width=5, height=4)
    """
    split = line.split()
    claim = Claim(
        id=int(split[0].replace('#', '')),
        x=int(split[2].split(',')[0]),
        y=int(split[2].split(',')[1].replace(':', '')),
        width=int(split[3].split('x')[0]),
        height=int(split[3].split('x')[1]),
    )
    return claim


# PART 2

def part2():
    claims = list(get_input())
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        for height_offset in range(claim.height):
            height_idx = claim.y + height_offset
            for width_offset in range(claim.width):
                width_idx = claim.x + width_offset
                fabric[height_idx][width_idx] += 1

    unique_claim = None
    for claim in claims:
        unique = True
        for height_offset in range(claim.height):
            height_idx = claim.y + height_offset
            if not unique:
                break
            for width_offset in range(claim.width):
                width_idx = claim.x + width_offset
                if fabric[height_idx][width_idx] != 1:
                    unique = False
                    break
        if unique:
            unique_claim = claim.id
            break

    return unique_claim


if __name__ == '__main__':
    solution_part1 = part1()
    print(solution_part1)

    solution_part2 = part2()
    print(solution_part2)
