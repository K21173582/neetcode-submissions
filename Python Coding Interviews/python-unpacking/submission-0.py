from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    i = 0
    total = 0
    while i < len(triplet):
        total += triplet[i]
        i += 1

    return total 



def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    i = 0
    total = 1
    while i < len(box_dimensions):
        total *= box_dimensions[i]
        i += 1

    return total 
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
