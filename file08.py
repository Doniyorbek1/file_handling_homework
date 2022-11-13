def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = []
    num = 0
    for i in f:
        if i.isdigit():
            data = data + [i]
    for i in data:
        if int(i)>num:
            num = int(i)
    return num

# Read data from file
f = open('txt_file/data08.txt').read().split()
print(main(f))