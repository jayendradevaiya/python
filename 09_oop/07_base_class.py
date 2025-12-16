class Chai:
    def __init__(self,type_, strength):
        self.type = type_
        self.strength = strength


""" This is a simple method"""

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level   

"""This is a explicit method"""

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(type_, strength)
#         self.spice_level = spice_level

""" This is a super method"""

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level