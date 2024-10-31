from setuptools import setup, find_packages

setup(
    name="PortScannerGUI",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # Dependências (exemplo: 'requests>=2.23.0')
    ],
    entry_points={
        "console_scripts": [
            "port_scanner_gui=port_scanner_gui.main:main",
        ],
    },
    author="Seu Nome",
    description="A simple port scanner with GUI for TCP and UDP protocols.",
    license="MIT",
)
