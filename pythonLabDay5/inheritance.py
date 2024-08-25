"""
    Simulate blood type inheritance in a family

"""
"""
    you have class Person
    which has a list of two elements of person objects representing parents
    each parent, has its own alleles, and you randomly choose one
    has a list of alleles of two elements of str, to assign alleles to.


    alleles: 
            A, B, O
         AA, BB, AB, OO

"""

import random
from typing import Optional, List

NUMBER_OF_GENERATIONS = 3
INDENT_LENGTH = 4


class Person:
    def __init__(self, parents: List, alleles: List[str]):
        # list of 2 elements of type Person
        self.parents = parents
        # list of 2 elements of type str
        self.alleles = alleles


def main():
    # create a new family with NUMBER_OF_GENERATIONS generations
    person = create_family(NUMBER_OF_GENERATIONS)

    # print out the family tree of blood types recursively
    print_family(person, 0)


def create_family(generations: int) -> Person:
    # TODO: Create a new person

    if generations > 1:
        parent_1: Person = create_family(generations - 1)
        parent_2: Person = create_family(generations - 1)

        # TODO: Set parents for current person
        parents=[parent_1, parent_2]
        # TODO: Randomly assign current person's alleles based on the alleles of
        #  their parents
        alleles=[random.choice(parent_1.alleles), random.choice(parent_2.alleles)]

    else:
      # TODO: Set parent pointers to NULL
      parents=[None,None]

      # TODO: Randomly assign alleles
      alleles=[get_random_allele(),get_random_allele()]

    # TODO: Return newly created person
    return Person(parents, alleles)

def print_family(person: Optional[Person], number_of_generations: int):
    if not person:
        return
    print(f"{' ' * number_of_generations * INDENT_LENGTH}", end="")
    if number_of_generations == 0:
        print(f"Child (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    elif number_of_generations == 1:
        print(f"Parent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    else:
        for i in range(number_of_generations - 2):
            print("great-", end="")
        print(f"grandparent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    print_family(person.parents[0], number_of_generations + 1)
    print_family(person.parents[1], number_of_generations + 1)


def get_random_allele():
    random_number: float = random.random()
    random_number = int(random_number * 100) % 3
    if random_number == 0:
        return "A"
    elif random_number == 1:
        return "B"
    return "O"


if __name__ == "__main__":
    main()