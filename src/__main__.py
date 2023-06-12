import argparse

import problem
import problem_factory

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='Math Worksheet Generator')
    parser.add_argument('-n', '--num', default=10, type=int, help='The number of math problems to make')
    subparsers = parser.add_subparsers(dest='problem_type')
    add_subparser = subparsers.add_parser('add')
    add_subparser.add_argument('--func', help=argparse.SUPPRESS, default=problem_factory.create_addition)
    add_subparser.add_argument('-m', '--min', default=0, type=int, help='The minimum value for an operand')
    add_subparser.add_argument('-M', '--max', default=9, type=int, help='The maximum value for an operand')

    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    problems = [args.func(args.min, args.max) for _ in range(args.num)]

    for problem in problems:
        print(problem)