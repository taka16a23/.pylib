#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""td -- td tag

"""
from .html_tag import HtmlTag


class td(HtmlTag):
    """td

    td is a HtmlTag.
    Responsibility:

    HTML の <td> 要素は、表でデータを包含するセルを定義します。
    これは表モデルに関与します。

    コンテンツカテゴリ	区分化ルート
    許可されている内容	フローコンテンツ
    タグの省略	開始タグは必須です。
    直後に <th> 要素または <td> 要素がある場合、または親要素内で以降のデータがない場合は終了タグを省略可能。
    許可されている親要素	<tr> 要素
    暗黙の ARIA ロール	cell (<table> 要素の子孫である場合)
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTableDataCellElement

    属性
    この要素にはグローバル属性があります。

    colspan
    この属性はセルをいくつの列に広げるかを示す、負でない整数を持ちます。
    既定値は 1 です。1000 を超える値は正しくないとみなされ、
    既定値 (1) が設定されるでしょう。

    headers
    この属性は、空白文字で区切られた文字列のリストを持ちます。
    各々の文字列は、この要素に当てはめる <th> 要素の id 属性と対応します。

    rowspan
    この属性はセルをいくつの行に広げるかを示す、負でない整数を持ちます。
    デフォルト値は 1 です。
    0 を設定した場合は、セルが属する表セクション (<thead>, <tbody>, <tfoot>)
    の終端 (暗黙的に定義されるものであっても) まで拡張します。
    65534 より大きな値は、65534 に切り詰めます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        COLSPAN = 'colspan'
        HEADERS = 'headers'
        ROWSPAN = 'rowspan'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='td', tags=[], attrs=None, **kwargs)

    def set_colspan(self, value):
        """Set colspan attibutes value.

        set_colspan(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.COLSPAN, value)
        return self

    def get_colspan(self, ):
        """Get colspan attribute value.

        get_colspan()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.COLSPAN, None)

    def remove_colspan(self, ):
        """Remove colspan attribute value.

        remove_colspan()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.COLSPAN in self.attrs:
            del self.attrs[self.AttributeNames.COLSPAN]
        return self

    def get_headers(self, ):
        """Get headers attribute values.

        get_headers()

        @Return: attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HEADERS, None)

    def append_headers(self, key):
        """Append headers.

        append_headers(key)

        @Arguments:
        - `key`: headers

        @Return: this instance.

        @Error:
        """
        self.append_attribute_value(self.AttributeNames.HEADERS, key)
        return self

    def remove_headers(self, key):
        """Remove headers.

        remove_headers(key)

        @Arguments:
        - `key`: headers

        @Return: this instance.

        @Error:
        """
        self.remove_attribute_value(self.AttributeNames.HEADERS, key)
        return self

    def clear_headers(self, ):
        """Clear headers.

        clear_headers()

        @Return: this instance.

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.HEADERS)
        return self

    def delete_headers(self, ):
        """Delete headers from attribute.

        delete_headers()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HEADERS in self.attrs:
            del self.attrs[self.AttributeNames.HEADERS]
        return self

    def contains_headers(self, key):
        """Contains headers.

        contains_headers(key)

        @Arguments:
        - `key`: headers

        @Return: Return True if exists. Else False.

        @Error:
        """
        return self.contains_attribute_value(self.AttributeNames.HEADERS, key)

    def set_rowspan(self, value):
        """Set rowspan attibutes value.

        set_rowspan(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ROWSPAN, value)
        return self

    def get_rowspan(self, ):
        """Get rowspan attribute value.

        get_rowspan()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ROWSPAN, None)

    def remove_rowspan(self, ):
        """Remove rowspan attribute value.

        remove_rowspan()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ROWSPAN in self.attrs:
            del self.attrs[self.AttributeNames.ROWSPAN]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# td.py ends here
