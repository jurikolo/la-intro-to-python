hr
========

CLI for exporting system user information into format that can be used by other departments

## Usage

The command will be able to export user names, IDs, home directories, and shells as either JSON or CSV.

This command will not include information about system users. By default, the command will display the information as JSON to Stdout, but the --format flag will allow a person to specify csv as an alternative export type.

Additionally, a file can be specified by using the --path flag.

Here are the various ways that the tool can be used:
```bash
$ hr --format=csv --path=path/to/users.csv
$ hr --path=path/to/users.json
$ hr
[
  {
    "name": "cloud_user",
    "id": 1002,
    "home": "/home/cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "kevin",
    "id": 1003,
    "home": "/home/kevin",
    "shell": "/bin/zsh"
  },
]
$ hr --format=csv
name,id,home,shell
cloud_user,1002,/home/cloud_user,/bin/bash
kevin,1003,/home/kevin,/bin/zsh
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@https://github.com/jurikolo/la-intro-to-python`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`