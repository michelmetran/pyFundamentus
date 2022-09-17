#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run_cmd.py
#  Version: 0.0.6
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------
"""Fundamentus Command line interface."""

import argparse
from test.textualize import (list_all_companies, list_all_property_funds,
                             list_fundamental_indicators)

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

from fundamentus._version import __version__ as version


def get_arguments() -> argparse.Namespace:
    """Argument parser.

    :return: Argument parser.
    """

    # Create the parser.
    parser = argparse.ArgumentParser(
        prog='pyfundamentus',
        description='Python Fundamentus is a Python API that allows you to '
        'quickly access the main fundamental indicators of the '
        'main stocks in the Brazilian market.')

    # Add the arguments.
    parser.add_argument('-t',
                        '--ticker',
                        action='store',
                        type=str,
                        help='Stock ticker.')

    parser.add_argument('-l',
                        '--list',
                        action='store',
                        type=str,
                        default='companies',
                        help='List all companies.')

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=f'%(prog)s {version}')

    return parser.parse_args()


if __name__ == '__main__':
    # Get the arguments.
    args = get_arguments()

    # Initialize the console.
    console = Console()

    # Clean the console.
    console.clear()

    if args.ticker:
        # Get the panels.
        panels = list_fundamental_indicators(ticker=args.ticker)

        titles = [
            f'{panels[1][1].renderable} - {panels[1][0].renderable}',
            'Informações Básicas', 'Oscilações', 'Indicadores de Valuation',
            'Indicadores de Rentabilidade', 'Indicadores de Endividamento',
            'Balanço Patrimonial', 'Demonstrativo de Resultados'
        ]

        # Print the panels.
        with console.pager(styles=True) as screen:
            console.print('Python Fundamentus')

            for panel, title in zip(panels, titles):
                console.print(
                    Panel(title=title,
                          renderable=Columns(panel, expand=True),
                          box=box.HEAVY_EDGE,
                          expand=True))

            # Print the footer.
            console.print('Created by Alexsander Lopes Camargos - '
                          'https://github.com/alexcamargos/pyFundamentus')
    elif args.list == 'companies':
        # Get the table.
        table = list_all_companies()

        # Print the tables.
        with console.pager(styles=True) as screen:
            console.print('Python Fundamentus')

            console.print(table)

            # Print the footer.
            console.print('Created by Alexsander Lopes Camargos - '
                          'https://github.com/alexcamargos/pyFundamentus')
    else:
        # Get the table.
        table = list_all_property_funds()

        # Print the tables.
        with console.pager(styles=True) as screen:
            console.print('Python Fundamentus')

            console.print(table)

            # Print the footer.
            console.print('Created by Alexsander Lopes Camargos - '
                          'https://github.com/alexcamargos/pyFundamentus')
