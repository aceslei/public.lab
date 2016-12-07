with open("/path/to/input/datfile.csv", "rt") as fin:
    with open("/path/to/modified/output.csv", "wt") as fout:
        for line in fin:
            fout.write(line.replace('"NaN"', ''))
            
'''
run this python script, when it is done, you will have a new file called output.csv with all the "Nan" taken out
'''
