import sys
from sort_packages import sort_packages

if __name__ == "__main__":
    params = [int(arg) for arg in sys.argv[1:]]
    print(sort_packages(*params))
