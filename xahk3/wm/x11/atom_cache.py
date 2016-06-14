#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""atom_cache -- DESCRIPTION

"""


class NotAtomCachedError(StandardError):
    r"""NotAtomCachedError

    NotAtomCachedError is a StandardError.
    Responsibility:
    """
    def __init__(self, name):
        StandardError.__init__(self)
        self._name = name

    def __str__(self):
        return 'Atom name "{}" not cached.'.format(self._name)


class AtomCache(object):
    """AtomCache

    AtomCache is a object.
    Responsibility: Atom を cache する。

    # TODO: (Atami) [2015/07/15]
    X11 のAtom をcache する。
    AtomName からAtom へ変換し保持する。
    Atom がcache されていない場合、XServer へリクエストし新にcache して返す。
    `disallow_uncached_atoms' を呼ぶとAtom がcache されていない場合、
    `NotAtomCachedError' を raise する。
    """
    # Attributes:
    def __init__(self, display, names):
        r"""

        # TODO: (Atami) [2015/07/15]
        @Arguments:
        - `display`: (xcb.Connection)
        - `names`: (list) default atom names string list
        """
        self._display = display
        self._cached_atoms = {}
        self._uncached_atoms_allowed = True

        cookies = []
        append = cookies.append
        for name in names:
            append(
                (name, self._display.core.InternAtom(False, len(name), name)))
        for name, cookie in cookies:
            self._cached_atoms[name] = cookie.reply().atom

    # Operations
    def get_atom(self, name):
        r"""Identify atom from name string.

        # TODO: (Atami) [2015/07/15]
        もしcache されていたらxserverに問合せずにcacheからかえす。
        cache されていない場合、２パターンある。
        １つは、cache して返す。
        ２つ目は、error を返す。

        get_atom(name)

        @Arguments:
        - `name`: (str) atom name

        @Return:
        (int) Atom number

        @Error:
        NotAtomCachedError
        if _uncached_atoms_allowed is True and not cached will raise error.
        """
        atom = self._cached_atoms.get(name, None)
        if atom is not None:
            return atom
        if self._uncached_atoms_allowed:
            atom = self._display.core.InternAtom(
                False, len(name), name).reply().atom
            self._cached_atoms[name] = atom
            return atom
        raise NotAtomCachedError(name)

    def list_atoms(self, names):
        r"""Identify atom from name string list.

        # TODO: (Atami) [2015/07/15]
        list_atoms(names)

        @Arguments:
        - `names`: (list) name string list

        @Return:
        (list) atoms

        @Error:
        NotAtomCachedError
        """
        return [self.get_atom(name) for name in names]

    def disallow_uncached_atoms(self):
        r"""Set raise flag for if not cached atom request.

        # TODO: (Atami) [2015/07/15]
        disallow_uncached_atoms()

        @Return:
        (None)

        @Error:
        """
        self._uncached_atoms_allowed = False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atom_cache.py ends here
