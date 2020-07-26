#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ol -- ol tag

"""
from .html_tag import HtmlTag


class Ol(HtmlTag):
    """Ol

    Ol is a HtmlTag.
    Responsibility:

    HTML の <ol> 要素は、項目の順序付きリストを表し、
    ふつうは番号付きのリストとして表示されます。

    コンテンツカテゴリ	フローコンテンツ。また、<ol> 要素の子に少なくとも 1 個の <li> 要素を包含する場合は、知覚可能コンテンツ。
    許可されている内容	0個以上の <li> または <script> 、 <template> 要素。 <li> 要素の子孫としてさらに <ol> 要素や <ul> 要素を配置することも可能。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	directory, group, listbox, menu, menubar, radiogroup, tablist, toolbar, tree, presentation
    DOM インターフェイス	HTMLOListElement

    compact
    この真偽値を持つ属性は、リストをコンパクトなスタイルで描画すべきというヒントを提供します。
    この属性の解釈はユーザーエージェントに依存するため、
    すべてのブラウザーで動作するわけではありません。
    警告: この属性は非推奨のため使用してはいけません。
    代わりに CSS を使用してください。
    compact 属性と似た効果を得るには、 CSS プロパティの line-height を使用し、
    値を 80% にしてください。

    reversed HTML5
    論理属性で、リストの項目が逆順で指定されていることを指定します。
    項目は大きい方から小さい方へ番号付けされます。

    start HTML5
    整数値を持つ属性で、リスト項目の序数の開始値を指定します。
    この値は、番号付けの種類が文字やローマ数字であっても、
    常にアラビア数字 (1, 2, 3, など) で指定します。
    例えば、 "d" の文字や "iv" のローマ数字から始める場合は、
    start="4" を使用してください。
    メモ: この属性は HTML4 で非推奨になりましたが、 HTML5 で再び導入されました。

    type
    この属性は、番号付けの種類を設定します。
    'a' は、英小文字を示します
    'A' は、英大文字を示します
    'i' は、小文字のローマ数字を示します
    'I' は、大文字のローマ数字を示します
    '1' は、数字を示します (既定値)
    指定された種類は、内部の <li> 要素で異なる type 属性が使用されない限り、
    リスト全体に使用されます。

    メモ: この属性は HTML4 で非推奨になりましたが、HTML5 で再び導入されました。

    (法律文書や技術文書の箇条書きなどのように) リスト番号の値に重要性ががない限り、
    代わりに CSS の list-style-type プロパティを使用してください。

    使用上の注意
    ふつう、順序付きリストの項目は、先頭に数字、文字、点などのマーカーが表示されます。
    マーカーの種類は CSS の list-style-type プロパティを使用して指定することができます。
    <ol> 要素と <ul> 要素は、必要なだけ深く入れ子にすることができます。
    さらに言えば、入れ子になったリストが <ol> と <ul> の間で変化することに
    で制限はありません。
    <ol> と <ul> は、どちらも項目のリストを表します。
    両者の違いは、 <ol> 要素では順序に意味があることです。
    使い分けの目安としては、項目の順序を変更してみてください。
    意味が変わるようであれば <ol> 要素を使用し、そうでない場合は、
    <ul> 要素を使用することができます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        COMPACT = 'compact'
        REVERSED = 'reversed'
        START = 'start'
        TYPE = 'type'

    class Type(object):
        """Type

        Type is a object.
        Responsibility:
        """
        ALPHA_LOWER = 'a'
        ALPHA_UPPER = 'A'
        ROMAN_LOWER = 'i'
        ROMAN_UPPER = 'I'
        NUMBER = '1'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='ol', tags=[], attrs=None, **kwargs)

    def set_compact(self, ):
        """Set compact attribute.

        set_compact()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.COMPACT, None)

    def is_compact(self, ):
        """Check compact.

        is_compact()

        @Return: True if exists compact attribute

        @Error:
        """
        return self.AttributeNames.COMPACT not in self.attrs

    def remove_compact(self, ):
        """Remove compact attribute value.

        remove_label()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.COMPACT in self.attrs:
            del self.attrs[self.AttributeNames.COMPACT]
        return self

    def set_reversed(self, ):
        """Set reversed attribute.

        set_reversed()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.REVERSED, None)

    def is_reversed(self, ):
        """Check reversed.

        is_reversed()

        @Return: True if exists reversed attribute

        @Error:
        """
        return self.AttributeNames.REVERSED not in self.attrs

    def remove_reversed(self, ):
        """Remove reversed attribute value.

        remove_reversed()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.REVERSED in self.attrs:
            del self.attrs[self.AttributeNames.REVERSED]
        return self

    def set_start(self, value):
        """Set start attibutes value.

        set_start(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.START, value)
        return self

    def get_start(self, ):
        """Get start attribute value.

        get_start()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.START, None)

    def remove_start(self, ):
        """Remove start attribute value.

        remove_start()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.START in self.attrs:
            del self.attrs[self.AttributeNames.START]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ol.py ends here
