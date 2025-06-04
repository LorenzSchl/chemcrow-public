from setuptools import find_packages, setup

exec(open("chemcrow/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chemcrow",
    python_requires=">=3.9",
    version=__version__,
    description="Accurate solution of reasoning-intensive chemical tasks, powered by LLMs.",
    author="Andres M Bran, Sam Cox, Andrew White, Philippe Schwaller",
    author_email="andrew.white@rochester.edu",
    url="https://github.com/ur-whitelab/chemcrow-public",
    license="MIT",
    packages=find_packages(),
    package_data={"chemcrow": ["data/chem_wep_smi.csv"]},
    install_requires=[
        "ipython",
        "python-dotenv",
        "pydantic"
        "rdkit",
        "synspace",
        "openai",
        "molbloom",
        "paper-qa@git+https://github.com/LorenzSchl/paper-qa.git",
        "google-search-results",
        "langchain==0.3,<0.4",
        "langchain_core",
        "langchain_openai",
        "langchain_experimental",
        "nest_asyncio",
        "tiktoken",
        "paper-scraper@git+https://github.com/blackadad/paper-scraper.git",
        "pypdf",
        "streamlit",
        "rxn4chemistry",
        "duckduckgo-search",
        "wikipedia",
    ],
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
