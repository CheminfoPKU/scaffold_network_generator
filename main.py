from multiprocessing import Pool,Manager
from os import path
import data
import linecache

num_process = 30
input_file = 'input.txt'
output_file = 'output.txt'
input_dir = path.join(path.dirname(__file__),
                      'data',
                      'datasets',
                      input_file
                      )

num_lines = -1
for num_lines, line in enumerate(open(input_dir, 'r')):
    pass
num_lines += 1


def get_smiles(idx_line):
    return linecache.getline(input_dir, idx_line).strip()


if __name__ == '__main__':
    print(num_lines)
    for i in range(num_lines):
        try:
            data.output_to_file(get_smiles(i+1))
        except:
            print(get_smiles(i+1))

