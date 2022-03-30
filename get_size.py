import os
import sys


def get_files(source):
    """Using the os walk function, recursively get a list of files in
       the target directory. Returns a list of strings

    Args:
        source (str): directory path

    Returns:
        list: list of strings
    """
    # list comprehension joins the direcctory path and file name
    file_list = [os.path.join(dir_path, x)
                 for dir_path, dirs, files in os.walk(source)
                 for x in files]
    return file_list


def interpret_size(size):
    """converts bytes into something humans can read

    Args:
        size (int): an integer

    Returns:
        (str): human readable string
    """
    for unit in ['  B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024 or unit == "PiB":
            break
        size /= 1024.0
    return f"{size:7.2f} {unit}"


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
                print(f"skipping symbolic link: {i}")
            # the file name and extension as per os splitext
            _, file_ext = os.path.splitext(i)
            if file_ext in size_by_ext.keys():
                size_by_ext[file_ext] += os.path.getsize(i)
            else:
                size_by_ext[file_ext] = os.path.getsize(i)
            # append the extension list
            extension.append(file_ext)
        except Exception as e:
            print(f"encountered an expception\n{e}\ncontinuing...")
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
    print(f"found {len(files)} files totaling {final_size} in size")


def main():
    # get the args
    try:
        source = sys.argv[1]
    except Exception as e:
        print(
            f"got an error!\t{e}\nprogram exiting....\n"
            f"help:\nexpected a directory as an arg"
            )
        sys.exit(1)
    # get the file list
    files = get_files(source)
    # get our information
    find_ext(files)


# if the file is being ran as itself and not being imported
if __name__ == '__main__':
    main()
