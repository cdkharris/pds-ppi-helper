from setuptools import setup, find_packages

setup(name='pds_ppi_helper',
      version='0.1',
      description="A helpful python package for interfacing with the Planetary Plasma Interactions node on NASA's Planetary Data System!",
      url='https://github.com/cdkharris/pds-ppi-helper',
      author='Camilla D. K. Harris',
      author_email='cdha@umich.edu',
      license='GNU',
      packages=find_packages(),
      python requires='>=3.6',
      zip_safe=True # this may not be optimal? unclear
)
