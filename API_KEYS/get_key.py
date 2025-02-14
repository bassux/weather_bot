import os.path

this_path = os.path.dirname(os.path.abspath(__file__))

def get_key(name: str) -> str:
    with open(f'{os.path.join(this_path, name)}', 'r') as file:
        return file.readline()
