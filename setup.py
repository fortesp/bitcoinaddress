import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitcoinaddress",
    version="0.0.2",
    author="Pedro Fortes",
    author_email="pedro.daniel.g@gmail.com",
    description="A simple Bitcoin address generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fortesp/bitcoinaddress",
    packages=setuptools.find_packages(),
    install_requires=['base58', 'ecdsa'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)