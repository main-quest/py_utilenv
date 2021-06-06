import os
from pathlib import Path


def add_or_update_env_var(key: str, val: str):
    if os.name == 'nt':
        if val.startswith('\''):
            val.strip('\'')

        if not val.startswith('"'):
            val = f'"{val}"'

        # Machine-wide
        os.system(f'SETX /M {key} {val}')
        # User-wide
        os.system(f'SETX {key} {val}')
        # Session-wide
        os.system(f'SET {key}={val}')

    elif os.name == 'posix':
        env_file_sys = '/etc/environment'
        env_file_user = str(Path.home()) + '/.bashrc'

        with open(env_file_sys, 'r') as f:
            env_lines_sys = f.readlines()
        with open(env_file_user, 'r') as f:
            env_lines_user = f.readlines()

        # env file format: VAR="<VALUE>"
        prefix = f"{key}='"
        line_to_set = f"{prefix}{val}'\r\n"
        __add_or_update_var_on_line(env_lines_sys, prefix, line_to_set)

        # .bashrc file format (just a bash script): export VAR="<VALUE>"
        prefix = f"export {key}='"
        line_to_set = f"{prefix}{val}'\r\n"
        __add_or_update_var_on_line(env_lines_user, prefix, line_to_set)

        with open(env_file_sys, 'w') as f:
            f.writelines(env_lines_sys)
        with open(env_file_user, 'w') as f:
            f.writelines(env_lines_user)

    else:
        raise Exception('Case not handled: os.name=' + os.name)

    # This applies the changes to the current session (so you won't need to log in and out)
    # Commented: this was (almost silently) failing, because the command 'source' is a shell builtin, so we need
    # another way of updating the current process' env
    # os.system('source ' + ENV_FILE_SYS)
    _environ = dict(os.environ.copy())
    try:
        _environ[key] = val
    finally:
        try:
            os.environ.clear()
        finally:
            os.environ.update(_environ)


def __add_or_update_var_on_line(lines: [str], line_prefix: str, line_to_set: str):
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith(line_prefix):
            lines[i] = line_to_set
            return

    lines.append(line_to_set)
