from setuptools import setup, find_packages

setup(name='pyimgsaliency',
      version='0.1',
      description='A package for calculating image saliency',
      url='https://github.com/yhenon/pyimgsaliency',
      author='Yann Henon',
      author_email='none',
      license='Apache',
      packages=find_packages(),
      install_requires=['networkx', 
                        'scipy', 
                        'scikit-image',
                        'scikit-learn'
                        ],
      zip_safe=False)
