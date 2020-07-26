#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""progress -- progress tag

"""
from .html_tag import HtmlTag


class Progress(HtmlTag):
    """Progress

    Progress is a HtmlTag.
    Responsibility:

    HTML の <progress> 要素は、タスクの進捗状況を表示します。
    プログレスバーとしてよく表示されます。

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ、ラベル付け可能コンテンツ、知覚可能コンテンツ
    許可されている内容	記述コンテンツ。ただし、子要素に <progress> 要素を含めてはならない。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツ を受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLProgressElement

    属性
    この要素にはグローバル属性があります。

    max
    この属性は、progress 要素で示すタスクで必要とする総作業量を設定します。max 属性を指定する場合は、値を 0 より大きい有効な浮動小数点数値にしなければなりません。既定値は 1 です。

    value
    この属性は、タスクの進捗状況を設定します。値は 0 から max までの間、または max を省略する場合は 0 から 1 までの間の、有効な浮動小数点数値であることが必要です。value 属性がない場合は、プログレスバーは不定、タスクは処理中であるものの完了までが予想できない状態になります。
    メモ: 最小値は常に 0 であり、min 属性は progress 要素で許可されていません。-moz-orient CSS プロパティを使用して、プログレスバーを水平方向に表示する (既定値) か垂直方向に表示するかを指定できます。

    メモ: :indeterminate 疑似クラスは、不定状態のプログレスバーにマッチします。プログレスバーを値がある状態から不定の状態に変更するには、element.removeAttribute("value") で value 属性を削除しなければなりません。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        MAX = 'max'
        VALUE = 'value'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='progress', tags=[], attrs=None, **kwargs)

    def set_max(self, value):
        """Set max attribute.

        set_max(value)

        @Arguments:
        - `value`: max value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MAX, value)

    def remove_max(self, ):
        """Remove max attribute.

        remove_max()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.MAX)
        return self

    def get_max(self, ):
        """Get max attribute.

        get_max()

        @Return: (str) accept value.

        @Error:
        """
        if self.AttributeNames.MAX not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.MAX])

    def set_value(self, value):
        """Set value attribute.

        set_value(value)

        @Arguments:
        - `value`: value value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.VALUE, value)

    def remove_value(self, ):
        """Remove value attribute.

        remove_value()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.VALUE)
        return self

    def get_value(self, ):
        """Get value attribute.

        get_max()

        @Return: (str) accept value.

        @Error:
        """
        if self.AttributeNames.VALUE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.VALUE])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# progress.py ends here
