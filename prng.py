from typing import Union, Iterable
from math import log2
import automata
import graphs

def order_adjacency(graph: list[set[int]]) -> list[list[int]]:
    result = []

    for adjacent in graph:
        result.append(list(adjacent))
    
    return result

def nat_to_bool_list(n: int, length: Union[None, int]) -> list[bool]:
    """
    Precondition:
    - 0 <= n < 2 ** length if length is not None
    - length > 0 if length is not None
    """
    result = list()

    for bit in bin(n)[2:]:
        result.append(bit == '1')
    
    if length is not None:
        result.reverse()

        for _ in range(length - len(result)):
            result.append(False)
    
        result.reverse()
    
    return result

def bool_iter_to_nat(l: Iterable[bool]) -> int:
    return int(''.join('1' if b else '0' for b in l), 2)

class Expander:
    def __init__(self, graph: list[set[int]], k: int) -> None:
        """
        Precondition:
        - k > 0
        - graph is a (2 ** k)-out graph
        - len(graph) == 2 ** n and n > 0 for some n: int
        """
        self.graph = order_adjacency(graph)
        self.n = int(log2(len(self.graph)))
        self.k = k

        self.state = 0
    
    def update(self, bools: list[bool]) -> list[bool]:
        """
        Precondition:
        - len(bools) == self.k
        """
        decision = bool_iter_to_nat(bools)

        self.state = self.graph[self.state][decision]

        return nat_to_bool_list(self.state, self.n)

def get_bool_from_automaton(automaton: automata.BlockAutomata, n_iterations: int, index: int) -> bool:
    """
    Precondition:
    - n_iterations > 0
    """
    for _ in range(n_iterations):
        automaton.update()
    
    x = index

    return automaton.get_item(x)

class PRNG:
    def __init__(self, automaton: automata.BlockAutomata, n_iterations: int, index: int, expander: Expander) -> None:
        self.automaton = automaton
        self.n_iterations = n_iterations
        self.index = index
        self.expander = expander
    
    def update(self) -> list[bool]:
        bools = []

        for _ in range(self.expander.k):
            bools.append(get_bool_from_automaton(self.automaton, self.n_iterations, self.index))
        
        return self.expander.update(bools)

def get_prng(seed: int, n_iterations: int) -> PRNG:
    data = nat_to_bool_list(seed % (2 ** (16 * automata.BLOCK_SIZE)), 16 * automata.BLOCK_SIZE)

    automaton = automata.BlockAutomata(data, automata.RAND_RULE, False)

    four_out = graphs.rand_k_out_graph(2 ** 14, 4)

    expander = Expander(four_out, 2)

    prng = PRNG(automaton, n_iterations, len(data) // 2, expander)

    return prng