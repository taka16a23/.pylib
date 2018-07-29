#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ValidationResult -- for result validate

"""


class ValidationResult(object):
    """BaseValidationResult

    BaseValidationResult is a object.
    Responsibility:
    """
    INVALIDED = 0
    VALIDATED = 1

    def __init__(self, isvalid, message):
        """

        @Arguments:
        - `isvalid`: INVALIDED/VALIDED
        - `message`: message for error
        """
        self._isvalid = isvalid
        self._message = message
        self._next = None

    def has_next(self, ):
        """Check has next result

        has_next()

        @Return:
        True if exists next or False is not exists
        """
        if self._next is None:
            return False
        return True

    def set_next(self, validation_result):
        """Set next validation result

        set_next(validation_result)

        @Arguments:
        - `validation_result`:

        @Return:
        None

        @Error:
        TypeError if validation_result is not ValidationResult
        """
        # check type of argument
        if not isinstance(validation_result, (ValidationResult, )):
            raise TypeError('validation_result require ValidationResult got {}'
                            .format(type(validation_result)))
        if self._next is None:
            self._next = validation_result
            return
        self._next.set_next(validation_result)

    def isvalid(self, ):
        """Check validated

        isvalid()

        @Return:
        True/False
        """
        if self._isvalid == self.INVALIDED:
            return False
        if self._next is None:
            return True
        # next is not None
        return self._next.isvalid()

    def get_messages(self, ):
        """List invalided messages.

        get_messages()

        @Return:
        List
        """
        messages = []
        if self._isvalid == self.INVALIDED:
            messages.append(self._message)
        if self._next is None:
            return messages
        messages.extend(self._next.get_messages())
        return messages

    def list_results(self, ):
        """List of ValidationResult

        list_results()

        @Return:
        List
        """
        results = []
        results.append(self)
        if self._next is not None:
            results.extend(self._next.list_results())
        return results



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ValidationResult.py ends here
