from setuptools import setup, find_packages

setup(
    name='voice-transformer',
    version='0.1.0',
    description='A voice transformation tool using machine learning',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/voice-transformer',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'librosa',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)