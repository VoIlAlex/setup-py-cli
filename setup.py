from distutils.core import setup
from setuptools import find_packages

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='setup-py-cli',
    version='2.1.0',
    license='MIT',
    packages=find_packages('.'),
    description='Simple module to generate setup.py template.',
    author='Ilya Vouk',
    author_email='ilya.vouk@gmail.com',
    url='https://github.com/VoIlAlex/setup-py-cli',
    download_url='https://github.com/VoIlAlex/setup-py/archive/v2.1.0.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['generator', 'setup', 'distribution', 'devtools'],
    install_requires=[
        'Click==7.0',
        'appdata==1.2.0',
        'click_default_group==1.2.2'
    ],
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
    ],
    entry_points="""
    [console_scripts]
    setup-py = setup_py.cli:cli
    """,
    zip_safe=False
)
