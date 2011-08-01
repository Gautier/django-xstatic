from setuptools import setup, find_packages

long_description = open('README.rst').read()

setup(
    name='django-xstatic',
    version='0.0.1',
    description='Django helpers to use xstatic packages in django projects',
    long_description="",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        ],
    keywords="",
    author='Gautier Hayoun',
    author_email='ghayoun@gmail.com',
    url='http://github.com/gautier/django-xstatic',
    license='MIT license',
    packages=find_packages(),
    install_requires=[''], # yeah, not even XStatic, isn't that MAGIC?
                           # No, it's just smart convention
)

