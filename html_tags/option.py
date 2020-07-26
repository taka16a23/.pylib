#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""option -- option tag

"""
from .html_tag import HtmlTag


class Option(HtmlTag):
    """Option

    Option is a HtmlTag.
    Responsibility:

    HTML の <option> 要素は、 <select> 要素、<optgroup> 要素、
    <datalist> 要素内で項目を定義するために使われます。
    したがって、<option> は HTML 文書でポップアップメニューのメニュー項目や、
    その他の項目の一覧を表すことができます。

    コンテンツカテゴリ	なし
    許可されている内容	エスケープされた文字 (例えば &eacute;) を含むテキスト
    タグの省略	開始タグは必須。直後に他の <option> 要素または <optgroup> 要素がある場合、または親要素が他に内容を持たない場合は終了タグを省略可能。
    許可されている親要素	<select> 要素、<optgroup> 要素、<menu> 要素。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLOptionElement

    属性
    この要素はグローバル属性を持ちます。

    disabled
    この論理属性を設定すると、選択肢が選択不能になります。
    多くのブラウザーはそのようなコントロールをグレーアウトで表示し、
    マウスクリックやフォーカスなど、いかなるイベントも受け付けなくなります。
    この属性を設定していなくても、祖先のいずれかが無効状態の <optgroup>
    要素である場合は無効化されます。

    label
    この属性は、選択肢の意味を示すラベル文字列です。
    label 属性を定義していない場合は、要素の文字列コンテンツが要素の値になります。

    selected
    この論理属性を設定すると、その選択肢が初期状態で選択されます。<option> 要素が multiple を設定していない <select> 要素の子孫である場合、<select> 要素内で1個の <option> だけが selected 属性を持てます。

    value
    この属性の内容は、フォームで送信する値を表します。値を送信するには、選択肢を選択しなければなりません。この属性を省略すると、 option 要素の中の文字列が値になります。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        DISABLED = 'disabled'
        LABEL = 'label'
        SELECTED = 'selected'
        VALUE = 'value'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='option', tags=[], attrs=None, **kwargs)

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

    def set_selected(self, ):
        """Set selected attribute.

        set_selected()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SELECTED, None)

    def remove_selected(self, ):
        """Remove selected attribute.

        set_selected()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SELECTED in self.attrs:
            del self.attrs[self.AttributeNames.SELECTED]
        return self

    def is_selected(self, ):
        """Check selected.

        is_selected()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.SELECTED not in self.attrs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# option.py ends here
