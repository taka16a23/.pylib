#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ins -- ins tag

"""
from .html_tag import HtmlTag


class Ins(HtmlTag):
    """Ins

    Ins is a HtmlTag.
    Responsibility:

    HTML の <ins> 要素は、文書に追加されたテキストの範囲を表します。

    コンテンツカテゴリ	記述コンテンツ または フローコンテンツ
    許可されている内容	透過的コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLModElement

    cite
    会議の議事録やトラブルシューティングシステムのチケットといった、
    追加についての説明を記したリソースへの URI を示す。
    datetime
    追加日時を示す。値は、正確な指定
    （※原題 : valid date with an optional time string） でなくてはなりません。
    記述ミスあるいは未記入によって属性値が解析できない場合には、
    要素に関連付けられたタイムスタンプはないものと解釈されます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        CITE = 'cite'
        DATETIME = 'datetime'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='ins', tags=[], attrs=None, **kwargs)

    def set_cite(self, value):
        """Set cite.

        set_cite(value)

        @Arguments:
        - `value`: cite value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CITE, value)

    def get_cite(self, ):
        """Get cite attribute value.

        get_cite()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CITE, None)

    def remove_cite(self, ):
        """Remove cite attribute.

        remove_cite()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CITE in self.attrs:
            del self.attrs[self.AttributeNames.CITE]
        return self

    def set_datetime(self, value):
        """Set datetime.

        set_datetime(value)

        @Arguments:
        - `value`: datetime value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DATETIME, value)

    def get_datetime(self, ):
        """Get datetime attribute value.

        get_datetime()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DATETIME, None)

    def remove_datetime(self, ):
        """Remove datetime attribute.

        remove_datetime()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DATETIME in self.attrs:
            del self.attrs[self.AttributeNames.DATETIME]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ins.py ends here
