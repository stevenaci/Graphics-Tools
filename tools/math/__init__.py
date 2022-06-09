
def clamp(num: int, min_value: int, max_value: int):
    """
        clamp a number between two values.
    
    """
    return max(min(num, max_value), min_value)
