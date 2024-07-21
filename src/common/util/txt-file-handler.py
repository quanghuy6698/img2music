def read_file(file_path):
    f = open(file_path, "r")
    return f.read()

def write_to_file(file_path, content):
    f = open(file_path, "w")
    f.write(content)
    f.close()