from setuptools import setup, find_packages

setup(
    name='pydxfconverter',
    version='0.1.0',
    author='Glenn Layson',
    author_email='dev@glennlayson.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'numpy-stl',
        'ezdxf',
    ],
    entry_points={
        'console_scripts': [
            'stl-to-dxf=pydxfconverter.converter:main',
            'verify-dxf=pydxfconverter.verify_dxf:main',
        ],
    },
)
