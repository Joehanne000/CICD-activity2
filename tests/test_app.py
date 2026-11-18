import unittest
from src.app import greet

class TestGreeting(unittest.TestCase):
    pass

def test_greeting():
    assert greet() == "Hello! Welcome to Software Engineering."

if __name__ == "__main__":
    unittest.main()
