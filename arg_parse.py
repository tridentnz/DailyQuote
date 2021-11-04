import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+")

    args = parser.parse_args()
    print(args)
