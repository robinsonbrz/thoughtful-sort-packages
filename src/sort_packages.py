import sys

def sort_packages(width, height, length, mass):
    volume = width * height * length
    
    if volume >= 1000000 and mass >= 20:
        return "REJECTED"
    elif volume >= 1000000 or mass >= 20:
        return "SPECIAL"

    return "STANDARD"

if __name__ == "__main__":
    params = [int(arg) for arg in sys.argv[1:]]
    print(sort_packages(*params))
