from setuptools import setup
from glob import glob

package_data = {
    "{{cookiecutter.cli_name}}": [
        "config.ini",
        "logging.conf",
    ]
}

data_files = [
    "config.ini",
    "logging.conf",
]
directories = glob("{{cookiecutter.cli_name}}/templates/")
for directory in directories:
    files = glob(directory + "*")
    data_files.append((directory, files))

setup(
    name="{{cookiecutter.cli_name}}",
    packages=["{{cookiecutter.cli_name}}"],
    include_package_data=True,
    data_files=data_files,
    package_data=package_data,
    install_requires=[
        "click",
        "requests",
        "sqlalchemy",
        "alembic",
        "psycopg2-binary",
        "mysqlclient",
        "pymysql",
        "jinja2",
    ],
    entry_points="""
    [console_scripts]
    {{cookiecutter.cli_name}}={{cookiecutter.cli_name}}.cli:cli
    """,
)
