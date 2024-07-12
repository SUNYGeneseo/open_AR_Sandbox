from setuptools import setup, find_packages
version = '1.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='arsandbox',
    version=version,
    packages=find_packages(exclude=('test', 'docs')),
    include_package_data=True,
    install_requires=[
        'matplotlib >= 3.5',
        'numpy ~= 1.26',
        'pandas',
        'panel == 0.14.4',
        'param < 2',
        'bokeh == 2.4.3',
        'jupyter-bokeh == 2.0.4',
        'scipy',
        'scikit-image',
        'opencv-contrib-python',
        'pytest',
        'jupyter',
        'cython',
        'seaborn',
        'tqdm',
        'pooch',
        'colorama',
        'pysolar',
    	'sphinx',
    	'nbsphinx',
   	'sphinx-rtd-theme',
   	'sphinx-markdown-tables',
   	'sphinx-copybutton',

    ],
    url='https://github.com/cgre-aachen/open_AR_Sandbox',
    license='LGPL v3',
    author='Daniel Escallon, Simon Virgo, Miguel de la Varga',
    author_email='simon@terranigma-solutions.com',
    description='An Open-source, Python-based Augmented reality (AR) sandbox to display many modules.',
    keywords=['AR', 'Augmented reality', 'sandbox', 'geology']
)
