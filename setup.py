from setuptools import setup, find_packages

setup(
    name='Flask-SQLAlchemy-Fixtures-Cli',
    description='Initial data Fixtures for Flask',
    version='0.1.0',
    url='https://github.com/nietzscheson/flask-sqlalchemy-fixtures-cli',
    licence='Apache Licence 2.0',
    author='Cristian Angulo Nova | @nietzscheson',
    author_email='cristianangulonova@gmail.com',
    maintainer='Cristian Angulo Nova',
    maintainer_email='cristianangulonova@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask'
    ]
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    packages=["flask_sqlalquemy_fixtures_cli"]
)
