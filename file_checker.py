import sys
import os

def main():
    length = len(sys.argv)
    if (length < 2):
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        if os.path.exists(filename):
            print(f"File {filename} exists at: {os.path.abspath(filename)}")
        else:
            print(f"File {filename} does not exist")
if __name__ == "__main__":
    main()
     