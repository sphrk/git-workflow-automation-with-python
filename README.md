# git-workflow-automation-with-python

GitPython library can be used to automate git workflow with python.
By using this library we can run init, clone, add, commit, push and ... commands of git by using python.

`test_GitPython.py` file, contains some examples of executing some commands.

Also by using `argparse` library along with `git`, we can write CLI to automate our git workflow from command line simply.

For example, to add desired files, commit changes and push them to the origin:
```
python git_workflow_automation.py -a -c -m "commit message" -p
```

desired files are defined in a list in `git_workflow_automation.py`.
- `-a` : adds desired files.
- `-c` : commits the changes and `-m` can be used to define commit message.
- `-p` : it pushes changes to the origin.
