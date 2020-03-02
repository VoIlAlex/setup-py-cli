from distutils.core import setup
from setuptools import find_packages

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='setup-py-cli',
    scripts=['./bin/setup-py'],
    version='1.0.2',
    license='MIT',
    description='Simple module to generate setup.py template.',
    author='Ilya Vouk',
    author_email='ilya.vouk@gmail.com',
    url='https://github.com/VoIlAlex/setup-py',
    download_url='https://github.com/VoIlAlex/setup-py/archive/v1.0.2.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['generator', 'setup', 'distribution', 'devtools'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: System :: Installation/Setup',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
