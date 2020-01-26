import os
import sys
# import argparse


# --USER--VARIABLES-- #
user_source = "./"
# --USER--VARIABLES-- #


def get_args():
    try:
        source = sys.argv[1]
    except Exception as e:
        print("didnt specify a directoy, using {}".format(user_source))
        source = user_source
    return source


def get_files(source):
    """
    utilizes the os module walk function to create
    a list of files recursively
    """
    # list comprehension the joins the direcctory
    # path and file name
    file_list = [os.path.join(dir_path, x)
                 for dir_path, dirs, files in os.walk(source)
                 for x in files]
    return file_list


def interpret_size(size):
    """
    convert bytes to human readable
    """
    tib = 1024 ** 4
    gib = 1024 ** 3
    mib = 1024 ** 2
    kib = 1024
    data = float(size)
    if data >= tib:
        symbol = 'TB'
        new_data = data / tib
    elif data >= gib:
        symbol = 'GB'
        new_data = data / gib
    elif data >= mib:
        symbol = 'MB'
        new_data = data / mib
    elif data >= kib:
        symbol = 'KB'
        new_data = data / kib
    elif data >= 0:
        symbol = ' B'
        new_data = data
    formated_data = "{0:.2f}".format(new_data)
    converted_data = str(formated_data) + symbol
    return converted_data


def find_ext(files):
    """
    will count files by extension
    """
    extension = []
    size_by_ext = {}
    total_size = 0
    for i in files:
        try:
            # get the size of the file
            if not os.path.islink(i):
                total_size += os.path.getsize(i)
            else:
                print("skipping symbolic link: {}".format(i))
            # the file name and extension as per os splitext
            fname, file_ext = os.path.splitext(i)
            if file_ext in size_by_ext.keys():
                size_by_ext[file_ext] += os.path.getsize(i)
            else:
                size_by_ext[file_ext] = os.path.getsize(i)
            # append the extension list
            extension.append(file_ext)
        except Exception as e:
            print("encountered an expception\n{}\ncontinuing...".format(e))
            continue

    # padding is longest extension length + 1
    pad = max(len(e) for e in extension) + 1
    # determine the size in B, K, M, G, T
    final_size = interpret_size(total_size)
    print("found the following extensions:\n")
    # for each uniq extension
    # for i in size_by_ext.keys():
    for k, v in size_by_ext.items():
        val = interpret_size(v)
        # print the extension plus the padding then the occurence of
        # the ext.
        print(val.ljust(8), k.ljust(pad), extension.count(k))
    # display total files and size
    print("found {} files totaling {} in size".format(len(files), final_size))


def main():
    # get the args
    source = get_args()
    # get the file list
    files = get_files(source)
    # get our information
    find_ext(files)


# if the file is being ran as itself and not being imported
if __name__ == '__main__':
    main()
