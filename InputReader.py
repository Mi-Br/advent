
def readInput(location):
    """Reads input file and returns content as array of elements"""
    outp = []
    with open(location, "r") as f:
        read_data = f.read().splitlines()
        for n in read_data:
         outp.append(n)
    return read_data