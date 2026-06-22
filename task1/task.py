#!/usr/bin/env python3

import argparse

def greet(name):
    return f"Hello, {name}!"
   

def main():
    parser = argparse.ArgumentParser(
        prog="mycli",
        description="Example CLI application"
    )

    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser("hello")
    hello_parser.add_argument("--name", default="World")

    subparsers.add_parser("version")

    args = parser.parse_args()

    if args.command == "hello":
        print(greet(args.name))

    elif args.command == "version":
        print("0.1.0")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()