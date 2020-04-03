import textwrap
from typing import Any


class SetupPyCode:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return self.value


class SetupPyArgument:
    def __init__(self,
                 name: str = '',
                 value: Any = '',
                 description: str = None,
                 imports=None,
                 presetup='',
                 postsetup=''):
        self.name = name
        self.value = value
        self.description = description
        self.imports = imports if imports else []
        self.presetup = presetup
        self.postsetup = postsetup

    def str(self, tab=0):
        result = ''

        if self.description:
            description_parts = []
            part = ''
            for word in self.description.split(' '):
                if len(part) + len(word) + 1 > 50:
                    description_parts.append(part)
                    part = ''
                part += word + ' '
            if part != '':
                description_parts.append(part)

            for i, part in enumerate(description_parts):
                if i != 0:
                    result += '\n'
                result += '\t' * tab + f'# {part}'
            if len(description_parts) != 0:
                result += '\n'

        if isinstance(self.value, str):
            value = f"'{self.value}'"
        else:
            value = f"{self.value}"
        result += '\t' * tab + f'{self.name}={value}'
        return result


class SetupPyArguments:
    def __init__(self):
        self.__args = {}

    def __getattr__(self, name):
        if name == '_SetupPyArguments__args':
            return self.__getattribute__(name)
        return self.__args[name]

    def __setattr__(self, name, value):
        if name == '_SetupPyArguments__args':
            return object.__setattr__(self, name, value)
        if not isinstance(value, SetupPyArgument):
            raise TypeError("Value should be _SetupPyArgument")
        if value.name == '':
            value.name = name
        self.__args[name] = value

    def __iter__(self):
        def iterator() -> SetupPyArgument:
            for key, value in self.__args.items():
                yield value
        return iterator()


class SetupPyGenerator:
    def __init__(self):
        self.arguments = SetupPyArguments()
        self.imports = [
            'from distutils.core import setup'
        ]
        self.presetup = []
        self.postsetup = []

    def __parse_args(self):
        for arg in self.arguments:
            self.imports = list(set(self.imports + arg.imports))
            if arg.presetup:
                self.presetup.append(arg.presetup)
            if arg.postsetup:
                self.postsetup.append(arg.postsetup)

    def generate(self):
        self.__parse_args()

        setup_py = ''

        for imp in self.imports:
            setup_py += imp + '\n'
        setup_py += '\n'

        for pre in self.presetup:
            setup_py += pre + '\n'
        setup_py += '\n'

        setup_py += 'setup(\n'
        for i, arg in enumerate(self.arguments):
            if i != 0:
                setup_py += ',\n'
            setup_py += arg.str(tab=1)
        setup_py += '\n)\n'

        for post in self.postsetup:
            setup_py += post + '\n'

        return setup_py


if __name__ == "__main__":
    generator = SetupPyGenerator()

    generator.arguments.name = SetupPyArgument(
        name='name',
        value=SetupPyCode('value'),
        description='Name of the package',
        presetup='value = "package"'
    )

    print(generator.generate())
