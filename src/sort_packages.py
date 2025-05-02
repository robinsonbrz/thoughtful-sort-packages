import sys

def sort_packages(width, height, length, mass):
    volume = width * height * length
    
    if volume >= 1000000 and mass >= 20:
        return "REJECTED"
    elif volume >= 1000000 or mass >= 20:
        return "SPECIAL"

    return "STANDARD"
