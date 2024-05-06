import unittest #built-in function/module
import fibonacci.fibonacci as fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_input(self):
        number = 10
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0,1,1,2,3,5,8,13,21,34]

    
        number = 6
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0,1,1,2,3,5]
        
        
    def test_fibonacci_with_negative_input(self):
        number = -2
        result = fibonacci.get_fibonacci_series(number)
        assert result is None
        
    def test_fibonacci_with_zero_input(self):
        number = 0
        result = fibonacci.get_fibonacci_series(number)
        assert result is None
    
    def test_fibonacci_with_one_input(self):
        number = 1
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0]
        
    def test_fibonacci_with_wrong_input_type(self):
        number = 0.1
        result = fibonacci.get_fibonacci_series(number)
        assert result is None
        
unittest.main()       
def main():
    number = int(input("enter a number: "))
    series = fibonacci.get_fibonacci_series(number)
    print (series)
    
main()