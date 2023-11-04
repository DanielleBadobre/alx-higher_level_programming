#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
allname = dir(hidden_4)
for i in range(len(allname)):
    if allname[i][0] != '_' and allname[i][1] != '_':
        print("{}".format(allname[i]))
