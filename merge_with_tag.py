import subprocess


def execute(command: str) -> str:
    output = subprocess.check_output(command)
    output = output.decode('utf8')
    return output.strip()


def get_head_commit() -> str:
    return execute('git rev-parse --short HEAD')


def main() ->  None:
    branch = execute('git branch --show-current')
    if branch != 'prd':
        print("Branch {}. Must be prd".format(branch))
        return
    prd_head_commit = get_head_commit()
    execute('git merge dev')
    cur_head_commit = get_head_commit()
    if cur_head_commit == prd_head_commit:
        print('prd last commit and dev last dev commit are identical. exit')
        return
    execute('git tag -a {tag} -m "tag {tag}"'.format(tag=cur_head_commit))
    execute('git push --tags')

if __name__ == '__main__':
    main()
