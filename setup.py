from setuptools import setup

setup(
    name='snapshotanalyzer-30000',
    version='1.0',
    author='James Reed',
    author_email='jdreed@q.com',
    description='SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/jdreed1954/snapshotalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
        
)
