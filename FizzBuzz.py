import unittest


def FizzBuzz(n):

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz ")
        else:
            print(i)

class TestFizzBuzz:
    def test_fizzbuzz(self):
        self.test_fizzbuzz(FizzBuzz(5), "1\n2\n\Fizz\4\n\Buzz")


if __name__ == "__main__":
    unittest.main

    
