# Python Project Template

Boiler plates for the creation of Python Project Template.

## How-to Use The Template

- Install Python 3
- Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) `pip install cookiecutter`
- Create a blank repository (no readme etc) on Github
- Run `cookiecutter https://github.com/marmstr93ng/PythonProjectTemplate.git` filling in the prompted information
- Connect the local directory to the git repository

## Reference

### Virtual Environments (VENV)

An [inbuilt Python tool](https://docs.python.org/3/library/venv.html) that creates an isolated python environment, keeping project dependencies independent from each other.

1. `python -m venv .venv`
2. `.\\.venv\\Scripts\\activate` or `.\\.venv\\Scripts\\deactivate`

### Requirements.txt

[DEPRICATED FOR PYPROJECT.TOML] A file which contains all the python packages used in the project

- ```pip freeze > requirements.txt``` - Capture the python requirements
- ```pip install -r requirements.txt```  - Install all python packages specified in requirements file

[How to include a Github repo in the requirements file](https://stackoverflow.com/questions/16584552/how-to-state-in-requirements-txt-a-direct-github-source)

### Commit Message Format

#### Format

```text
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

- The **header line is mandatory**, while the rest of the message is advisory.
- Any line of the commit message cannot be longer 100 characters! This allows the message to be easier to read on GitHub as well as in various git tools.
- use the imperative, present tense: "change" not "changed" nor "changes"

#### `<Type>`

- **feat**: a new user feature (inclusion in a release bumps a MINOR version)
- **fix**: a user bug fixed (inclusion in a release bumps a PATCH version)
- **docs**: changes to documentation
- **style**: formatting changes, missing semicolons, etc
- **refactor**: code change that neither fixes a bug nor adds a feature
- **perf**: code change that improves performance (inclusion in a release bumps a PATCH version)
- **test**: adding missing or correcting existing tests
- **chore**: changes to the build process or auxiliary tools and libraries such as documentation generation

#### `<Subject>`

A succinct description of the change.

- don't capitalize first letter
- no dot (.) at the end

#### `<Body>`

The body should include the motivation for the change and contrast this with previous behaviour

#### `<Footer>`

The footer should contain any information about breaking changes and is also the place to reference issue numbers from your issue tracker

- Closed bugs should be listed, comma separated, on a separate line at the end of the footer prefixed with "Closes" keyword like this: `Closes #123, #245`

[[1](http://karma-runner.github.io/6.3/dev/git-commit-msg.html)], [[2](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)]

### Setup SSH

Run all the commands in Git Bash

#### Generate SSH Key

```ssh-keygen -t rsa -b 4096 -C "your_email@example.com"```

- On "Enter a file in which to save the key," press Enter. This accepts the default file location.
- At the prompt, type a secure passphrase.

#### Add SSH Key to SSH-Agent

- SSH-Agent is an SSH key manager that stores the SSH key in a process memory so that users can log into SSH servers without having to type the key’s passphrase every time they authenticate with the server
- Ensure ssh-agent is enabled: ```eval "$(ssh-agent -s)"```
- Add your SSH key to the ssh-agent: ```ssh-add ~/.ssh/id_rsa```

#### Add SSH key to Github Account

- Copy the SSH key to your clipboard. ```clip < ~/.ssh/id_rsa.pub```
- In the top right corner of any page, click your profile photo, then click Settings
- In the user settings sidebar, click SSH keys.
- Click New SSH key.
- Name and add Key

#### Test SSH Connection

```ssh -T git@github.com```

- Check if the hash that is shown matches one of the hashes shown in [Github SSH Key Fingerprints](https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/)
- If the following error occurs ```The authenticity of host 'github.com (140.82.121.3)' can't be established.``` run ```ssh-keyscan github.com >> ~/.ssh/known_hosts``` which will add authenticity to your known_hosts.
