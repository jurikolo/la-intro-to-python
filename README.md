# la-intro-to-python

My sandbox based on [Introduction to Python Development](https://linuxacademy.com/cp/modules/view/id/311) course in LinuxAcademy

## How to develop and distribute command-line application
* create a project:
```bash
mkdir -p $projectname/src/$projectname
```
* initialize python environment
```bash
cd $projectname
pipenv --python python3
pipenv shell
```
* create empty init file
```bash
touch src/$projectname/__init.py__
```

* create setup file and fill in relevant information. See examples in HR lab
```bash
touch setup.py
```

* create README file and fill in relevant information. See examples in HR lab
```bash
touch README.md
```

* create cli file and main function in it. That's entrypoint for the utility
```bash
touch src/$projectname/cli.py
```

* install local package
```bash
pip install -e .
```

* now you can launch utility
```bash
$packagename
```