from setuptools import setup

setup(name='sungather_prometheus_exporter',
      version='0.1',
      description='Export prometheus metrics from sungather.',
      url='http://github.com/Eigenbaukombinat/sungather_prometheus_exporter',
      author='nilo',
      author_email='nilo@team-tfm.com',
      license='BSD',
      packages=['sungather_prometheus_exporter'],
      install_requires=['prometheus_client']
      zip_safe=False)
