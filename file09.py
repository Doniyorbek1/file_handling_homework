def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = []
    num = 0
    for i in data1:
        if i.isnumeric():
            data = data + [i]    
    for i in data:
        if int(i)<num:
            num = int(i)
    return num

# Read data from file
data1 = open('txt_file/data09.txt').read().split()
print(main(data1))