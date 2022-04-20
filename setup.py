from setuptools import setup, find_packages
import tetrisTest

setup(
    name="Tetris_KG",
    version="1.0",
    author="club_finX",
    author_email='m@mail.ru',
    packages=find_packages(),
    command_options={
            'build_sphinx': {
                'project': ('setup.py', tetrisTest),
                'version': ('setup.py', "1.0"),
                'release': ('setup.py', "1.0.0"),
                'source_dir': ('setup.py', 'doc')}},
)
