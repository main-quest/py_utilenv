from setuptools import setup, find_packages

# How to structure a python main package: https://stackoverflow.com/a/54613085
install_requires = open("requirements.txt", "r").read().splitlines()

# Remove any comments
install_requires = [line for line in install_requires if not line.startswith('#')]
pkg_name = 'py_utilenv'

setup(
    name=pkg_name,
    version='0.0.4',
    description="Utils for environment setup (mostly environment vars). " +
                f"'Install by 'pip install --upgrade git+https://github.com/main-quest/py_utilenv.git#egg={pkg_name}'",
    url='https://github.com/main-quest/py_utilenv.git',
    author='The Fallen Games',
    author_email='contact@thefallengames.com',
    license='unlicense',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires=">=3.7",
    install_requires=install_requires,
    zip_safe=False
)
