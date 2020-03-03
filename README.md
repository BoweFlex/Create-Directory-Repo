# Create Directory and Repo

# Description
Simple script to create a new directory, log in to GitHub and create new repository with the same name, and then create an empty README and push the directory to the repository.

# Setup

1. Install Python3
2. Download repository
3. Install requirements of the repository: pip install selenium
4. Either run the command "source ~/Path/to/file/create.zsh" or add block from example .zshrc in this repository to .zshrc (or .bashrc, syntax is the same) file in home folder and quit/reopen terminal.
Note: zsh/bashrc chunk is required if you want this to be available without typing source command before use.
5. If using bash and not zsh, change create.zsh to create.sh and change starting shebang from #!/bin/zsh to #!/bin/bash.
6. Change noted spots in main.py and create.zsh to contain GitHub username and password, and to make sure the create.zsh file knows the path to main.py.
7. If you use VSCode, open VSCode, press Command+Shift+P, type "Shell", and select the option "Shell Command : Install code in PATH".
8. If you don't use VSCode, remove the "code ." line from create.zsh, and if you'd like you can replace it with the command to open your IDE of choice, or just leave it to be in that folder in the terminal.
9. Have fun!
