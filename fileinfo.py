# Consider a function that’s intended to produce a list with information about files in the current directory and
# that uses Boolean arguments to indicate whether that list should include information such as file size, last modified date, and so forth, for each file.

import os
import time
def get_file_info(filename, size = False, create_date = False, mod_date = False):
    file_info = {}
    if size:
        file_size = os.path.getsize(filename)
        file_info['file_size'] = file_size
    if create_date:
        time_created = os.path.getctime(filename)
        created_time = time.ctime(time_created)
        file_info['created_time'] = created_time
    return file_info

def main():
    filename = 'moby_01.txt'
    file_info = get_file_info(filename, size=True, create_date=True)
    print("The file '{0}' of size {1} was created on {2}".format(filename, file_info['file_size'],file_info['created_time']))

if __name__ == '__main__':
    main()