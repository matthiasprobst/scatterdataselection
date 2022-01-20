import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScatterDataSelection",
    version='0.0.0',
    author="Matthias Probst",
    author_email="matth.probst@gmail.com",
    description="Tool to selecting data points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="N.A.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'matplotlib',
        'plotly',
        'pandas',
        'ipywidgets',
    ],
)
