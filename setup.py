import os.path

from setuptools import setup, find_packages


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except (IOError, OSError):
        return ''

install_requires = {
    'click >= 5.1',
}

setup(
    name='rar_password',
    version='0.0.1',
    description='rar_password is simple command line tool for find password',
    long_description=readme(),
    author='item4',
    author_email='item4_hun' '@' 'hotmail.com',
    maintainer='item4',
    maintainer_email='item4_hun' '@' 'hotmail.com',
    url='https://github.com/item4/rar_password',
    download_url='https://github.com/item4/rar_password/archive/master.zip',
    license='MIT License',
    install_requires=install_requires,
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            ['rar_password = rar_password.cli:main']
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
