from setuptools import setup


setup(
    name='django-xstatic',
    version='0.0.2',
    description='Django helpers to use XStatic packages in Django projects',
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
    author='Gautier Hayoun',
    author_email='ghayoun@gmail.com',
    url='http://github.com/gautier/django-xstatic',
    license='MIT license',
    packages=['django_xstatic'],
    install_requires=[''], # yeah, not even XStatic, isn't that MAGIC?
                           # No, it's just smart convention
)
