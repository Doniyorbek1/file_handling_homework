def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = f.split(',')
    list1 = []
    for i in data:
        for j in range(len(i)):
            if not str(i[j]).isdigit() or i[j].isspace():
                list1 = list1 + [i[j]]

    return list1

   
# Read data from file
f = open('txt_file/data04.txt').read()
print(main(f))