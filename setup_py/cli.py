import click
import os
from appdata import AppDataPaths
from configparser import ConfigParser
from click_default_group import DefaultGroup

from .generator import (
    SetupPyGenerator,
    SetupPyArgument,
    SetupPyCode
)
from .utils import (
    config_section, 
    config_parser,
    build_download_url,
    build_repo_url
)


def main(use_requirements=False):
    _, cwd_dirname = os.path.split(os.getcwd())
    generator = SetupPyGenerator()
    generator.arguments.name = SetupPyArgument(
        description='Name of the package',
        value=cwd_dirname
    )

    with config_section('DEFAULT') as default_config:
        generator.arguments.packages = SetupPyArgument(
            description='Packages to include into the distribution',
            value=SetupPyCode("find_packages('.')"),
            imports=[
                'from setuptools import find_packages'
            ]
        )

        generator.arguments.version = SetupPyArgument(
            description='Start with a small number and increase it with every change you make https://semver.org',
            value='1.0.0'
        )

        generator.arguments.license = SetupPyArgument(
            description='Chose a license from here: https: // help.github.com / articles / licensing - a - repository. For example: MIT',
            value=default_config['license'] if 'license' in default_config else ''
        )

        generator.arguments.description = SetupPyArgument(
            description='Short description of your library'
        )

        generator.arguments.long_description = SetupPyArgument(
            description='Long description of your library',
            value=SetupPyCode('long_description'),
            presetup="""# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''""",
            imports=[
                'import os'
            ]
        )

        generator.arguments.long_description_content_type = SetupPyArgument(
            value='text/markdown'
        )

        generator.arguments.author = SetupPyArgument(
            description='Your name',
            value=default_config.get('fullname', '')
        )

        generator.arguments.author_email = SetupPyArgument(
            description='Your email',
            value=default_config.get('email', '')
        )

        repo_url = build_repo_url(
            default_config['username'], 
            cwd_dirname
        ) if 'username' in default_config else ''
        generator.arguments.url = SetupPyArgument(
            description='Either the link to your github or to your website',
            value=repo_url
        )

        download_url = build_download_url(
            default_config['username'],
            cwd_dirname
        ) if 'username' in default_config else ''
        generator.arguments.download_url = SetupPyArgument(
            description='Link from which the project can be downloaded',
            value=download_url
        )

        generator.arguments.keywords = SetupPyArgument(
            description='List of keywords',
            value=SetupPyCode('[]')
        )

        if use_requirements and os.path.exists('requirements.txt'):
            with open('requirements.txt') as reqs:
                install_requires = str([req.rstrip() for req in reqs.readlines()])
        else:
            install_requires = str([])
        generator.arguments.install_requires = SetupPyArgument(
            description='List of packages to install with this one',
            value=SetupPyCode(install_requires)
        )

        generator.arguments.classifiers = SetupPyArgument(
            description='https://pypi.org/classifiers/',
            value=SetupPyCode('[]')
        )
        setup_py = generator.generate()
        setup_py_path = os.path.join(os.getcwd(), 'setup.py')
        with open(setup_py_path, 'w+') as setup_py_file:
            setup_py_file.write(setup_py)


@click.group(cls=DefaultGroup, default='generate', default_if_no_args=True)
def cli(*args, **kwargs):
    pass

@cli.command()
@click.option('-r', '--use-requirements', is_flag=True)
def generate(*args, **kwargs):
    main(*args, **kwargs)

@cli.command()
@click.option('-e', '--email', required=False)
@click.option('-u', '--username', required=False)
@click.option('-l', '--license', required=False)
@click.option('-f', '--fullname', required=False)
@click.option('-s', '--show', required=False, is_flag=True)
def config(email, username, license, fullname, show, *args, **kwargs):
    with config_section('DEFAULT') as default_section:    
        if email:
            default_section['email'] = email
        if username:
            default_section['username'] = username
        if license:
            default_section['license'] = license
        if fullname:
            default_section['fullname'] = fullname

    if show:
        with config_parser() as parser:
            for section in parser:
                print(f'[{section}]')
                for key, value in parser[section].items():
                    print(f'{key}={value}')
    

if __name__ == "__main__":
    cli()
