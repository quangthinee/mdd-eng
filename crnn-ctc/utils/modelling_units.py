import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract the modelling units."
    )
    
    parser.add_argument(
        '--train_text',
        help="The training phoneme file."
    )
    
    parser.add_argument(
        '--output',
        help='File contraining modelling unit.'
    )
    
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    
    units = {}
    
    with open(args.train_text, 'r') as fin:
        line = fin.readline()
        
        while line:
            line = line.strip().split(' ')
            
            for char in line[1:]:
                try:
                    if units[char] == True:
                        continue
                except:
                    units[char] = True
            line = fin.readline()
    
    fwriter = open(args.output, 'w')
    for char in units:
        print(char, file=fwriter)