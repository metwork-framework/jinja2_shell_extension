from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n')
        if (line and not line.startswith('--')) and (";" not in line)]

with open("README.md") as f:
    long_description = f.read()

setup(
    author="Fabien MARTY",
    author_email="fabien.marty@gmail.com",
    name="jinja2_shell_extension",
    version="2.1.1",
    license="BSD",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.0',
    description="a jinja2 extension to access to system environment variables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metwork-framework/jinja2_shell_extension",
    keywords="jinja2 extension",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)
