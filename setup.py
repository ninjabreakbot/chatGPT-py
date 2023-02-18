#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='chatGPT',
      version='0.1.0',
      description='Ask chatGPT questions',
      author='JLA',
      author_email='ninjabreakbot@icloud.com',
      packages=find_packages(include=['chatGPT','chatGPT.*']),
      py_modules=['chatGPT'],
      install_requires=['openai'],
      entry_points={
        'console_scripts': [
            'chatGPT = chatGPT.chatGPT:cli'
        ],
      },
)
