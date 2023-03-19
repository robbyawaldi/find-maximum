import unittest
import numpy as np
import random

def create_random_array():
    """
    Fungsi untuk membuat array dengan 1000 nilai random dengan nilai maksimum 999 di index yang acak.
    """
    arr = [random.randint(0, 999) for i in range(1000)]
    max_index = random.randint(0, 999)
    arr[max_index] = 999
    return arr

def find_maximum(arr):
    """
    Fungsi untuk mencari nilai maksimum dalam array.
    """
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return np.max(arr)
    else:
        mid = len(arr) // 2
        left_max = find_maximum(arr[:mid])
        right_max = find_maximum(arr[mid:])
        return np.max([left_max, right_max])

class Test(unittest.TestCase):
    def test_random_element(self):
        self.assertEqual(find_maximum(create_random_array()), 999)

    def test_single_element(self):
        arr = [42]
        expected_max = 42
        self.assertEqual(find_maximum(arr), expected_max)
        
    def test_two_elements(self):
        arr = [1, 2]
        expected_max = 2
        self.assertEqual(find_maximum(arr), expected_max)

    def test_even_length(self):
        arr = [4, 3, 5, 1]
        expected_max = 5
        self.assertEqual(find_maximum(arr), expected_max)
        
    def test_odd_length(self):
        arr = [4, 3, 5, 1, 2]
        expected_max = 5
        self.assertEqual(find_maximum(arr), expected_max)

def main():
    arr = create_random_array()
    print(find_maximum(arr))    

if __name__ == "__main__":
    unittest.main()