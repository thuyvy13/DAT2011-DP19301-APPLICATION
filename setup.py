# Sử dụng lệnh "pip install setuptools để sử dụng thư viện setuptools"

from setuptools import setup, find_packages

setup(
    name='DAT2011-DP19301-APPLICATION',
    version='3.12.2',
    description='Hệ thống quản lý điểm số cho sinh viên',
    author='Đỗ Thuỳ Vy',
    author_email='contact.vyda@gmail.com',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)


