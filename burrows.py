_BWT_MARKER = 256
from collections import deque

def couting_sort(array, correspondance):
    frequencies = [0 for _ in range(_BWT_MARKER)]
    indexes = [None for _ in range(_BWT_MARKER)]

    for element in array:
        frequencies[correspondance(element)] += 1
    
    _index = 0
    for value, freq in enumerate(frequencies):
        if freq > 0:
            indexes[value] = (_index, _index)
            _index += freq

    i = 0
    while i < len(array):
        value = correspondance(array[i])
        initial_index, actual_index = indexes[value]

        # i'm not in this element zone, so we put it in their zone
        if i < initial_index:
            array[i], array[actual_index] = array[actual_index], array[i]
            indexes[value] = (initial_index, actual_index + 1)
        # i'm in this element zone and i didn't see this element yet
        elif i == actual_index:
            indexes[value] = (initial_index, actual_index + 1)
            i += 1
        # i'm in this element zone and i already see it
        elif i < actual_index:
            i = actual_index

        
    return array


def generate_correspondance_function(text, element_index):

    def correspondance_function(rotation_index):
        deque_text = deque(text)
        deque_text.rotate(rotation_index)

        return deque_text[element_index]

    return correspondance_function
            
