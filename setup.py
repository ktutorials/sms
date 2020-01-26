from setuptools import setup

setup(name='sms',
      version='0.1',
      description='School Management System',
      url='http://github.com/jsanyal/sms',
      author='CFirst Technology Constulting LLC',
      author_email='cfirst@gmail.com',
      license='',
      packages=['sms'],
      zip_safe=False,
      install_requires=[
            'psycopg2'
      ],
      tests_require=[],
      dev_require=[],
      extras_require={
            'test': [],
            'doc': [],
            'dev': [],
      })