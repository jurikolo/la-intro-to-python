import subprocess
import sys

def dymp(url):
    try:
        return subprocess.Popen([ 'pgdump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)