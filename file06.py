def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = cd.split()
    list1 = []
    for i in data:
        list1 = list1 + [len(i)]
    return list1
    
# Read data from file
cd = open('txt_file/data06.txt').read()
print(main(cd))