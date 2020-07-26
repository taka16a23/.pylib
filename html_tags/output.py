#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""output -- output tag

"""
from .html_tag import HtmlTag


class Output(HtmlTag):
    """Output

    Output is a HtmlTag.
    Responsibility:

    HTML の出力要素 (<output>) は、サイトやアプリが計算結果や
    ユーザー操作の結果を挿入することができるコンテナー要素です。

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ、フォーム関連要素 (リスト化、ラベル付け可能、リセット可能)、知覚可能コンテンツ
    許可された内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可された親要素	記述コンテンツを受け入れるすべての要素
    許可された ARIA ロール	すべて
    DOM インターフェイス	HTMLOutputElement

    属性
    この要素にはグローバル属性があります。

    for
    他の要素の id の空白区切りのリストで、入力値が計算に使用される
    (または何らかの影響を与える) 要素を示します。

    form
    この要素に関連付けられた ("form owner" である) form 要素 を指定します。
    この値は、同じ文書内の <form> 要素の id である必要があります。
    <output> 要素が form 要素の子孫である場合
    (そしてその <form> 要素が form owner である場合)、
    または <output> 要素が全くフォームと関連付けられていない場合は、
    この属性は必要ありません。

    name
    要素の名前です。フォームの送信の際に、この <output> を識別するために使用します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        FOR = 'for'
        FORM = 'form'
        name = 'name'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='output', tags=[], attrs=None, **kwargs)

    def get_for(self, ):
        """Get for attribute values.

        get_for()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FOR, None)

    def append_for(self, value):
        """Append for values.

        append_for(value)

        @Arguments:
        - `value`:

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.FOR, value)
        return self

    def remove_for(self, value):
        """Remove for value.

        remove_for(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.FOR, value)
        return self

    def clear_autocomplete(self, ):
        """Clear autocomplete.

        clear_autocomplete()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.AUTOCOMPLETE)
        return self

    def delete_for(self, ):
        """Delete for.

        delete_for()

        @Return: this instance

        @Error:
        """
        self.remove_attribute(self.AttributeNames.FOR)
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# output.py ends here
