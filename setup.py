from setuptools import setup, find_packages

setup(name='etxt_api',

      version='0.1',

      url='https://github.com/Khvostenko-OV/etxt-api',

      license='MIT',

      author='Oleg Khvostenko',

      author_email='homoascensum@gmail.com',

      description='API-client for etxt.biz',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=['requests'])