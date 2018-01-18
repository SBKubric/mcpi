import io
from setuptools import setup, find_packages
import sys

with io.open('README.rst', mode='r', encoding='utf8') as f:
    readme = f.read()


setup(name='py3minepi-sbkubric',
      version='0.0.2',
      description='A better Minecraft Pi library. Includes py3mineapi and minecraftstuff',
      url='https://github.com/SBKubric/mcpi',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      zip_safe=True,
      include_package_data=True,
      keywords='minecraft raspberry pi mcpi py3minepi minecraftstuff',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Education',
          'Intended Audience :: Developers',
          'License :: Other/Proprietary License',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
)
