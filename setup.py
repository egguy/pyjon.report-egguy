from setuptools import setup, find_packages
import os

version = '0.7.1'

setup(name='pyjon.reports-egguy',
      version=version,
      description="Pyjon.Reports is a module bridging z3c.rml, genshi and pypdf together to provide a simple mean of creating templated pdf documents in python.",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='pdf template report rml splitting',
      author='Etienne G.',
      author_email='crazypops@gmail.com',
      url='https://github.com/egguy/pyjon.report-egguy',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pyjon'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'genshi >= 0.5',
          'z3c.rml >= 0.7',
          'pypdf4'
          # -*- Extra requirements: -*-
      ],
      )
