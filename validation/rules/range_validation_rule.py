#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""RangeValidationRule -- DESCRIPTION

"""
import logging
from validation.rules.validation_rule import ValidationRule
from validation.result.validation_result import ValidationResult


class RangeValidationRule(ValidationRule):
    """RangeValidationRule

    RangeValidationRule is a ValidationRule.
    Responsibility:
    """
    def __init__(self, start, end, stopvalidation=None):
        """

        @Arguments:
        - `stopvalidation`:
        - `start`:
        - `end`:
        """
        super(RangeValidationRule, self).__init__(stopvalidation=stopvalidation)
        self._start = int(start)
        self._end = int(end)

        if self._end < self._start:
            log = logging.getLogger()
            log.warning('start({}) larger than end({})'.format(self._start, self._end))
            self._start, self._end = self._end, self._start

    def get_start(self, ):
        """SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._start

    def set_start(self, start):
        """SUMMARY

        set_start(start)

        @Arguments:
        - `start`:

        @Return:

        @Error:
        """
        self._start = int(start)

    def get_end(self, ):
        """SUMMARY

        get_end()

        @Return:

        @Error:
        """
        return self._end

    def set_end(self, end):
        """SUMMARY

        set_end(end)

        @Arguments:
        - `end`:

        @Return:

        @Error:
        """
        self._end = int(end)

    def _get_message(self, value):
        """SUMMARY

        _get_message()

        @Return:

        @Error:
        """
        return u"{} と {} 内で入力してください。".format(self._start, self._end)

    def validate(self, value):
        """SUMMARY

        validate(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        if self._start < value < self._end:
            return ValidationResult(ValidationResult.VALIDATED, "")
        return ValidationResult(ValidationResult.INVALIDED, self._get_message(value))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# RangeValidationRule.py ends here
