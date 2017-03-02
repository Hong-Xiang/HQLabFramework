import subprocess
import sys

def main(argv):
    subprocess.call(['python','test2.py','tmp2.txt'])

if __name__ == "__main__":
    main(sys.argv)