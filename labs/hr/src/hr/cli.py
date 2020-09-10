from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    Export system user information.
    """)
    parser.add_argument("--format",
                        help="output format",
                        required=False,
                        default="json",
                        choices=["json", "csv"],
                        type=str.lower)
    parser.add_argument("--path", help="output location", required=False)

    return parser

def main():
    from hr import users, export

    args = create_parser().parse_args()
    user_list = users.get_users()
    if args.format == "csv":
        export.export_to_csv(user_list, args.path)
    else:
        export.export_to_json(user_list, args.path)
    return 0