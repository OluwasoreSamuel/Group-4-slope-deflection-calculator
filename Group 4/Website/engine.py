from sympy import symbols, Eq, solve
from utilis import Span, Node


def calculate_beam(number_of_supports: int, number_of_internal_joints: int, span_data, settlement_positions: str, settlement_on_beam: float, first_node_fixed: str, last_node_fixed: str):
    number_of_nodes = number_of_supports + number_of_internal_joints
    number_of_spans = number_of_supports - 1

    beam_nodes = [Node() for _ in range(number_of_nodes)]
    beam_spans = [Span(**data) for data in span_data]


  
  

      