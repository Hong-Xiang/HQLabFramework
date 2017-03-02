import sys

def main(argv):
    with open(argv[1], "w") as fp:
        print("test", file=fp)

if __name__ == "__main__":
    main(sys.argv)