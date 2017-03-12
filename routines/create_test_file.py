import sys


def create_file(path):
    with open(path, 'w') as fout:
        print("test file content.", file=fout)

if __name__ == "__main__":
    create_file(sys.argv[1])
