from __future__ import annotations

import shutil
import pkg_resources
import os
from string import Template
from typing import Dict, Final, List


class ProjectTemplate(Template):
    delimiter = "%"


"""Holds the template files names for the project"""
TEMPLATE_FILES: Final[List[str, str]] = (
    ".gitignore",
    ".pre-commit-config.yaml",
    "AUTHORS.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "Dockerfile",
    "launcher.py",
    "README.md",
    "requirements.txt",
    "tox.ini",
    "scripts/docker.py",
    "src/base/config.py",
    "src/base/database.py",
    "src/base/router.json",
    "src/base/keys/token.key",
    "src/base/keys/cert.key",
    "src/base/keys/uri.key",
    "src/bot/bot.py",
    "src/bot/__init__.py",
    "src/bot/cogs/example.py",
    "tests/test-db.py",
)


class Generator:
    """Generator class for generating the project."""

    def __init__(self):
        pass

    def find_license(self, name: str) -> str:
        """Returns the license file name

        Arguments
        ---------
        name (str): The name of the license

        Returns
        -------
        str: License file name

        """
        license_mapping: Dict[str, str] = {
            "MIT": "LICENSE-mit",
            "Apache-2.0": "LICENSE-ap2",
            "GPL-3.0": "LICENSE-gpl",
            "BSD-3-Clause": "LICENSE-bsd3",
            "BSD-2-Clause": "LICENSE-bsd2",
            "Creative Commons Zero v1.0 Universal": "LICENSE-ccL",
            "Affero GPL v3": "LICENSE-agpl",
            "Eclipse Public License v2.0": "LICENSE-epl",
            "ISC": "LICENSE-isc",
            "LGPL-3.0": "LICENSE-lgpl",
            "Mozilla Public License 2.0": "LICENSE-mpl",
        }

        return license_mapping.get(name, "LICENSE-MIT")

    def find_license_url(self, name: str) -> str:
        """Returns the license file url

        Arguments
        ---------
        name (str): The name of the license

        Returns
        -------
        str: License file url

        """
        license_mapping: Dict[str, str] = {
            "MIT": "https://opensource.org/license/mit",
            "Apache-2.0": "https://opensource.org/license/apache-2-0",
            "GPL-3.0": "https://opensource.org/license/gpl-3-0",
            "BSD-3-Clause": "Lhttps://opensource.org/license/bsd-3-clause",
            "BSD-2-Clause": "https://opensource.org/license/bsd-2-clause",
            "Creative Commons Zero v1.0 Universal": "https://creativecommons.org/licenses/by/3.0/",
            "Affero GPL v3": "https://opensource.org/license/agpl-v3",
            "Eclipse Public License v2.0": "https://opensource.org/license/epl-2-0",
            "ISC": "https://opensource.org/license/isc-license-txt",
            "LGPL-3.0": "https://opensource.org/license/lgpl-3-0",
            "Mozilla Public License 2.0": "https://opensource.org/license/mpl-2-0",
        }

        return license_mapping[name]

    def generate(self, dst: str, project_data: Dict[str, str]):
        """Generates the project

        Arguments
        ---------
        dst (str): The destination path
        project_data (Dict[str, str]): The project data

        """
        for template_file in TEMPLATE_FILES:
            template_path = pkg_resources.resource_filename(
                __name__, f"templates/{template_file}.template"
            )

            with open(template_path, "r", encoding="utf-8") as f:
                template_str = f.read()

            template = ProjectTemplate(template_str)
            processed_content = template.substitute(project_data)

            output_file = template_file.replace(".template", "")
            output_dir = os.path.dirname(output_file)
            os.makedirs(f"{dst}/{output_dir}", exist_ok=True)

            with open(
                f"{dst}/{output_file}", "w", encoding="utf-8"
            ) as f:  # Corrected 'w+' to 'w'
                f.write(processed_content)


if __name__ == "__main__":
    generator = Generator()
