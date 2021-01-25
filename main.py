from compression import Compression

def main():
    c = Compression();
    c.compress("compressed.tar.gz", ["mytext.txt", "mytext1.txt"])
    main()

if __name__ == "__main__":
    main()