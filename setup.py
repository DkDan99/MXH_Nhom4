from setuptools import setup, find_packages

setup(
    name='du_doan_xep_loai',
    version='0.1.0',
    description='Dự đoán xếp loại tốt nghiệp sinh viên UIT dựa trên mạng xã hội',
    author='[Tên của bạn]',
    author_email='[Email của bạn]',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'networkx',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ]
)