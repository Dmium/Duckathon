from setuptools import setup

setup(
    name='projectname',
    packages=['projectname',
              'projectname.controllers',
              'projectname.models'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'marshmallow',
        'marshmallow_enum',
        'flask-cors',
        'flask_jwt',
        'psycopg2'
    ],
)
