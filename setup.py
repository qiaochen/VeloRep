"""
VeloAE: Autoencoding single cell velocity
See: https://github.com/qiaochen/VeloRep
"""

from setuptools import setup

setup(
        name='veloAE',
        version='0.2.0',
        description='Autoencoding single cell velocity',
        author='Chen Qiao',
        author_email='cqiao@connect.hku.hk',
        url='https://github.com/qiaochen/VeloAE',
        packages=['veloproj'],
        entry_points = {
            "console_scripts": ['veloproj = veloproj.veloproj:main']
        },
        install_requires=[
            'numpy',
            'scipy',
            'pandas',
            'matplotlib',
            'tqdm',
            'anndata>=0.7.4',
            'scanpy>=1.5.1',
            'scvelo>=0.2.2',
            'torch>=1.7',
            'scikit-learn',
            'torch-geometric>=1.6.3',
        ]
)