

def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data =f.split(',')
    return data
# Read data from file
f= open('/home/asus/Python/file_handling_homework/txt_file/data01.txt','r').read()
print(main(f))