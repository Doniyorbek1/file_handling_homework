def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = 0
    for i in op:
        if len(i)>data:
            data = len(i)
    

    return data
# Read data from file
op = open('txt_file/data10.txt').read().split('\n')
print(main(op))