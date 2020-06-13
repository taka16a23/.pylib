#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""typecheck -- typecheck

"""


def typecheck(a_value, a_arg_name, a_instances=[]):
    """TypeCheck values

    typecheck(a_value, a_arg_name, a_instances=[])

    @Arguments:
    - `a_value`: target type check value
    - `a_arg_name`: argument name for message
    - `a_instances`: check instance

    @Return:

    @Error:
    """
    if isinstance(a_value, a_instances):
        return
    t_results = []
    for instance in a_instances:
        t_results.append('{0.__class__.__name__}'.format(instance))
    raise TypeError(
        '{} must be {}. got({0.__class__.__name__})'
        .format(a_arg_name, ','.join(t_results), a_value))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# typechecker.py ends here
