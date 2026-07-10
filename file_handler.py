def read_file(path):
    f = open(path, 'r')
    return f.read()

def write_file(path, content):
    f = open(path, 'w')
    f.write(content)