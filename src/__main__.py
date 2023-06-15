import argparse

import export
import problem_factory


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="Math Worksheet Generator")
    parser.add_argument(
        "-n", "--num", default=10, type=int, help="The number of math problems to make"
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="The location to output the PDF to, if not specified then stdout",
    )
    subparsers = parser.add_subparsers(dest="problem_type")
    add_subparser = subparsers.add_parser("add")
    add_subparser.add_argument(
        "--func", help=argparse.SUPPRESS, default=problem_factory.create_addition
    )
    add_subparser.add_argument(
        "-m", "--min", default=0, type=int, help="The minimum value for an operand"
    )
    add_subparser.add_argument(
        "-M", "--max", default=9, type=int, help="The maximum value for an operand"
    )
    add_subparser.add_argument(
        "-V",
        "--display_vertical",
        action="store_true",
        default=False,
        help="Display the problem vertically instead of horizontally",
    )

    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    problems = [
        args.func(args.min, args.max, args.display_vertical) for _ in range(args.num)
    ]

    if args.output is None:
        for prob in problems:
            print(prob)
    else:
        export.generate_pdf(problems, args.output)
