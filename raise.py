class ShellException(Exception):
    pass


class ShebangShellException(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Must me a shebang'


class EmptyShellException(Exception):

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'File cannot be empty'


class ShellExecutor:
    def __init__(self, file_content):
        self.content = file_content
        if len(self.content) == 0:
            raise EmptyShellException

        if self.content[0] != '#':
            raise ShebangShellException


content = '#!/bin/bash'   # right
content = '!/bin/bash'    # missing shebang
content = ''     # empty file
try:
    shell_executor = ShellExecutor(content)
except EmptyShellException as ex:
    print(ex.message)
except ShebangShellException as ex:
    print(ex.message)
