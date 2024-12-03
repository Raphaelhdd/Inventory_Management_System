import sys
import os
import pytest 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    pytest_args = ["tests/"]
    result = pytest.main(pytest_args)
    if result == 0:
        print("All Basics tests passed !")
    else:
        print("Some tests failed")

if __name__ == "__main__":
    main()