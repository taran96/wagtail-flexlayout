from setuptools import setup, find_packages
import pkgutil

from wagtail_flexlayout import __version__

install_requires = ['Django>=1.11']

setup(
    name="wagtail-flexlayout",
    version=__version__,
    url='https://github.com/taran96/wagtail-flexlayout',
    license='MIT',
    platforms=['OS Independent'],
    description="A collection of components used by wagtail to create custom layouts using flexbox css",
    install_requires=install_requires,
    long_description=open('README.md').read(),
    author='Taranvir Waraich',
    author_email='taranvir@me.com',
    maintainer='Taranvir Waraich',
    maintainer_email='taranvir@me.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 0.1.0 Alpha',
        'Framework :: Wagtail',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
