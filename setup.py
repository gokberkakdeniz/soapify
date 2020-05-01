import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name='soapify',  
    version='1.0.2',
    entry_points = {
        "console_scripts": ['soapify = soapify.cli:main']
    },
    author="tncga",
    author_email="qokberk_akdeniz@hotmail.com",
    description="search on your all spotify playlists",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tncga/soap",
    packages=["soapify"],
    install_requires=["click", "spotipy"],
    license="MIT",
    keywords="spotify search playlist cli"
 )