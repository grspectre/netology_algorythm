from merge_with_tag import execute


def main() -> None:
    execute('git reset')
    execute('git clean -fd')


if __name__ == '__main__':
    main()
