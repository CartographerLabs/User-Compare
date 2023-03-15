import setuptools

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="UserCompare",
    version="0.0.6",
    author="James Stevenson",
    author_email="hi@jamesstevenson.me",
    description="A tool for comparing user profiles and returning a confidence score.",
    long_description="A tool for comparing user profiles and returning a confidence score.",
    long_description_content_type="text/markdown",
    url="JamesStevenson.me",
    packages=["UserCompare"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)