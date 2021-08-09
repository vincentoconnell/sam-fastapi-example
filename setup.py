from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="app",
    version="0.1.0",
    description="data ingestion api",
    url="https://github.com/vincentoconnell/sam-fastapi-example",
    author=" vincentoconnell",
    author_email="",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
