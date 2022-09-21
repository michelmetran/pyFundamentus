#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: fundamentus_pipeline.py
#  Version: 0.0.5
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
"""Test the FundamentusPipeline."""

from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.drivers.mocks.companies_list import COMPANIES_LIST_MOCK

from .fundamentus_pipeline import FundamentusPipeline


def test_get_stock_information() -> None:
    """Test the get_stock_information method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'papel': 'MGLU3', 'interface': 'mobile'}

    main_pipeline = FundamentusPipeline(url=url, params=payload)
    response = main_pipeline.get_stock_information()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, dict)
    assert isinstance(response.transformed_information['price_information'],
                      dict)
    assert isinstance(response.transformed_information['detailed_information'],
                      dict)
    assert isinstance(response.transformed_information['oscillations'], dict)
    assert isinstance(response.transformed_information['valuation_indicators'],
                      dict)
    assert isinstance(
        response.transformed_information['profitability_indicators'], dict)
    assert isinstance(
        response.transformed_information['indebtedness_indicators'], dict)
    assert isinstance(response.transformed_information['balance_sheet'], dict)
    assert isinstance(response.transformed_information['income_statement'],
                      dict)


def test_list_all_companies(requests_mock) -> None:
    """Test the list_all_companies method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    main_pipeline = FundamentusPipeline(url=url, params=payload)
    response = main_pipeline.list_all_companies()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, list)
    assert isinstance(response.transformed_information[0], dict)


def test_list_all_property_funds(requests_mock) -> None:
    """Test the list_all_companies method."""

    url = 'https://www.fundamentus.com.br/detalhes.php'
    payload = {'interface': 'mobile'}

    requests_mock.get(url=url,
                      status_code=COMPANIES_LIST_MOCK['status_code'],
                      text=COMPANIES_LIST_MOCK['content'])

    main_pipeline = FundamentusPipeline(url=url, params=payload)
    response = main_pipeline.list_all_property_funds()

    assert isinstance(response, TransformContract)
    assert isinstance(response.transformed_information, list)
    assert isinstance(response.transformed_information[0], dict)
