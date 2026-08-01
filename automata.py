from typing import Any
import permutations
import random

def all_lists(domain: list[Any], n: int):
    if n == 0:
        yield []

    else:
        for l in all_lists(domain, n - 1):
            for element in domain:
                yield l + [element]

def rand_bij(domain: list[Any], n: int) -> dict[tuple[Any], tuple[Any]]:
    all_l = list(all_lists(domain, n))
    all_l_c = all_l.copy()

    perm = permutations.rand_perm_list(len(all_l_c))

    permutations.apply_perm(all_l_c, perm)

    result = dict()

    for e1, e2 in zip(all_l, all_l_c):
        result[tuple(e1)] = tuple(e2)
    
    return result

def rand_long_bij(domain: list[Any], n: int) -> dict[tuple[Any], tuple[Any]]:
    all_l = list(all_lists(domain, n))

    perm = permutations.rand_perm_list(len(all_l))

    permutations.apply_perm(all_l, perm)

    cycle = all_l[1:] + [all_l[0]]

    result = dict()

    for e1, e2 in zip(all_l, cycle):
        result[tuple(e1)] = tuple(e2)
    
    return result

def inv_dict(d: dict[Any, Any]) -> dict[Any, Any]:
    result = dict()

    for k, v in d.items():
        result[v] = k
    
    return result

class BlockAutomata:
    def __init__(self, 
                 initial: list[Any], 
                 rule: dict[tuple[Any], tuple[Any]],
                 offset: bool) -> None:
        """
        Precondition:
        - Every key of rule has the length of some block_size: int
        - block_size divides len(initial)
        """
        self.state = initial.copy()
        self.rule = rule
        self.offset = offset

        self.block_size = len(list(self.rule)[0])
        self.times = len(self.state) // self.block_size
    
    def get_state(self) -> list[Any]:
        return self.state.copy()
    
    def get_item(self, index: int) -> Any:
        return self.state[index]
    
    def half_update(self) -> None:
        x = 0
        multiples = self.times

        if self.offset:
            x = self.block_size // 2
            multiples -= 1
        
        for _ in range(multiples):
            new_block = self.rule[tuple(self.state[x: x + self.block_size])]

            for i, e in enumerate(new_block):
                self.state[x + i] = e
            
            x += self.block_size
        
        self.offset = not self.offset
    
    def update(self) -> None:
        self.half_update()
        self.half_update()
    
    def reverse(self) -> "BlockAutomata":
        return BlockAutomata(self.state.copy(), inv_dict(self.rule), not self.offset)

random.seed(1)

RAND_RULE = rand_long_bij([False, True], 16)
BLOCK_SIZE = 16