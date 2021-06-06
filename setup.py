from setuptools import setup, find_packages

setup(
    name='py_utilenv',
    version='0.0.3',
    description="Utils for environment setup (mostly environment vars). " +
                "'Install by 'pip install --upgrade git+https://github.com/main-quest/py_utilenv.git#egg=py_utilenv'",
    url='https://github.com/main-quest/py_utilenv.git',
    author='The Fallen Games',
    author_email='contact@thefallengames.com',
    license='unlicense',
    packages=find_packages(),
    zip_safe=False
)
