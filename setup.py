"""
2021. Triad National Security, LLC. All rights reserved.
This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos
National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S.
Department of Energy/National Nuclear Security Administration. All rights in the program are
reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear
Security Administration. The Government is granted for itself and others acting on its behalf a
nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare
derivative works, distribute copies to the public, perform publicly and display publicly,
and to permit others to do so.
"""
from setuptools import setup, find_packages
from pathlib import Path

__version__ = "1.0.2"

# Read long description
long_description = Path("README.md").read_text(encoding="utf-8")

# Read dependencies
install_requires = Path("requirements.txt").read_text(encoding="utf-8").strip().splitlines()

setup(
    name="pyCP_APR",
    version=__version__,
    author="Maksim E. Eren, Juston S. Moore, Erik Skau, Manish Bhattarai, Gopinath Chennupati, Boian S. Alexandrov",
    author_email="maksim@lanl.gov",
    description="pyCP_APR: CP-APR Tensor Decomposition with PyTorch Backend.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lanl/pyCP_APR",
    packages=find_packages(),
    include_package_data=True,
    platforms=["Linux", "Mac", "Windows"],
    python_requires=">=3.9,<3.13",  # Max Python version added
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries"
    ],
    license="BSD-3-Clause"
)
