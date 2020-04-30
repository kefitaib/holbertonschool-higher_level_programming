#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    l = dir(hidden_4)
    for i in range(len(l)):
        if l[i][:1] != '_':
            print("{:s}".format(l[i]))
