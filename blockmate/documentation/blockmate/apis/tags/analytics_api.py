# coding: utf-8

"""
    Blockmate

    Blockmate API OpenAPI documentation  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Generated by: https://openapi-generator.tech
"""

from blockmate.paths.v1_analytics_account_provider_account_account_id_stats.get import GetAccountAnalytics
from blockmate.paths.v1_analytics_project_stats.get import GetProjectAnalytics
from blockmate.paths.v1_analytics_account_provider_stats.get import GetProviderAnalytics
from blockmate.paths.v1_analytics_user_stats.get import GetUserAnalytics


class AnalyticsApi(
    GetAccountAnalytics,
    GetProjectAnalytics,
    GetProviderAnalytics,
    GetUserAnalytics,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
