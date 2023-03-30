from setuptools import setup, find_packages

setup(
    name='c99-api',
    version='1.0.0',
    description='A Python wrapper and handler for the c99.nl API',
    author='David Peterson',
    author_email='dapanon@proton.me',
    url='https://github.com/haste171/c99-api',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

