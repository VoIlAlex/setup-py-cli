from contextlib import contextmanager
from appdata import AppDataPaths
from configparser import ConfigParser


@contextmanager
def config_parser():
    app_data_paths = AppDataPaths(
        app_name='opensource',
        with_dot=True
    )
    if app_data_paths.require_setup():
        app_data_paths.setup()
    config_parser = ConfigParser()
    config_parser.read(app_data_paths.main_config_path)

    yield config_parser

    with open(app_data_paths.main_config_path, 'w+') as f:
        config_parser.write(f)

@contextmanager
def config_section(section_name: str):
    with config_parser() as parser:
        if 'DEFAULT' not in parser:
            parser['DEAFULT'] = {}
        default_section = parser['DEFAULT']
        yield default_section


def build_repo_url(username: str, repo_name: str):
    return f'https://github.com/{username}/{repo_name}'

def build_download_url(username: str, repo_name: str, tag: str = 'v1.0.0'):
    return f'https://github.com/{username}/{repo_name}/archive/{tag}.tar.gz'
