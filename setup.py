import setuptools

setuptools.setup(
    name='signxml_sunat',
    version='1.0.3',
    author='@danilobrinu',
    author_email='ddbn.c2@gmail.com',
    description='SUNAT - sign and verify xml',
    long_description=open('README.rst', encoding='utf-8').read(),
    install_requires=[
        'lxml >= 4.2.5',
        'xmlsec >= 1.3.52'
    ],
    url='https://github.com/danilobrinu/signxml_sunat',
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)