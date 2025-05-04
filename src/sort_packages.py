import sys

MAX_VOLUME =  1_000_000
MAX_MASS = 20

def sort_packages(width: int, height: int, length: int, mass: int) -> str:
    """Classify a package based on its volume and mass.

    Args:
        width: Package width in centimeters.
        height: Package height in centimeters.
        length: Package length in centimeters.
        mass: Package mass in kilograms.

    Returns:
        str: "STANDARD", "SPECIAL" or "REJECTED".
    """
    volume = width * height * length
    
    if volume >= MAX_VOLUME and mass >= MAX_MASS:
        return "REJECTED"
    elif volume >= MAX_VOLUME or mass >= MAX_MASS:
        return "SPECIAL"

    return "STANDARD"
