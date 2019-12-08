from distutils.core import setup

setup(name='port-scanner',
    version='1.0.0',
    description='Port scanner using nmap, outputting its results as an HTML page',
    author='x1n5h3n',
    author_email='x1n5h3n@protonmail.com',
    url='https://github.com/x1n5h3n/port_scanner',
    keywords='nmap, html, multiprocessing',
    license='GPLv3',
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security'
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Framework :: Jinja2',
    ],
    packages=['port_scanner'],
    package_dir={'port_scanner': 'port_scanner'},
    package_data={'port_scanner': ['templates/*.html']},
    scripts=['bin/run-scanner'],
)