from setuptools import setup, find_packages

VERSION = '0.5.2' 
DESCRIPTION = 'A package with japanese-related functions'
with open(r"D:\sys\downloads\Python Projects\waganolib\README.md", 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
        name="wagano", 
        version=VERSION,
        author="Ichiro Ishikawa",
        author_email="Saser003@Outlook.sa",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'japan', 'japanese'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)