def vfs_open(filename):
    f = open(filename, 'rb')
    f.fileno = lambda: -1 # get pygame to call read() on vfs resource
    return f
