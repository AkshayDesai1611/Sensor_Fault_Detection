"""
This is a custom class created to map the target values i.e, to 0 and 1
respectively. A label encoding can also be used alternatively
"""
class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__


    def reverse_mapping(self):
        """
        Reverse Mapping function is created to reverse the effect of target mapping
        to its original values i.e, positive and negative
        """
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))

