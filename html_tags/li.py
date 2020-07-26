#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""li -- li tag

"""
from .html_tag import HtmlTag


class Li(HtmlTag):
    """Li

    Li is a HtmlTag.
    Responsibility:

    HTML の <li> 要素は、リストの項目を表すために用いられます。
    この要素は、その項目が属する順序付きリスト (<ol>)、順序なしリスト
    (<ul>)、メニュー (<menu>) のいずれかの子要素として配置する必要があります。
    メニュー要素および順序なしリスト内においては、
    リストの項目は通常、行頭文字伴って表示され、順序付きリスト内では、
    数字や文字による連番のリストマーカーを伴って表示されます。

    コンテンツカテゴリー	なし
    許可されている内容	フローコンテンツ
    タグの省略	直後に別の <li> 要素が続く場合、または他のリスト項目が続くことなく親要素が閉じられた場合は、終了タグが省略可能。
    許可されている親要素	<ul>、<ol>、<menu>。すでに廃止されているが、<dir> の子要素としても配置可能であった。
    許可されている ARIA ロール	menuitem, menuitemcheckbox, menuitemradio, option, presentation, radio, separator, tab, treeitem
    DOM インターフェイス	HTMLLIElement

    属性
    この要素にはグローバル属性があります。

    value
    これは整数値の属性で、 <ol> 要素で定義されたリスト項目の序数値を示します。
    リストがローマ数字や文字で表示される場合であっても、この属性は数値のみが指定できます。
    続くリスト項目は、その番号から続いて採番されます。
    順序なしリスト (<ul>) やメニュー (<menu>) では value 属性は意味がありません。
    メモ: この属性は HTML4 で非推奨とされましたが、 HTML5 で再導入されました。
    メモ: Gecko 9.0 以前では、負の値が誤って 0 に変換されていました。
    Gecko 9.0 からは、すべての整数値が正しく解析されます。

    type
    文字の属性で、表示するリストマーカーの種類を指定します。
    a: 小文字
    A: 大文字
    i: 小文字のローマ数字
    I: 大文字のローマ数字
    1: 数字
    もし親の <ol> 要素で使用されていた場合は、それよりも優先されます。
    使用上の注意: この属性は非推奨になっています。
    代わりにCSS の list-style-type プロパティを使用してください。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        VALUE = 'value'
        TYPE = 'type'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='li', tags=[], attrs=None, **kwargs)

    def set_value(self, value):
        """Set value attibutes value.

        set_value(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.AS, value)
        return self

    def get_value(self, ):
        """Get value attribute value.

        get_value()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.VALUE, None)

    def remove_value(self, ):
        """Remove value attribute value.

        remove_value()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.VALUE in self.attrs:
            del self.attrs[self.AttributeNames.VALUE]
        return self

    def set_type(self, value):
        """Set type attibutes value.

        set_type(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TYPE, value)
        return self

    def get_type(self, ):
        """Get type attribute value.

        get_type()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TYPE, None)

    def remove_type(self, ):
        """Remove type attribute value.

        remove_type()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TYPE in self.attrs:
            del self.attrs[self.AttributeNames.TYPE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# li.py ends here
