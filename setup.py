from setuptools import setup, find_packages

setup(
    name='tomo2bm',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Alan Kastengren',
    author_email='akastengren@anl.gov',
    url='https://github.com/xray-imaging/2bm-tomo',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/tomo'],
    description='cli to run tomo scans at 7-bm',
    zip_safe=False,
)

