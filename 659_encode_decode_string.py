"""
   @param: strs: a list of strings
   @return: encodes a list of strings to a single string.
   """
def encode(self, strs):
    # write your code here
    individual = []
    for string in strs:
        individual.append(string)
    return ".".join(individual)

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(self, str):
    # write your code here
    return str.split(".")



