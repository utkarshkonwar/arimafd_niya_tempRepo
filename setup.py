from setuptools import setup, find_packages
 
setup(name='arimafd',
      version='1.4.1',
      url='https://github.com/waico/arimafd',
      license='MIT',
      #packages=find_packages(),
      packages=['arimafd'],
      author='Vyacheslav Kozitsin, Iurii Katser',
      author_email='waico@waico.ru',
      description='Build librarry',
      #packages=find_packages(exclude=['tests']),
      #long_description=open('./arimafd/README.md').read(),
      #long_description_content_type='text/x-rst',
      install_requires=['numpy','pandas','sympy','scikit-learn','statsmodels'], # install_requires=[ 'A>=1,<2', 'B>=2']
      zip_safe=False)
