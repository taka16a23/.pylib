#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""del -- del tag

"""
from .html_tag import HtmlTag


class Del(HtmlTag):
    """Del

    Del is a HtmlTag.
    Responsibility:

    HTML の <del> 要素は、文書から削除された文字列の範囲を表します。
    これは例えば、「変更の追跡」や、ソースコードの差分情報を描画するときに使用することができます。
    <ins> 要素は逆の目的に、文書に追加された文字列を示すために用いることができます。

    一般的にこの要素は (必ずではありませんが) 打ち消し線のスタイルを伴って描画されます。

    コンテンツカテゴリ	記述コンテンツ または フローコンテンツ
    許可されている内容	透過的コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLModElement
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        cite
        変更についての説明を記したリソース（例えば、議事録など）への URI を示す。
        datetime
        この属性は変更日時を示し、有効な日付文字列と任意の
        時刻文字列でなくてはなりません。
        値を時刻および日付の文字列として解釈できない場合は、
        要素に関連付けられたタイムスタンプはないものと解釈されます。
        日付のない文字列の書式については、日付の文字列を参照してください。
        日付と時刻の両方を含んだ文字列の書式は、地方時の日付と時刻の文字列にあります。
        """
        CITE = 'cite'
        DATETIME = 'datetime'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='del', tags=[], attrs=None, **kwargs)

    def set_cite(self, value):
        """Set cite.

        set_cite(value)

        @Arguments:
        - `value`: cite attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.CITE, value)
        return self

    def get_cite(self, ):
        """Get cite attribute value.

        get_cite()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CITE, None)

    def remove_cite(self, ):
        """Remove cite attribute value.

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
        - `value`: datetime attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DATETIME, value)
        return self

    def get_datetime(self, ):
        """Get datetime attribute value.

        get_datetime()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DATETIME, None)

    def remove_datetime(self, ):
        """Remove datetime attribute value.

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
# del.py ends here
