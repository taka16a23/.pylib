#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""validator_engine -- for validator engine

"""
import collections

from validation.rules.validation_rule import ValidationRule


class BaseValidatorEngine(object):
    """ValidatorEngine

    ValidatorEngine is a object.
    Responsibility:
    """

    def validate(self, rules, value):
        """SUMMARY

        validate(value)

        @Arguments:
        - `value`:

        @Return:
        List of ValidationResult

        @Error:
        """
        raise NotImplementedError()


class ValidatorEngine(BaseValidatorEngine):
    """ValidatorEngine

    ValidatorEngine is a BaseValidatorEngine.
    Responsibility: Process validate value by each rules
    """
    def validate(self, rules, value):
        """Validate value by each rules.

        validate(value)

        @Arguments:
        - `value`: value for inspect

        @Return:
        ValidationResult

        @Error:
        TypeError
        """
        # Type check as iterable
        if not isinstance(rules, (collections.Iterable, )):
            raise TypeError("'type' object is not iterable")

        result = None
        for rule in rules:
            # check type of rule
            if not isinstance(rule, (ValidationRule, )):
                raise TypeError("rule require ValidationRule")
            # if exists result
            if result is not None:
                result.set_next(rule.validate(value))
            # check if first result
            if result is None:
                result = rule.validate(value)
            # stop validation if rule has stop status
            if rule.status_stop_validation() == ValidationRule.STOP_VALIDATION:
                break
        return result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# validator_engine.py ends here
