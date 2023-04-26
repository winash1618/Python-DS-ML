from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    author='John Doe',
    author_email='johndoe@example.com',
    description='A short description of my package',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        # give the list of dependency you want it will get installed during the installation of the package
    ],
)
