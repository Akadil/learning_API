# coding: utf-8

"""
    Blockmate

    Blockmate API OpenAPI documentation  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from blockmate import schemas  # noqa: F401


class TransactionRiskReport(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    TransactionRiskReport
    """


    class MetaOapg:
        required = {
            "chain",
            "address",
            "details",
            "risk",
        }
        
        class properties:
            chain = schemas.StrSchema
            
            
            class risk(
                schemas.IntSchema
            ):
                pass
            
            
            class details(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class own_categories(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['RiskReportCategory']:
                                            return RiskReportCategory
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['RiskReportCategory'], typing.List['RiskReportCategory']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'own_categories':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'RiskReportCategory':
                                        return super().__getitem__(i)
                                
                                
                                class source_of_funds_categories(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['RiskReportCategory']:
                                            return RiskReportCategory
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['RiskReportCategory'], typing.List['RiskReportCategory']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'source_of_funds_categories':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'RiskReportCategory':
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "own_categories": own_categories,
                                    "source_of_funds_categories": source_of_funds_categories,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["own_categories"]) -> MetaOapg.properties.own_categories: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["source_of_funds_categories"]) -> MetaOapg.properties.source_of_funds_categories: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["own_categories", "source_of_funds_categories", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["own_categories"]) -> typing.Union[MetaOapg.properties.own_categories, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["source_of_funds_categories"]) -> typing.Union[MetaOapg.properties.source_of_funds_categories, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["own_categories", "source_of_funds_categories", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            own_categories: typing.Union[MetaOapg.properties.own_categories, list, tuple, schemas.Unset] = schemas.unset,
                            source_of_funds_categories: typing.Union[MetaOapg.properties.source_of_funds_categories, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                *args,
                                own_categories=own_categories,
                                source_of_funds_categories=source_of_funds_categories,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> 'details':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            case_id = schemas.StrSchema
            request_datetime = schemas.StrSchema
            response_datetime = schemas.StrSchema
            transaction = schemas.StrSchema
            __annotations__ = {
                "chain": chain,
                "risk": risk,
                "details": details,
                "case_id": case_id,
                "request_datetime": request_datetime,
                "response_datetime": response_datetime,
                "transaction": transaction,
            }
    
    chain: MetaOapg.properties.chain
    address: schemas.AnyTypeSchema
    details: MetaOapg.properties.details
    risk: MetaOapg.properties.risk
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chain"]) -> MetaOapg.properties.chain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk"]) -> MetaOapg.properties.risk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["case_id"]) -> MetaOapg.properties.case_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_datetime"]) -> MetaOapg.properties.request_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response_datetime"]) -> MetaOapg.properties.response_datetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction"]) -> MetaOapg.properties.transaction: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chain", "risk", "details", "case_id", "request_datetime", "response_datetime", "transaction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chain"]) -> MetaOapg.properties.chain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk"]) -> MetaOapg.properties.risk: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["case_id"]) -> typing.Union[MetaOapg.properties.case_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_datetime"]) -> typing.Union[MetaOapg.properties.request_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response_datetime"]) -> typing.Union[MetaOapg.properties.response_datetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction"]) -> typing.Union[MetaOapg.properties.transaction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chain", "risk", "details", "case_id", "request_datetime", "response_datetime", "transaction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        chain: typing.Union[MetaOapg.properties.chain, str, ],
        address: typing.Union[MetaOapg.properties.address, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        details: typing.Union[MetaOapg.properties.details, dict, frozendict.frozendict, ],
        risk: typing.Union[MetaOapg.properties.risk, decimal.Decimal, int, ],
        case_id: typing.Union[MetaOapg.properties.case_id, str, schemas.Unset] = schemas.unset,
        request_datetime: typing.Union[MetaOapg.properties.request_datetime, str, schemas.Unset] = schemas.unset,
        response_datetime: typing.Union[MetaOapg.properties.response_datetime, str, schemas.Unset] = schemas.unset,
        transaction: typing.Union[MetaOapg.properties.transaction, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionRiskReport':
        return super().__new__(
            cls,
            *args,
            chain=chain,
            address=address,
            details=details,
            risk=risk,
            case_id=case_id,
            request_datetime=request_datetime,
            response_datetime=response_datetime,
            transaction=transaction,
            _configuration=_configuration,
            **kwargs,
        )

from blockmate.model.risk_report_category import RiskReportCategory
