import os
from .generator import (
    SetupPyGenerator,
    SetupPyArgument,
    SetupPyCode
)


def cli():
    _, cwd_dirname = os.path.split(os.getcwd())
    generator = SetupPyGenerator()
    generator.arguments.name = SetupPyArgument(
        description='Name of the package',
        value=cwd_dirname
    )

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
        description='Chose a license from here: https: // help.github.com / articles / licensing - a - repository. For example: MIT'
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
        description='Your name'
    )

    generator.arguments.author_email = SetupPyArgument(
        description='Your email'
    )

    generator.arguments.url = SetupPyArgument(
        description='Either the link to your github or to your website'
    )

    generator.arguments.download_url = SetupPyArgument(
        description='Link from which the project can be downloaded'
    )

    generator.arguments.keywords = SetupPyArgument(
        description='List of keywords',
        value=SetupPyCode('[]')
    )

    generator.arguments.install_requires = SetupPyArgument(
        description='List of packages to install with this one',
        value=SetupPyCode('[]')
    )

    generator.arguments.classifiers = SetupPyArgument(
        description='https://pypi.org/classifiers/',
        value=SetupPyCode('[]')
    )
    setup_py = generator.generate()
    setup_py_path = os.path.join(os.getcwd(), 'setup.py')
    with open(setup_py_path, 'w+') as setup_py_file:
        setup_py_file.write(setup_py)


if __name__ == "__main__":
    cli()
