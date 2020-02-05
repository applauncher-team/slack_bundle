from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='slack_bundle',
    packages=find_packages(),
    version='1.0',
    description='Slack support for applauncher',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/slack_bundle',
    download_url='https://github.com/applauncher-team/slack_bundle/archive/master.zip',
    keywords=['applauncher', 'slack'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
) 
