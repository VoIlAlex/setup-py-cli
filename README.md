# SetupPY 

SetupPY is the utility to generate a simple *setup.py* file (template) with useful comments and links.

## Features
Generates *setup.py* file with the following content:
* automatically fulfilled package name based on the name of the current directory.
* some basic fields to fulfill.
* clarifying comments and links to useful resources.
* automatically inserted description from *README.md* or an empty string if there is no *README.md*.



## Installation
```bash
sudo pip install setup-py
```

## Usage
To generate *setup.py* file just type in the terminal.
```bash
setup-py
```
Now *setup.py* file should occur in the current directory. 

## Generated setup.py file
```python
from distutils.core import setup
from setuptools import find_packages
import os


# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Name of the package
    name=<name of current directory>,

    # Packages to include into the distribution
    packages=find_packages('.'), 

    # Start with a small number and increase it with every change you make
    # https://semver.org
    version='1.0.0',

    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    # For example: MIT
    license='',

    # Short description of your library
    description='',

    # Long description of your library
    long_description = long_description,
    long_description_context_type = 'text/markdown',

    # Your name
    author='', 

    # Your email
    author_email='',     

    # Either the link to your github or to your website
    url='',

    # Link from which the project can be downloaded
    download_url='',

    # List of keyword arguments
    keywords=[],

    # List of packages to install with this one
    install_requires=[],

    # https://pypi.org/classifiers/
    classifiers=[]  
)
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ilya Vouk** - *Initial work* - [voilalex](https://github.com/VoIlAlex)

See also the list of [contributors](https://github.com/VoIlAlex/setup-py/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
