#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""th -- th tag

"""
from .html_tag import HtmlTag


class th(HtmlTaq):
    """th

    th is a HtmlTaqg.
    Responsibility:

    HTML の <th> 要素は、表のセルのグループ用のヘッダーであるセルを定義します。
    このグループの性質は、scope 属性と headers 属性で定義します。

    コンテンツカテゴリ	なし
    許可されている内容	フローコンテンツ、ただしヘッダー、フッター、区分コンテンツ、見出しコンテンツを除く。
    タグの省略	開始タグは必須です。
    直後に <th> 要素または <td> 要素がある場合、または親要素内で以降のデータがない場合は終了タグを省略可能。
    許可されている親要素	<tr> 要素
    暗黙の ARIA ロール	columnheader or rowheader
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTableHeaderCellElement

    属性
    この要素にはグローバル属性があります。

    abbr
    この属性は、セルの内容の簡潔な説明を持ちます。読み上げソフトなど一部のユーザーエージェントは、内容自体の前にこの説明を提供することがあります。
    colspan
    この属性はセルをいくつの列に広げるかを示す、負でない整数を持ちます。既定値は 1 です。1000 を超える値は正しくないとみなされ、既定値 (1) が設定されるでしょう。
    headers
    この属性は、空白文字で区切られた文字列のリストを持ちます。各々の文字列は、この要素に当てはめる <th> 要素の id 属性と対応します。
    rowspan
    この属性はセルをいくつの行に広げるかを示す、負でない整数を持ちます。既定値は 1 です。0 を設定した場合は、セルが属する表セクション (<thead>, <tbody>, <tfoot>, 暗黙的に定義されたものも含む) の終端まで拡張します。 65534 より大きな値は、 65534 に切り詰めます。
    scope
    これは列挙型の属性で、この (<th> で定義されている) 見出し要素が関連するセルを定義します。次の値を取ることができます。
    row: この見出しはその行に属するすべてのセルに関連します。
    col: この見出しはその列に属するすべてのセルに関連します。
    rowgroup: この見出しは行グループに属し、その中のすべてのセルに関連します。これらのセルは <table> 要素の dir 属性の値によって、見出しの右又は左に配置されます。
    colgroup: この見出しは列グループに属し、その中のすべてのセルに関連します。.
    auto
    この属性が指定されなかった場合の既定値は auto です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        ABBR = 'abbr'
        COLSPAN = 'colspan'
        HEADERS = 'headers'
        ROWSPAN = 'rowspan'
        SCOPE = 'scope'
        AUTO = 'auto'

    class Scope(object):
        """Scope

        Scope is a object.
        Responsibility:
        """
        ROW = 'row'
        COL = 'COL'
        ROWGROUP = 'ROWGROUP'
        COLGROUP = 'COLGROUP'
        AUTO = 'auto'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='th', tags=[], attrs=None, **kwargs)

    def set_abbr(self, value):
        """Set abbr attibutes value.

        set_abbr(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ABBR, value)
        return self

    def get_abbr(self, ):
        """Get abbr attribute value.

        get_abbr()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ABBR, None)

    def remove_abbr(self, ):
        """Remove abbr attribute value.

        remove_abbr()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ABBR in self.attrs:
            del self.attrs[self.AttributeNames.ABBR]
        return self

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

    def set_scope(self, value):
        """Set scope attibutes value.

        set_scope(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.SCOPE, value)
        return self

    def get_scope(self, ):
        """Get scope attribute value.

        get_scope()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SCOPE, None)

    def remove_scope(self, ):
        """Remove scope attribute value.

        remove_scope()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SCOPE in self.attrs:
            del self.attrs[self.AttributeNames.SCOPE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# th.py ends here
