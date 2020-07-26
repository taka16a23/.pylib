#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""select -- select tag

HTML の <select> 要素は、選択式のメニューを提供するコントロールを表します。
"""
from .html_tag import HtmlTag


class Select(HtmlTag):
    """Select

    Select is a HtmlTag.
    Responsibility:

    HTML の <select> 要素は、選択式のメニューを提供するコントロールを表します。

    上のデモは、典型的な <select> の利用方法を示しています。
    アクセシビリティのために、 <label> と結び付けられるように
    id 属性が与えられています。
    それぞれのメニューの選択肢は、 <select> の中の <option> 要素で定義されています。

    <option> 要素は、選択肢が選択されたときにサーバーに送信するデータの値を含む value 属性を持ちます。
    value 属性が含まれない場合、既定で要素の中に含まれるテキストの値が使用されます。
    <option> 要素に selected 属性を付けることで、
    ページが最初に読み込まれたときに既定で選択状態にすることができます。

    <select> 要素は、複数の選択肢を選択することができるかどうかを定める
    multiple、同時にいくつの選択肢を表示することができるかを定める
    size など、制御のために利用することができる固有の属性がいくつかあります。
    required, disabled, autofocus, などのような一般のフォーム入力属性
    の多くも受け付けます。

    さらに、 <option> 要素を <optgroup> 要素の中に入れることで、
    ドロップダウンの中で選択肢をグループに分割することができます。

    その他の例は、ネイティブフォームウィジェット:
    ドロップダウンコンテンツを参照してください。

    属性
    この要素はグローバル属性を持ちます。

    autocomplete
    DOMString で、ユーザーエージェントの自動補完機能のヒントを提供します。
    値の完全なリストや自動補完の使い方の詳細は、 HTML の
    autocomplete 属性を参照してください。

    autofocus
    真偽値属性で、ページが読み込まれた時にこのフォームコントロールが
    入力フォーカスを持つべきであることを指定することができます。
    文書内で autofocus 属性を持つことができるフォーム要素は一つだけです。

    disabled
    真偽値属性で、ユーザーがそのコントロールを利用することができないことを示します。
    もしこの属性が指定されていない場合、コントロールはその設定を親要素、
    例えば <fieldset> 要素から継承します。
    もし親要素に disabled 属性を持つものがなければ、そのコントロールは利用可能です。

    form
    <select> を関連付ける <form> 要素 (フォームオーナー) です。
    この属性の値は、同じ文書内の form 要素の id でなければなりません。
    (この属性が設定されていない場合は、 <select> はその祖先である
    <form> が存在すればそれと関連付けられます。)
    この属性によって、 <select> 要素は、 <form> 要素の子孫に限らず、
    文書内のどこの <form> と結び付けることもできます。
    これは祖先の <form> を上書きすることもできます。

    multiple
    真偽値属性で、リストの複数の選択肢を選択することができることを示します。
    指定されていない場合は、一度に選択することができる選択肢は一つだけです。
    multiple が指定されている場合、多くのブラウザーは単一行の
    ドロップダウンの代わりに、スクロールするリストボックスを表示します。

    name
    この属性は、コントロールの名前を指定するために使用します。

    required
    真偽値属性で、空ではない文字列の値の選択肢を選択しなければならないことを示します。

    size
    コントロールがスクロールするリストボックスとして表示される場合
    (つまり、 multiple が指定されている場合)、
    この属性は一度に見えるべきリストの行数を表します。
    ブラウザーは、 select 要素をスクロールリストボックスとして
    提供する必要はありません。既定値は 0 です。

    メモ: HTML5 の仕様によると、 size 属性の初期値は 1 であるべきとされています。
    しかしながら、実際のところは、このことによっていくつかのウェブサイトを
    壊してしまうことがわかり、他のブラウザーでも現在そうしているものはなく、
    Mozilla は当分の間、 Firefox でも 0 を返し続けることを選択しました。
    使用上の注意
    複数の項目の選択
    デスクトップコンピューターでは、 <select> 要素に multiple
    属性がついている場合に、複数の項目を選択する方法がいくつもあります。

    マウスを使用すると、 Ctrl, Command, Shift キー
    (オペレーティングシステムによって異なります)
    を押しながらクリックすることで、複数の項目を選択または解除することができます。

    警告: キーボードから連続していない複数の項目を選択する仕組みは、
    今のところ Firefox でしか動作しないようです。

    注: macOS では、 Ctrl + ↑ および Ctrl + ↓ のショートカットが、
    OS 既定の Mission Control および Application windows の
    ショートカットと競合するため、動作させるためにはこれらを
    オフにしなければならないでしょう。

    キーボードを使用して、連続した複数の項目を選択するには以下のようにします。

    <select> 要素にフォーカスを移動します。 (例えば Tab を使用するなど)。
    ↑ および ↓ のカーソルキーを使用して、項目を上下に移動し、
    選択したい範囲の先頭または末尾の項目を選択する。
    Shift キーを押したまま ↑ および ↓ のカーソルキーを使用して、
    項目を選択する範囲を増加または減少させる。
    キーボードを使用して、連続していない複数の項目を選択するには以下のようにします。

    <select> 要素にフォーカスを移動します。 (例えば Tab を使用するなど)。
    Ctrl キーを押したまま ↑ および ↓ のカーソルキーを使用して「フォーカスのある」
    選択肢を、選択したいものに移動します。
    「フォーカスのある」選択肢は、キーボードでリンクを
    フォーカスしたときと同様に、点線の輪郭線で強調されます。
    スペースを押して「フォーカスのある」選択肢を選択または解除します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        AUTOCOMPLETE= 'autocomplete'
        AUTOFOCUS = 'autofocus'
        DISABLED = 'disabled'
        FORM = 'form'
        MULTIPLE = 'multiple'
        NAME = 'name'
        REQUIRED = 'required'
        SIZE = 'size'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='select', tags=[], attrs=None, **kwargs)

    def set_autocomplete(self, value):
        """Set autocomplete attribute value.

        set_autocomplete(value)

        @Arguments:
        - `value`: autocomplete attribute value
                   'on' or 'off'

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOCOMPLETE, value)

    def get_autocomplete(self, ):
        """Get autocomplete attribute value.

        get_autocomplete()

        @Return: autocomplete attribute value

        @Error:
        """
        return self.attrs.get(self.AttributeNames.AUTOCOMPLETE, None)

    def enable_autocomplete(self, ):
        """Enable autocomplete attribute value to On.

        enable_autocomplete()

        @Return: this instance

        @Error:
        """
        self.set_autocomplete(self.AutoComplete.ON)
        return self

    def disable_autocomplete(self, ):
        """Disable autocomplete attribute value to OFF.

        disable_autocomplete()

        @Return: this instance

        @Error:
        """
        self.set_autocomplete(self.AutoComplete.OFF)
        return self

    def remove_autocomplete(self, ):
        """Remove autocomplete attribute.

        remove_autocomplete()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOCOMPLETE in self.attrs:
            del self.attrs[self.AttributeNames.AUTOCOMPLETE]
        return self

    def enable_autofocus(self, ):
        """Enable autofocus.

        enable_autofocus()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOFOCUS, '')

    def disable_autofocus(self, ):
        """Disable autofocus.

        disable_autofocus()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOFOCUS in self.attrs:
            del self.attrs[self.AttributeNames.AUTOFOCUS]
        return self

    def set_disabled(self, ):
        """Set disabled attribute.

        disable_attribute()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

    def remove_disabled(self, ):
        """Remove disabled attribute.

        remove_disabled()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLED, '')

    def is_disabled(self, ):
        """Check has disabled attribute.

        is_disabled()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.DISABLED not in self.attrs

    def set_form(self, value):
        """Set form.

        set_form(value)

        @Arguments:
        - `value`: form value as form id

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORM, value)

    def get_form(self, ):
        """Get form attribute value.

        get_form()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORM, None)

    def remove_form(self, ):
        """Remove form attribute.

        remove_form()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORM in self.attrs:
            del self.attrs[self.AttributeNames.FORM]
        return self

    def disable_multiple(self, ):
        """Disable multiple as set disable attribute.

        disable_multiple()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MULTIPLE in self.attrs:
            del self.attrs[self.AttributeNames.MULTIPLE]
        return self

    def enable_multiple(self, ):
        """Enable multiple.

        enable_input()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MULTIPLE, None)

    def is_multiple(self, ):
        """Check enabled multiple.

        is_enable_multiple()

        @Return: True if enable input

        @Error:
        """
        return self.AttributeNames.MULTIPLE not in self.attrs

    def set_name(self, value):
        """Set name.

        set_name(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NAME, value)

    def get_name(self, ):
        """Get name attribute value.

        get_name()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name(self, ):
        """Remove name attribute.

        remove_name()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
        return self

    def set_required(self, ):
        """Set required attribute.

        disable_required()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

    def remove_disabled(self, ):
        """Remove disabled attribute.

        remove_disabled()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLED, '')

    def is_disabled(self, ):
        """Check has disabled attribute.

        is_disabled()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.DISABLED not in self.attrs

    def set_size(self, value):
        """Set size.

        set_size(value)

        @Arguments:
        - `value`: size value as form id

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SIZE, value)

    def get_size(self, ):
        """Get size attribute value.

        get_size()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SIZE, None)

    def remove_size(self, ):
        """Remove size attribute.

        remove_size()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SIZE in self.attrs:
            del self.attrs[self.AttributeNames.SIZE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# select.py ends here
