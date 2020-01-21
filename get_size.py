import os
import argparse


# --USER--VARIABLES-- #
user_source = "./"
# --USER--VARIABLES-- #


def get_args():
    """
    gets cli args via the argparse module
    """
    msg = """This tool gets the size of a directory and displays info about the
contents"""
    # create an instance of parser from the argparse module
    parser = argparse.ArgumentParser(description=msg)
    # add expected arguments
    parser.add_argument('-s', dest='source', required=False, help="source dir")
    args = parser.parse_args()
    if args.source:
        source = args.source
    else:
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
    total_size = 0
    for i in files:
        # get the size of the file
        if not os.path.islink(i):
            total_size += os.path.getsize(i)
        else:
            print("skipping symbolic link: {}".format(i))
        # the file name and extension as per os splitext
        fname, file_ext = os.path.splitext(i)
        # append the extension list
        extension.append(file_ext)
    # padding is longest extension length + 1
    pad = max(len(e) for e in extension) + 1
    # determine the size in B, K, M, G, T
    final_size = interpret_size(total_size)
    # create a set from the extension list (essentially just a list of
    # unique extensions)
    extensions = set(extension)
    print("found the following extensions:\n")
    # for each uniq extension
    for i in extensions:
        # print the extension plus the padding then the occurence of
        # the ext.
        print(i.ljust(pad), extension.count(i))
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
