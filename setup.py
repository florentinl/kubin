from setuptools import setup, find_packages


setup(name='Kubin',
      version='0.2',
      description="Rubik's Cube model and solver",
      url='http://github.com/florentinl/Kubin',
      author='Florentin Labelle',
      author_email='florentin.labelle@outlook.fr',
      license='',
      packages=find_packages(exclude=["Kubin"]),
      zip_safe=False)
