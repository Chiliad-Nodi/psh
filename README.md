psh
===

Augmented Unix Userland shell inspired by Windows PowerShell, written in Python.

Requirements
------------

* Python 3+
* pip

Installing
----------

Preferably, you would use a separate virtual env

```bash
pip install -r requirements.txt
pip install -e .  # installs the 'psh' package in editable mode
```

Running
-------

From Python shell:

```
from psh.run import main
main()
```

From Unix shell:
```bash
python -m psh.run
```

Testing
-------

From Unix shell:

```bash
py.test
```
