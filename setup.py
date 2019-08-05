from setuptools import setup

try:
  readme = open('README.md').read()
except IOError:
  readme = ''


setup(
    name='solidpinball',
    use_scm_version={'write_to': 'pinball/_version.py'},
    url='https://github.com/felipesanches/SolidPinball/',
    license='GNU GPLv3+',
    packages=['pinball',
              'pinball.parts'],
    description='A digital fabrication framework for pinball machines using Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Felipe Correa da Silva Sanches',
    author_email='juca@members.fsf.org',
    python_requires='>=3.6',
    setup_requires=['setuptools_scm'],
    install_requires=['solidpython'],
    classifiers=[
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3 :: Only",
      "Development Status :: 4 - Beta",
      "Topic :: Multimedia :: Graphics :: 3D Modeling",
      "Topic :: Games/Entertainment :: Arcade",
      "Intended Audience :: Manufacturing",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
      "Operating System :: OS Independent",
      "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
