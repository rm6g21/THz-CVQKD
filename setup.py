"""Setup script for thzcvqkd package."""

from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="thzcvqkd",
    version="1.0.0",
    description="A package for THz Continuous Variable Quantum Key Distribution simulations and analysis.",
    author="Robbie",
    license="MIT",
    python_requires=">=3.9",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest==8.4.2",
            "Sphinx==8.2.3",
        ],
    },
)