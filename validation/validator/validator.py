#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Validator -- DESCRIPTION

"""
from collections import Iterable

from validation.engine.validator_engine import ValidatorEngine
from validation.rules.validation_rule import ValidationRule


class Validator(object):
    """Validatorl

    Validator is a object.
    Responsibility:
    """
    def __init__(self, ):
        """

        @Arguments:
        - `rules`:
        """
        self._engine = ValidatorEngine()
        self._rules = []
        self._on_create()

    def _on_create(self, ):
        """SUMMARY

        _OnCreate()

        @Return:

        @Error:
        """

    @classmethod
    def from_list(cls, rules):
        """SUMMARY

        from_list(rules)

        @Arguments:
        - `rules`:

        @Return:

        @Error:
        """
        # Type check as iterable
        if not isinstance(rules, (Iterable, )):
            raise TypeError("'type' object is not iterable")

        # register each rule
        instance = cls()
        for rule in rules:
            instance.add_rule(rule)

        return instance

    def add_rule(self, rule):
        """Add intance of ValidationRule.

        add_rule(rule)

        @Arguments:
        - `rule`: intance of ValidationRule

        @Return:
        None

        @Error:
        TypeError: if not rule as ValidationRule
        """
        # type check as ValidationRule
        if not isinstance(rule, (ValidationRule, )):
            raise TypeError('Invalided type. Must be ValidationRule type. got ({})'
                            .format(type(rule)))

        # register
        self._rules.append(rule)

    def exists_rule(self, rule):
        """Check rule exists in rules.

        exists_rule(rule)

        @Arguments:
        - `rule`: intance of ValidationRule

        @Return:
        True/False

        @Error:
        TypeError: if not rule as ValidationRule
        """
        # type check as ValidationRule
        if not isinstance(rule, (ValidationRule, )):
            raise TypeError('Invalided type. Must be ValidationRule type. got ({})'
                            .format(type(rule)))

        return rule in self._rules

    def remove_rule(self, rule):
        """Remove instance of ValidationRule.

        remove_rule(rule)

        @Arguments:
        - `rule`: instance of ValidationRule

        @Return:
        None

        @Error:
        TypeError: if not rule as ValidationRule
        """
        # type check as ValidationRule
        if not isinstance(rule, (ValidationRule, )):
            raise TypeError('Invalided type. Must be ValidationRule type. got ({})'
                            .format(type(rule)))

        self._rules.remove(rule)

    def validate(self, value):
        """SUMMARY

        validate(value)

        @Arguments:
        - `value`:

        @Return:
        List of ValidationResult

        @Error:
        """
        # require

        # do
        return self._engine.validate(self._rules, value)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# validator.py ends here
