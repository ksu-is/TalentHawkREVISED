from setuptools import setup, find_packages

setup(
    name="talenthawk",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask>=2.2.3",
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "matplotlib>=3.5.2",
        "scikit-learn>=1.2.1",
        "scipy>=1.10.0",
        "pytest>=7.0.0",
    ],
    author="TalentHawk Team",
    author_email="example@talenthawk.com",
    description="A simple soccer talent scouting and analytics platform",
    keywords="soccer, sports, analytics, scouting, talent, data",
    url="https://github.com/ksu-is/TalentHawkREVISED",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Sports Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
) 