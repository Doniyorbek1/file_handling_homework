def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = f.split(',')
    sum = 0
    num = []

    for i in data:
        for j in i:
            num = num +[j]
    for i in num:
        if i.isdigit():
            sum = sum + int(i)
    return sum
# Read data from file
f = open('txt_file/data07.txt').read()
print(main(f))