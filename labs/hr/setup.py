from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='hr',
    version='0.1.0',
    author='Jurijs Kolomijecs',
    author_email='jurikolo@yandex.com',
    description='A utility for exporting system user information',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jurikolo/la-intro-to-python',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main'
        ],
    }
)