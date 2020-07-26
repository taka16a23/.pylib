#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""fieldset -- fieldset tag

"""
from .html_tag import HtmlTag


class FieldSet(HtmlTag):
    """FieldSet

    FieldSet is a HtmlTag.
    Responsibility:

    HTML の <fieldset> 要素は、ウェブフォーム内のラベル (<label>)
    などのようにいくつかのコントロールをグループ化するために使用します。

    <form>
      <fieldset>
        <legend>Choose your favorite monster</legend>

        <input type="radio" id="kraken" name="monster">
        <label for="kraken">Kraken</label><br/>

        <input type="radio" id="sasquatch" name="monster">
        <label for="sasquatch">Sasquatch</label><br/>

        <input type="radio" id="mothman" name="monster">
        <label for="mothman">Mothman</label>
      </fieldset>
    </form>

    上記の例にあるように、 <fieldset> 要素は HTML フォームの一部をグループ化し、
    内側の <legend> 要素で <fieldset> のキャプションを提供しています。
    いくつかの属性を取りますが、特に重要なものとして form は、
    同じページの <form> の id を含むことができ、
    <fieldset> が <form> の中になくてもその一部として扱うことができたり、
    disabled は、 <fieldset> およびその中身を一度に無効にすることができたりします。

    disabled
    この論理型属性が設定されている場合、
    <fieldset> の子孫要素として配置したフォームコントロールはすべて無効になり、
    つまり編集したり <form> と一緒に送信したりすることができなくなります。
    マウスクリックやフォーカス関連のイベントのような閲覧イベントを受け取らなくなります。
    既定では、ブラウザーはそのようなコントロールを灰色で表示します。
    なお、子孫の <legend> 要素の中のフォーム要素は無効になりません。

    form
    <form> 要素の id 属性を指定し、 <fieldset> 要素はたとえその中になくても、
    その一部とすることができます。

    name
    グループに関連付けられた名前です。

    メモ: fieldset 要素自身のラベルの役割は、その最初の子要素として配置した
    <legend> 要素が担います。

    CSS でのスタイル付け
    <fieldset> には、スタイル付けの特殊な考慮事項がいくつかあります。

    display の値は既定で block であり、ブロック整形コンテキストを確立します。
    <fieldset> がインラインレベルの display の値でスタイル付けされた場合は
    inline-block として動作し、そうでなければ block として動作します。
    既定では、コンテンツを囲む 2px groove の境界線があり、
    少量の既定のパディングがあります。要素は既定で
    min-inline-size: min-content を持ちます。

    <legend> が存在する場合は、 block-start 境界線の上に配置されます。
    <legend> は縮小折り返しであり、整形コンテキストを確立します。
    display の値はブロック的です。 (例えば、 display: inline は
    block として動作します。)

    <fieldset> の内容を保持する無名のボックスが生成され、
    <fieldset> から特定のプロパティを継承します。
    <fieldset> が display: grid または
    display: inline-grid でスタイル付けされていた場合、
    無名ボックスはグリッド整形コンテキストになり、
    <fieldset> が display: flex または
    display: inline-flex でスタイル付けされていた場合、
    無名ボックスはフレックス整形コンテキストになります。
    それ以外の場合はブロック整形コンテキストになります。

    <fieldset> および <legend> に対しては、
    ページデザインに合うあらゆる方法で気軽にスタイル付けしてください。

    メモ: この記事の執筆時点で、 Microsoft Edge と Google Chrome には
    フレックスボックスやグリッドレイアウトが <fieldset>
    の中に置けないというバグがあります。この GitHub の課題がバグ追跡のリンクです。

    技術的概要
    コンテンツカテゴリー	フローコンテンツ, 区分化ルート, リスト化, フォーム関連要素, 知覚可能コンテンツ
    許可されている内容	任意の <legend> 要素と、それに続くフローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    暗黙の ARIA ロール	group
    許可されている ARIA ロール	radiogroup, presentation, none
    DOM インターフェイス
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        disabled
        この論理型属性が設定されている場合、
        <fieldset> の子孫要素として配置したフォームコントロールはすべて無効になり、
        つまり編集したり <form> と一緒に送信したりすることができなくなります。
        マウスクリックやフォーカス関連のイベントのような閲覧イベントを受け取らなくなります。
        既定では、ブラウザーはそのようなコントロールを灰色で表示します。
        なお、子孫の <legend> 要素の中のフォーム要素は無効になりません。

        form
        <form> 要素の id 属性を指定し、 <fieldset> 要素はたとえその中になくても、
        その一部とすることができます。

        name
        グループに関連付けられた名前です。
        """
        DISABLED = 'disabled'
        FORM = 'form'
        NAME = 'name'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='fieldset', tags=[], attrs=None, **kwargs)

    def disable(self, ):
        """Set disable attribute.

        disable(value)

        @Arguments:
        - `value`: disable attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DISABLED, None)
        return self

    def enable(self, ):
        """Remove disable attribute.

        enable()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

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

    def set_name_attribute(self, value):
        """Set name.

        set_name_attribute(value)

        @Arguments:
        - `value`: name attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NAME, value)

    def get_name_attribute(self, ):
        """Get name attribute.

        get_name_attribute()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name_attribute(self, ):
        """Remove name attribute.

        remove_name_attribute()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# fieldset.py ends here
