# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


PACKAGE_NAME = 'USST'
PACKAGE_VER = "0.5"
PACKAGE_DESC = 'USST - Universal Streamer Subscribing Tool '
PACKAGE_URL = 'https://github.com/lao605/USST.git'


def get_install_requires():
    requires = []
    links = []
    for line in open('requirements.txt', 'r'):
        line = line.strip()
        if not line.startswith('#'):
            parts = line.split('#egg=')
            if len(parts) == 2:
                links.append(line)
                requires.append(parts[1])
            else:
                requires.append(line)
    return requires, links


install_requires, dependency_links = get_install_requires()


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VER,
    description=PACKAGE_DESC,
    url=PACKAGE_URL,
    author='lao605',
    author_email='laozhikun1994@gmail.com',
    # https://pythonhosted.org/setuptools/setuptools.html#id9
    packages=find_packages(exclude=["tests", ]),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
)
