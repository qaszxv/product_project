from setuptools import find_packages, setup

setup(
    name='product-example',
    version='0.0.1',
    description='Listen and store product information',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'nameko==2.8.5',
        'elasticsearch-dsl==6.1.0',
        'marshmallow==2.15.0',
    ],
    extras_require={
        'dev': [
            'pytest==3.5.0',
        ],
    },
    zip_safe=True
)