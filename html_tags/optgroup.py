#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""optgroup -- optgroup tag

"""
from .html_tag import HtmlTag


class OptGroup(HtmlTag):
    """OptGroup

    OptGroup is a HtmlTag.
    Responsibility:

    HTML の <optgroup> 要素は、ウェブフォームにおいて <select> 要素内の、
    選択肢 (<option>) のグループを作成します。

    コンテンツカテゴリ	なし
    許可されている内容	0 個以上の <option> 要素
    タグの省略	開始タグは必須。要素の直後に他の <optgroup> 要素が接続する場合、または親要素が他の内容を持たない場合、終了タグが省略可能となる。
    許可されている親要素	<select> 要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLOptGroupElement

    属性
    この要素にはグローバル属性があります。

    disabled
    この論理属性が指定された場合、このオプショングループ内の項目のいずれも選択不能となります。
    多くの場合、ブラウザーはそのコントロールをグレーアウトで表示し、
    マウスクリックやフォーカスなど、いかなるイベントも受け付けなくなります。

    label
    ブラウザーがユーザーインターフェイス上の選択肢にラベル付けするのに使用できる
    オプションのグループの名前。この要素を使用する場合には、この属性は必須です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        DISABLED = 'disabled'
        LABEL = 'label'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='optgroup', tags=[], attrs=None, **kwargs)

    def disable(self, ):
        """Disable as set disable attribute.

        disable()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLED, None)

    def enable(self, ):
        """Enable as remove enable attribute.

        enable()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

    def is_enable(self, ):
        """Check enabled.

        is_enable()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.DISABLED not in self.attrs

    def set_label(self, value):
        """Set label attibutes value.

        set_label(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.LABEL, value)
        return self

    def get_label(self, ):
        """Get label attribute value.

        get_label()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LABEL, None)

    def remove_label(self, ):
        """Remove label attribute value.

        remove_label()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LABEL in self.attrs:
            del self.attrs[self.AttributeNames.LABEL]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# optgroup.py ends here
