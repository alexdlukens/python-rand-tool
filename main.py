import argparse
import random
import sys




def main():
    parser = argparse.ArgumentParser(description="Generate a random integer or float.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-i",
        "--int",
        action="store_true",
        help="Generate a random integer",
        dest="_int",
    )
    group.add_argument(
        "-f",
        "--float",
        action="store_true",
        help="Generate a random float",
        dest="_float",
    )
    parser.add_argument("--min", help="Minimum value", default=0, dest="min")
    parser.add_argument("--max", help="Maximum value", default=100, dest="max")
    
    args = parser.parse_args()

    assert args.min < args.max, "Minimum value must be less than maximum value"

    if args._int:
        print(random.randint(int(args.min), int(args.max)))
    elif args._float:
        print(random.uniform(float(args.min), float(args.max)))
    else:
        print("Please specify either -i for int or -f for float")
        sys.exit(1)


if __name__ == "__main__":
    main()
