import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apa102_spi",
    version="1.0",
    author="Frederic",
    description="Python library for controlling APA102 LEDs through SPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Frederic98/APA102_SPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['spidev', 'numpy']
)
