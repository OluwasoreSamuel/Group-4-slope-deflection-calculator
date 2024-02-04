class Node:
    def __init__(self,angular_displacement,reaction,settlement, equilibrum_equation):
        self.angular_displacement = angular_displacement
        self.reaction = reaction
        self.settlement = settlement
        self.equilibrum_equation = equilibrum_equation
        
        

class Span:
    def __init__(self, left_fem, right_fem, span_length, load, loading_condition, cord_rotation, left_moment,
                 right_moment, left_slope_deflection_equation, right_slope_deflection_equation,
                 reaction_at_left_node_on_span, reaction_at_right_node_on_span, span_a_value):
        """
        
        Shows all the properties within a span

        Args:
            left_fem (float): The left Fixed End Moment within 2 reactions/support
            right_fem (float): The right Fixed End Moment within 2 reactions/support
            span_length (float): The length within a span
            load (float): The reaction acting on span
            loading_condition (float): _description_
            cord_rotation (float): _description_
            left_moment (float): _description_
            right_moment (float): _description_
            left_slope_deflection_equation (float): _description_
            right_slope_deflection_equation (float): _description_
            reaction_at_left_node_on_span (float): _description_
            reaction_at_right_node_on_span (float): _description_
            span_a_value (float): _description_
        """
        self.left_fem = left_fem
        self.right_fem = right_fem
        self.span_length = span_length
        self.load = load
        self.loading_condition = loading_condition
        self.cord_rotation = cord_rotation
        self.left_moment = left_moment
        self.right_moment = right_moment
        self.left_slope_deflection_equation = left_slope_deflection_equation
        self.right_slope_deflection_equation = right_slope_deflection_equation
        self.reaction_at_left_node_on_span = reaction_at_left_node_on_span
        self.reaction_at_right_node_on_span = reaction_at_right_node_on_span
        self.span_a_value = span_a_value