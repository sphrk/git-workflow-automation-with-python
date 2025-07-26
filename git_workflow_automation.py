from argparse import ArgumentParser
from git import Repo

files = [
    'y.txt', 
    'z.txt',
]


REPO_URL = 'https://github.com/sphrk/git-workflow-automation-with-python.git'
REPO_LOCAL_PATH = './git-workflow-automation-with-python' # Path to Repo Directioy

repo = Repo(REPO_LOCAL_PATH)
# print(repo)
## ------------------------------------------------------------------------------------
parser = ArgumentParser(
    prog="My Git Automation App",
    # usage="### Usage text ### %(prog)s %(prog)s",
    # description="### Description text ### %(prog)s",
)

parser.add_argument('-a', '--add', action='store_true', help='add files')
parser.add_argument('-c', '--commit', action='store_true', help='commit changes')
parser.add_argument('-m', '--message', default='No message.', help="Commit message")
parser.add_argument('-p', '--push', action='store_true', help="Push changes to origin")

args = parser.parse_args()
# print(args)
# print(args.add)

add = args.add
commit = args.commit
commit_message = args.message
push = args.push
## ------------------------------------------------------------------------------------

if add:
    repo.index.add(files)
    print('Files Added.')

if commit:
    repo.index.commit(commit_message)
    print('Commited Successfully.')

if push:
    origin = repo.remote(name='origin')
    origin.push()
    print("Pushed Changes Successfully.")
