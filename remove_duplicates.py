import os
import hashlib


def is_directory(directory):
    if os.path.isdir(directory):
        return True
    print ('Enter a valid Directory')
    exit()

def get_file_checksum(file):
    filesum=hashlib.sha1()
    with open(file,'rb') as file:
        file_bits =0
        while file_bits != b'':
            file_bits= file.read(1024)
            filesum.update(file_bits)
    return filesum.hexdigest()

def main():
    directory = input('Input the directory that you want to scan ')
    is_directory(directory)
    names=[]
    hashes=[]
    for r, d, f in os.walk(directory):
        for file in f:
            names.append(os.path.join(r,file))
            hashes.append(get_file_checksum(os.path.join(r, file)))
    print(names)
    print(hashes)


if __name__=='__main__':
    main()