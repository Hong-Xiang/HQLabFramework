""" lauch server """
import sys
from hqlf import app

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(host = "0.0.0.0", port=port, debug=True)
