import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-travis-test",
    version="0.0.3",
    author="davidlj95 && ccebrecos",
    author_email="ccebrecos@davidlj95.com",
    description="Tests PyPi deployments with Travis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidlj95/python-travis-test",
    packages=setuptools.find_packages(),
    classifiers=(
	"Programming Language :: Python :: 3.5",
	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ),
)
