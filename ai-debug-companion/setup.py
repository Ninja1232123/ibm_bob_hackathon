#!/usr/bin/env python3
"""
AI Debug Companion - Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="ai-debug-companion",
    version="0.1.0",
    description="An intelligent TUI tool that watches your development session and suggests fixes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DevMaster Team",
    author_email="devmaster@example.com",
    url="https://github.com/devmaster/ai-debug-companion",
    packages=find_packages(exclude=["tests", "tests.*", "examples"]),
    python_requires=">=3.10",
    install_requires=[
        "textual>=0.40.0",
        "gitpython>=3.1.0",
        "click>=8.0.0",
        "watchdog>=3.0.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "ruff>=0.1.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "debug-companion=ai_debug_companion.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debuggers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="debugging ai development tools tui",
    project_urls={
        "Bug Reports": "https://github.com/devmaster/ai-debug-companion/issues",
        "Source": "https://github.com/devmaster/ai-debug-companion",
        "Documentation": "https://github.com/devmaster/ai-debug-companion/blob/main/README.md",
    },
)
