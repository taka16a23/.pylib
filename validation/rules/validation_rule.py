#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ValidationRule -- For rule of validation

"""
from validation.result.validation_result import ValidationResult


class ValidationRule(object):
    """ValidationRule

    ValidationRule is a object.
    Responsibility:
    """
    NOT_STOP_VALIDATION = 0
    STOP_VALIDATION = 1

    def __init__(self, stopvalidation=None):
        """

        @Arguments:
        - `message`:
        - `stopvalidation`:
        """
        stop = None
        if stopvalidation is not None:
            stop = stopvalidation
        self._stopvalidation = stop

    def validate(self, value):
        """SUMMARY

        validate(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        # require

        # do

        # ensure
        return ValidationResult(
            ValidationResult.INVALIDED, "Not implemented validation rule.")

    def status_stop_validation(self, ):
        """SUMMARY

        isstop()

        @Return:

        @Error:
        """
        return self._stopvalidation



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# validation_rule.py ends here
