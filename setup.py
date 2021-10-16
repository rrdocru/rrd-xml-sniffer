# coding: utf-8
import os
import setuptools
from rrd_xml_sniffer import name as package_name, version as package_version

with open('README.md', 'r', encoding='utf-8') as fn:
    long_description = fn.read()


def read_requirements():
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r', encoding='utf-8') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setuptools.setup(
    name=package_name,
    version=package_version,
    description='Утилита получения типа и версии xml-документа',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rrdocru/rrd-xml-sniffer',
    author='IT-Thematic',
    author_email='inbox@it-thematic.ru',
    classifiers=[
        'Development Status :: 5 - Production/Stable'
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=setuptools.find_packages(exclude=['examples', 'tests*']),
    install_requires=read_requirements(),
    python_requires='~=3.6',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'rrd-xml-sniffer=rrd_xml_sniffer.__main__:main'
        ]
    }
)
