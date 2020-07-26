#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dialog -- dialog tag

"""
from .html_tag import HtmlTag


class Dialog(HtmlTag):
    """Dialog

    Dialog is a HtmlTag.
    Responsibility:

    HTML の <dialog> 要素は、ダイアログボックスや、消すことができるアラート、
    インスペクター、サブウィンドウ等のような対話的コンポーネントを表します。

    コンテンツカテゴリ	フローコンテンツ, 区分化ルート
    許可された内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可された親要素	フローコンテンツを受け入れるあらゆる要素
    暗黙の ARIA ロール	dialog
    許可された ARIA ロール	alertdialog
    DOM インターフェイス	HTMLDialogElement

    tabindex 属性を <dialog> 要素で使用してはいけません。

    open
    ダイアログがアクティブで操作で使用できることを示します。
    open 属性が設定されていないときは、
    ダイアログはユーザーに表示するべきではありません。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        open
        ダイアログがアクティブで操作で使用できることを示します。
        open 属性が設定されていないときは、
        ダイアログはユーザーに表示するべきではありません。
        """
        OPEN = 'open'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='dialog', tags=[], attrs=None, **kwargs)

    # override for disable this method
    def set_tabindex(self, value):
        """Do not use tabindex

        set_tabindex(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        raise NotImplemented('tabindex 属性を <dialog> 要素で使用してはいけません。')

    def enable_open(self, ):
        """Enable open.

        enable_open()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.OPEN, '')

    def disable_open(self, ):
        """Disable open.

        disable_open()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.OPEN in self.attrs:
            del self.attrs[self.AttributeNames.OPEN]
        return self

    def is_open(self, ):
        """Check open enabled.

        is_open()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.OPEN in self.attrs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dialog.py ends here
