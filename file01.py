

def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data =f.split(',')
    ls = []
    for i in data:
        ls = ls + [int(i)]
    return ls
# Read data from file
f= open('txt_file/data01.txt').read()
print(main(f))