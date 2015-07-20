# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


version = '1.0'

tests_require = []

setup(name='ukhtheme.uvclight',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      namespace_packages=['ukhtheme'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ukhtheme.resources',
          'uvc.themes.btwidgets',
      ],
      extras_require = {'test': tests_require},
      entry_points={
      }
      )
