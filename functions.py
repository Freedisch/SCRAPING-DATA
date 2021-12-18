import os
# contains all of our function

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data +'\n')

def clear_file(path):
    f=open(path,'w')
    f.close()

def does_file_exist(path):
    return os.path.isfile(path)

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line.replace("\n",""))
            