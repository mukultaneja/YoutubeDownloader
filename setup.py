import ytdownloader
from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    required_packages = f.readlines()

required_packages = [package.strip() for package in required_packages]
custom_packages = ['ytdownloader']

setup(
    name='ytdownloader',
    version=ytdownloader.__VERSION__,
    description='An automation service to download videos from Youtube',
    long_description=long_description,
    url='https://github.com/mukultaneja/YoutubeDownloader',
    author='mukultaneja',
    author_email='mukultaneja91@gmail.com',
    license='MIT License',
    keywords='youtube download downloader videos playlist',
    install_requires=required_packages,
    python_requires='>=2.7',
    entry_points={
        'console_scripts': ['ytdownloader=ytdownloader.command_line:main'],
    },
    packages=custom_packages,
    project_urls={
        'Bug Reports': 'https://github.com/mukultaneja/YoutubeDownloader/issues',
        'Source': 'https://github.com/mukultaneja/YoutubeDownloader',
    },
)
