inventory = {}

'''
inventory["Amul"] = ["Mystic Mocha",55]    Output - {'Amul': ['Mystic Mocha', 55]}
inventory["Amul, Mystic Mocha"] = 55         Output - {'Amul, Mystic Mocha': 55}
inventory[["Amul","Mystic Mocha"]] = 55         error - TypeError: unhashable type: 'list'

Lists are mutable in Python, which means they can change their content. Since Python dictionaries require keys to be 
hashable and immutable (like strings, integers, or tuples), using a list as a key in a dictionary is not allowed.
To fix the error, you can convert the list to a tuple since tuples are immutable and can be used as dictionary keys.

inventory[("Amul","Mystic Mocha")] = 55  Output - {('Amul', 'Mystic Mocha'): 55}

'''


print(inventory)