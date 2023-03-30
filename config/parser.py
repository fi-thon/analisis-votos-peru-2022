from argparse import ArgumentParser, Namespace

def parse_arguments() -> Namespace:
    parser = ArgumentParser(description='')
    parser.add_argument(
        '--script',
        metavar='SCRIPT',
        type=str,
        nargs='?',
        default=None,
    )
    parser.add_argument(
        '--ubigeo',
        metavar='000000',
        type=str,
        nargs='?',
        default=None,
    )
    parser.add_argument(
        '--partido',
        metavar='PARTIDO',
        type=str,
        nargs='?',
        default=None,
    )
    
    args: Namespace = parser.parse_args()

    return args