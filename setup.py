from setuptools import setup, find_packages
import tetrisTest

setup(
    name="Tetris_KG",
    version="1.1",
    author="club_finX",
    author_email='m@mail.ru',
    packages=find_packages(),
    command_options={
            'build_sphinx': {
                'project': ('setup.py', tetrisTest),
                'version': ('setup.py', "1.1"),
                'release': ('setup.py', "1.0.1"),
                'source_dir': ('setup.py', 'doc')}},
)
