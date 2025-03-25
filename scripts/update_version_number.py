#!/usr/bin/env python3

import os
import pathlib
import re
import sys

ROOT_DIR = ".."


def replace_file(file, pattern, repl):
    with open(file, "r") as f:
        code = f.read()
    code = re.sub(pattern, repl, code, count=1)
    with open(file, "w") as f:
        f.write(code)


def set_version_numbers():
    if len(sys.argv) < 2:
        print("set_version_numbers version")
        sys.exit(1)
    os.chdir(pathlib.Path(__file__).parent / ROOT_DIR)
    version = sys.argv[1]
    replace_file(
        "rust/pyxel-engine/src/settings.rs", '(VERSION.*)".*"', f'\\1"{version}"'
    )
    replace_file("python/pyproject.toml", '(version.*)".*"', f'\\1"{version}"')
    replace_file("rust/pyxel-platform/Cargo.toml", '(version.*)".*"', f'\\1"{version}"')
    replace_file("rust/pyxel-engine/Cargo.toml", '(version.*)".*"', f'\\1"{version}"')
    replace_file(
        "rust/pyxel-engine/Cargo.toml",
        '(pyxel-platform", version.*)".*"',
        f'\\1"{version}"',
    )
    replace_file("rust/pyxel-wrapper/Cargo.toml", '(version.*)".*"', f'\\1"{version}"')
    replace_file(
        "rust/pyxel-wrapper/Cargo.toml",
        '(pyxel-engine", version.*)".*"',
        f'\\1"{version}"',
    )


if __name__ == "__main__":
    set_version_numbers()
