
# pip install GitPython

from git import Repo

REPO_URL = 'https://github.com/sphrk/git-workflow-automation-with-python.git'
REPO_LOCAL_PATH = './git-workflow-automation-with-python' # Path to Repo Directioy

## init new Rep
# new_repo = Repo.init('./repo_directory')

## Clone
# repo = Repo.clone_from(REPO_URL, REPO_LOCAL_PATH)

## Open existing Repo 
repo = Repo(REPO_LOCAL_PATH)
origin = repo.remote(name='origin')
# print("Repo :", repo)
# print("Origin:", origin)

## Add files to repo
# repo.index.add(['file1', 'file2'])
repo.index.add(['y.txt', 'z.txt'])

## Commit changes
# repo.index.commit('Your Commit Message')
repo.index.commit('this changes committed using GitPython.')
print('changes Commited.')

## Push to origin
# origin.push()
# print("Pushed Changes Successfully.")
