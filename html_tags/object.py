#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""object -- object tag

"""
from .html_tag import HtmlTag


class Object(HtmlTag):
    """Object

    Object is a HtmlTag.
    Responsibility:

    HTML の <object> 要素は、画像、内部の閲覧コンテキスト、
    プラグインによって扱われるリソースなどのように扱われる外部リソースを表現します。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 埋め込みコンテンツ, 知覚可能コンテンツ、要素が usemap 属性を持つ場合は 対話型コンテンツ, リスト化/送信可能 な フォーム関連要素
    許可されている内容	0個以上の <param> 要素とそれに続く 透過的コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	埋め込みコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	application, document, image
    DOM インターフェイス	HTMLObjectElement

    data
    リソースのアドレスを有効な URL で指定。
    data 属性と type 属性のうち、少なくとも1つは定義しておく必要があります。
    この論理属性は属性名を指定するだけで有効になります。オブジェクトは、後続する
    <object> 要素でインスタンス化しなければなりません。
    HTML5 ではリソースを再利用するごとに、完全な形の <object> 要素を繰り返し配置します。
    formHTML5
    オブジェクトがフォームに関連付けられている場合、そのフォーム（※フォームオーナー）の id を指定。属性値は、同一文書内の <form> 要素の id でなければなりません。

    height
    表示されるリソースの高さを CSS ピクセル値 で指定。(絶対値に限ります。パーセント値は不可)

    name
    有効な閲覧コンテキストの名前 (HTML5) またはコントロールの名前 (HTML 4)。

    type
    data 属性によって指定されたリソースの content type。data 属性と type 属性のうち、
    少なくとも 1 つは定義しておく必要があります。
    typemustmatchHTML5
    この論理属性は、リソースを使用するためには type 属性の値とリソースの実際の
    content type が一致していなければならないかを示します。
    usemap
    <map> 要素を参照するハッシュ名。
    '#' の後に map 要素の name 属性を繋げた文字列を属性値として記述します。
    width
    表示されるリソースの幅を CSS ピクセル値 で指定。(絶対値に限ります。パーセンテージは不可)
    """
    class AttributeNames(HtmlTag.AttributeNames):
        DATA = 'data'
        HEIGHT = 'height'
        WIDTH = 'width'
        NAME = 'name'
        TYPE = 'type'
        USEMAP = 'usemap'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='object', tags=[], attrs=None, **kwargs)

    def set_data(self, value):
        """Set data attibutes value.

        set_data(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DATA, value)
        return self

    def get_data(self, ):
        """Get data attribute value.

        get_data()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DATA, None)

    def remove_data(self, ):
        """Remove data attribute value.

        remove_data()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DATA in self.attrs:
            del self.attrs[self.AttributeNames.DATA]
        return self

    def set_height(self, value):
        """Set height attibutes value.

        set_height(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.HEIGHT, value)
        return self

    def get_height(self, ):
        """Get height attribute value.

        get_height()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HEIGHT, None)

    def remove_height(self, ):
        """Remove height attribute value.

        remove_height()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HEIGHT in self.attrs:
            del self.attrs[self.AttributeNames.HEIGHT]
        return self

    def set_width(self, value):
        """Set width attibutes value.

        set_width(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.WIDTH, value)
        return self

    def get_width(self, ):
        """Get width attribute value.

        get_width()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.WIDTH, None)

    def remove_width(self, ):
        """Remove width attribute value.

        remove_width()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.WIDTH in self.attrs:
            del self.attrs[self.AttributeNames.WIDTh]
        return self

    def set_name(self, value):
        """Set name attibutes value.

        set_name(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.NAME, value)
        return self

    def get_name(self, ):
        """Get name attribute value.

        get_name()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name(self, ):
        """Remove name attribute value.

        remove_name()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
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

    def set_usemap(self, value):
        """Set usemap attibutes value.

        set_usemap(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.USEMAP, value)
        return self

    def get_usemap(self, ):
        """Get usemap attribute value.

        get_usemap()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.USEMAP, None)

    def remove_usemap(self, ):
        """Remove usemap attribute value.

        remove_usemap()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.USEMAP in self.attrs:
            del self.attrs[self.AttributeNames.USEMAP]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# object.py ends here
