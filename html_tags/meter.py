#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""meter -- meter tag

"""
from .html_tag import HtmlTag


class Meter(HtmlTag):
    """Meter

    Meter is a HtmlTag.
    Responsibility:

    HTML の <meter> 要素は、既知の範囲内のスカラー値、または小数値を表します。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, ラベル付け可能コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ。ただし他の <meter> 要素の子孫要素として配置してはならない。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLMeterElement

    属性
    他のすべての要素と同様に、この要素はグローバル属性を持ちます。

    value
    現在の数値。min 属性と max 属性が指定されている場合、
    これらの表す範囲内に収まる値でなくてはなりません。
    この value 属性が未定義、あるいは不正な値であった場合は、
    その値は "0" となります。
    指定されている値が min 属性と max 属性が示す範囲の範囲外の値である場合、
    その範囲の内のもっとも近い値が適用されます。
    使用上の注意: value 属性の値が 0 を下限、1 を上限とするものでない限り、
    min 属性および max 属性で value 属性の下限および上限を定義しなくてはなりません。

    min
    範囲全体の下限。 max 属性により上限が設定されている場合は、
    それより小さい値でなくてはなりません。
    未設定の場合、下限値は 0 となります。

    max
    範囲全体の上限。 min 属性により下限が設定されている場合は、
    それより大きい値でなくてはなりません。
    未設定の場合、上限値は 1 となります。

    low
    「低」とされる範囲全体の上限値。属性値は、min 属性の値より大きく、
    かつ high 属性および max 属性の値より小さいものでなくてはなりません
    (※これらが定義されている場合)。low が未定義、
    もしくはその値が min 属性の値より小さい場合、low の値は最小値と同じです。

    high
    「高」とされる範囲全体の下限値。属性値は、max 属性の値より小さく、
    かつ low 属性や min 属性の値より大きいものでなくてはなりません
    (※これらが定義されている場合)。high 属性が未定義、
    もしくはその値が max 属性の値より大きい場合、high の値は最大値と同じです。

    optimum
    最適な数値の範囲を表します。min 属性と max
    属性によって定義される範囲内の値でなくてはなりません。
    low 属性と high 属性が指定されている場合、
    この属性の値を含む範囲が最適な数値の範囲とみなされます。
    例えば optinum 属性の値が min 属性と low 属性の間のいずれかである場合、
    「低」の範囲が最適な数値となります。

    form
    meter 要素の属するフォーム (form owner) の id を指定します。
    例えばフォームの input 要素 (<input type="number" />)
    の範囲を表す用途で meter 要素を用いている場合、
    このフォームの id を指定します。
    対象がフォーム関連要素である場合にのみこの属性を使用可能です。
    meter 要素が関連するフォームの子孫要素として配置されているのなら、
    そのメーターは自動的にそのフォームに属するものとなり、この属性は省略可能です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        VALUE = 'value'
        MIN = 'min'
        MAX = 'max'
        LOW = 'low'
        HIGH = 'high'
        OPTIMUM = 'optimum'
        FORM = 'form'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='a', tags=[], attrs=None, **kwargs)

    def set_value(self, value):
        """Set value attibutes value.

        set_value(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.VALUE, value)
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

    def set_min(self, value):
        """Set min attibutes value.

        set_min(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.MIN, value)
        return self

    def get_min(self, ):
        """Get min attribute value.

        get_min()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MIN, None)

    def remove_min(self, ):
        """Remove value attribute value.

        remove_value()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MIN in self.attrs:
            del self.attrs[self.AttributeNames.MIN]
        return self

    def set_max(self, value):
        """Set max attibutes value.

        set_max(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.MAX, value)
        return self

    def get_max(self, ):
        """Get max attribute value.

        get_max()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MAX, None)

    def remove_max(self, ):
        """Remove max attribute value.

        remove_max()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MAX in self.attrs:
            del self.attrs[self.AttributeNames.MAX]
        return self

    def set_low(self, value):
        """Set low attibutes value.

        set_low(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.LOW, value)
        return self

    def get_low(self, ):
        """Get low attribute value.

        get_low()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LOW, None)

    def remove_low(self, ):
        """Remove low attribute value.

        remove_low()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LOW in self.attrs:
            del self.attrs[self.AttributeNames.LOW]
        return self

    def set_hight(self, value):
        """Set hight attibutes value.

        set_hightl(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.HIGHT, value)
        return self

    def get_hight(self, ):
        """Get hight attribute value.

        get_hight()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HIGHT, None)

    def remove_hight(self, ):
        """Remove hight attribute value.

        remove_hightl()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HIGHT in self.attrs:
            del self.attrs[self.AttributeNames.HIGHT]
        return self

    def set_optimum(self, value):
        """Set optimum attibutes value.

        set_optimum(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.OPTIMUM, value)
        return self

    def get_optimum(self, ):
        """Get optimum attribute value.

        get_optimum()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.OPTIMUM, None)

    def remove_optimum(self, ):
        """Remove optimum attribute value.

        remove_optimum()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.OPTIMUM in self.attrs:
            del self.attrs[self.AttributeNames.OPTIMUM]
        return self

    def set_form(self, value):
        """Set form attibutes value.

        set_form(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.FORM, value)
        return self

    def get_form(self, ):
        """Get form attribute value.

        get_form()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORM, None)

    def remove_form(self, ):
        """Remove form attribute value.

        remove_form()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORM in self.attrs:
            del self.attrs[self.AttributeNames.FORM]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# meter.py ends here
