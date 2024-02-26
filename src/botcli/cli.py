from __future__ import annotations

import click
import sys
import platform
from colorama import init, Fore, Style
from InquirerPy import prompt

from . import __version__, Generator, __author__

init(autoreset=True)


@click.command()
def generate():
    """Generates a discord.py bot project"""
    click.echo(
        f"""{Fore.MAGENTA}{Style.BRIGHT}
BBBBBBBBBBBBBBBBB                             tttt                       CCCCCCCCCCCCClllllll   iiii  
B::::::::::::::::B                         ttt:::t                    CCC::::::::::::Cl:::::l  i::::i 
B::::::BBBBBB:::::B                        t:::::t                  CC:::::::::::::::Cl:::::l   iiii  
BB:::::B     B:::::B                       t:::::t                 C:::::CCCCCCCC::::Cl:::::l         
  B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt          C:::::C       CCCCCC l::::l iiiiiii 
  B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t         C:::::C               l::::l i:::::i 
  B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t         C:::::C               l::::l  i::::i 
  B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt         C:::::C               l::::l  i::::i 
  B::::BBBBBB:::::B o::::o     o::::o      t:::::t               C:::::C               l::::l  i::::i 
  B::::B     B:::::Bo::::o     o::::o      t:::::t               C:::::C               l::::l  i::::i 
  B::::B     B:::::Bo::::o     o::::o      t:::::t               C:::::C               l::::l  i::::i 
  B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt      C:::::C       CCCCCC l::::l  i::::i 
BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t       C:::::CCCCCCCC::::Cl::::::li::::::i
B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t        CC:::::::::::::::Cl::::::li::::::i
B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt          CCC::::::::::::Cl::::::li::::::i
BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt               CCCCCCCCCCCCClllllllliiiiiiii
    """
    )
    click.echo(f"{Fore.LIGHTMAGENTA_EX}Version: {Style.RESET_ALL}{__version__}")
    click.echo(f"{Fore.LIGHTMAGENTA_EX}Author: {Style.RESET_ALL}{__author__}\n")
    click.echo(f"                   {Fore.RED}Options: {Style.RESET_ALL}")
    click.echo(Fore.BLUE + "+" + "-" * 46 + "+")
    click.echo(
        f"{Fore.BLUE}|{Fore.LIGHTMAGENTA_EX} [1]{Style.RESET_ALL}: Generate a discord.py bot project       {Fore.BLUE}|"
    )
    click.echo(
        f"{Fore.BLUE}|{Fore.LIGHTMAGENTA_EX} [2]{Style.RESET_ALL}: Display package information             {Fore.BLUE}|"
    )
    click.echo(
        f"{Fore.BLUE}|{Fore.LIGHTMAGENTA_EX} [3]{Style.RESET_ALL}: Exit                                    {Fore.BLUE}|"
    )
    click.echo(Fore.BLUE + "+" + "-" * 46 + "+")
    option = click.prompt(
        f"{Fore.LIGHTMAGENTA_EX}Choose an option{Style.RESET_ALL}", type=int, default=1
    )
    match option:
        case 1:
            gen = Generator()
            path = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the path to the project{Style.RESET_ALL}",
                type=str,
                default="./",
            )
            name = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the project name{Style.RESET_ALL}",
                type=str,
                default="DiscordBot",
            )
            author = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the author name{Style.RESET_ALL}",
                type=str,
                default="ComboGang",
            )
            email = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the author email{Style.RESET_ALL}",
                type=str,
                default="contact@combogang.com",
            )
            description = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the project description{Style.RESET_ALL}",
                type=str,
                default="A discord.py bot project",
            )
            github_link = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the github link{Style.RESET_ALL}",
                type=str,
                default="https://github.com/combogangreal/BotCli",
            )
            docs_link = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the documentation link{Style.RESET_ALL}",
                type=str,
                default=github_link,
            )
            licenseQu = [
                {
                    "type": "list",
                    "name": "license",
                    "message": f"Select an license",
                    "choices": [
                        "MIT",
                        "Apache-2.0",
                        "GPL-3.0",
                        "BSD-3-Clause",
                        "BSD-2-Clause",
                        "Creative Commons Zero v1.0 Universal",
                        "Affero GPL v3",
                        "Eclipse Public License v2.0",
                        "ISC",
                        "LGPL-3.0",
                        "Mozilla Public License 2.0",
                    ],
                },
            ]
            _license = prompt(licenseQu).get("license")
            mongo_uri = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the MongoDB uri{Style.RESET_ALL}",
                type=str,
                default="mongodb://localhost:27017/",
            )
            mongo_cert = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the MongoDB certificate (Copy and paste the certificate){Style.RESET_ALL}",
                type=str,
                default="",
            )
            mongo_db = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the MongoDB database name{Style.RESET_ALL}",
                type=str,
                default="",
            )
            mongo_coll = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the MongoDB collection name for testing{Style.RESET_ALL}",
                type=str,
                default="",
            )
            bot_token = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter your Bot token{Style.RESET_ALL}",
                type=str,
                default="",
            )
            docker_image = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the docker image name{Style.RESET_ALL}",
                type=str,
                default="combogang/discord-bot",
            )
            docker_username = click.prompt(
                f"{Fore.LIGHTMAGENTA_EX}Enter the docker username{Style.RESET_ALL}",
                type=str,
                default="combogang",
            )

            gen.generate(
                path,
                {
                    "NAME": name,
                    "AUTHOR": author,
                    "EMAIL": email,
                    "DESCRIPTION": description,
                    "GITHUB_URL": github_link,
                    "DOCUMENTATION_URL": docs_link,
                    "IMAGE_NAME": docker_image,
                    "DOCKER_HUB_NAME": docker_username,
                    "LICENSE": _license,
                    "LICENSE_LINK": gen.find_license_url(_license),
                    "URI": mongo_uri,
                    "CERT": mongo_cert,
                    "TOKEN": bot_token,
                    "COLLNAME": mongo_coll,
                    "DATABASENAME": mongo_db,
                },
            )

        case 2:
            click.echo(f"{Fore.LIGHTMAGENTA_EX}Name: {Style.RESET_ALL}BotCli")
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Description: {Style.RESET_ALL}A CLI to generate a discord.py bot project"
            )
            click.echo(f"{Fore.LIGHTMAGENTA_EX}Author: {Style.RESET_ALL}ComboGang")
            click.echo(f"{Fore.LIGHTMAGENTA_EX}Version: {Style.RESET_ALL}{__version__}")
            click.echo(f"{Fore.LIGHTMAGENTA_EX}License: {Style.RESET_ALL}MIT")
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Source: {Style.RESET_ALL}https://github.com/combogangreal/BotCli"
            )
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Python Version: {Style.RESET_ALL}{sys.version}"
            )
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Python Path: {Style.RESET_ALL}{sys.executable}"
            )
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Operating System: {Style.RESET_ALL}{platform.system()} {platform.release()}"
            )
            click.echo(
                f"{Fore.LIGHTMAGENTA_EX}Support Server: {Style.RESET_ALL}https://discord.gg/GqdWT74Qwx"
            )
        case 3:
            exit(0)
        case _:
            click.echo(f"{Fore.RED}Invalid option{Style.RESET_ALL}")
