from setuptools import setup, find_packages

setup(
      name='pharma_vqe',
      version='0.1.0',
      description='Quantum VQE algorithms for pharmaceutical drug discovery',
      author='Brandon Butera',
      author_email='your@email.com',
      url='https://github.com/BrandonButera/qiskit-pharmaceutical-vqe',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires=[
                'qiskit>=0.43.0',
                'qiskit-ibm-runtime>=0.15.0',
                'qiskit-nature>=0.6.0',
                'openfermion>=1.2.0',
                'mitiq>=0.30.0',
                'tensorflow>=2.11',
                'numpy>=1.21',
                'scipy>=1.9',
                'matplotlib>=3.5',
      ],
      python_requires='>=3.9',
      classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Science/Research',
                'Topic :: Scientific/Engineering :: Physics',
                'License :: OSI Approved :: Apache Software License',
      ],
)
