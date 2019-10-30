import os
import hashlib

def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Enter a valid Directory')
    exit()

def file_size(file):
    return os.path.getsize(file)

def is_same_name(file1,file2):
    if file1==file2:
        return True
    return False

def get_file_checksum(file):
    filesum=hashlib.sha1()
    with open(file,'rb') as file:
        file_bits =0
        while file_bits != b'':
            file_bits= file.read(1024)
            filesum.update(file_bits)
    return filesum.hexdigest()

def check_item_exists(item, dict={}):
    if item in dict.keys():
        return True
    else:
        return False

def get_items(item, dict={}):
    if item in dict.keys():
        return dict[item]
    else:
        return False

def print_dict(dict):
    for items in dict:
        print(items)


def main():
    files={}
    duplicates={}
    directory=input('Input the directory that you want to scan')
    is_directory(directory)
    for r,d,f in os.walk(directory):
        for file in f:
            filesize=file_size(os.path.join(r,file))
            if check_item_exists(file+"."+str(filesize),files):
                dir_list=get_items(file+"."+str(filesize),files)
                duplicates[f]=os.path.join(r,file)+','+dir_list
            else:
                files[file+"."+str(filesize)]=os.path.join(r,file)
    print_dict(duplicates)

    

if __name__=='__main__':
    main()