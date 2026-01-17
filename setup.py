from setuptools import setup, find_packages

setup(
    name="transcenders",
    version="1.0.0",
    description="The Ultimate Quantum System - Superior to Transformers",
    packages=find_packages(),
    install_requires=[
        "pennylane",
        "torch",
        "numpy",
        "fastapi",
        "uvicorn",
        "pydantic",
        "rich",
        "requests"
    ],
    include_package_data=True,
    package_data={
        "": ["*.json"]
    },
    entry_points={
        "console_scripts": [
            "transcenders=transcenders.cli:main"
        ]
    }
)
