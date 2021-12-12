from pydriller import Repository

repo = Repository('https://github.com/schleising/python-tests')

for commit in repo.traverse_commits():
    print(f'{commit.msg}')
