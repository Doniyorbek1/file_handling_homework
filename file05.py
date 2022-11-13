def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = []
    num = 0
    char = 0
    for i in opn[0]:
        if i.isdigit():
            num +=1
        else:
            char +=1
    list1 = list1 + [num] + [char]
    return list1
    
# Read data from file
opn = open('txt_file/data05.txt').read().split(',')
print(main(opn))