#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""style -- style tag

"""
from .html_tag import HtmlTag


class Style(HtmlTag):
    """Style

    Style is a HtmlTag.
    Responsibility:

    HTML の <style> 要素は、文書あるいは文書の一部分のスタイル情報を含みます。
    <style> 要素を含んでいる文書のコンテンツに適用される CSS を含みます。

    <style> 要素は文書の <head> 要素の中に入れる必要があります。
    一般に、スタイルを外部スタイルシートに入れて <link> 要素を使用すること
    をより推奨します。

    文書に複数の <style> 及び <link> が含まれている場合、
    これらは含まれている文書の DOM 上の順序で適用されます。
    — 予期しないカスケード問題を防ぐために、
    含まれている順序が正しいことを確認してください。

    <link> 要素と同じ方法で、 <style> 要素に media 属性を付けて
    メディアクエリを含めると、ビューポートの幅などのメディア特性に
    依存して内部スタイルシートを選択的に適用することができます。

    属性
    この要素にはグローバル属性があります。

    type
    この属性は、スタイル言語を MIME タイプで定義します
    (文字セットは指定すべきではありません)。
    この属性は省略可能であり、省略した場合の既定値は text/css です。
    空文字列と text/css 以外の値は使用されません。
    メモ: 現代のウェブ文書では、この属性を含める理由はほとんどありません。

    media
    この属性はスタイルを適用するメディアを定義します。
    値はメディアクエリであり、省略した場合の既定値は all です。

    nonce
    script-src コンテンツセキュリティポリシー内の行内スクリプトを
    ホワイトリストに入れるために使われる暗号ノンス (ワンタイム番号) です。
    サーバーはポリシーを送信するたびに一意のノンス値を生成する必要があります。
    それ以外の方法でリソースのポリシーのバイパスとして推測できない
    ノンスを提供することが重要です。

    title
    この属性は代替スタイルシートのセットを指定します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        TYPE = 'type'
        MEDIA = 'media'
        NONCE = 'nonce'
        TITLE = 'title'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='style', tags=[], attrs=None, **kwargs)

    def set_type(self, value):
        """Set type.

        set_type(value)

        @Arguments:
        - `value`: type attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TYPE, value)

    def get_type(self, ):
        """Get type attribute.

        get_type()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TYPE, None)

    def remove_type(self, ):
        """Remove type attribute.

        remove_type()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TYPE in self.attrs:
            del self.attrs[self.AttributeNames.TYPE]
        return self

    def set_media(self, value):
        """Set as media value.

        set_media(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.MEDIA, value)
        return self

    def get_media(self, ):
        """Get media attribute value.

        get_media()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MEDIA, None)

    def remove_media(self, ):
        """Remove media attribute value.

        remove_media()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MEDIA in self.attrs:
            del self.attrs[self.AttributeNames.MEDIA]
        return self

    def set_nonce(self, value):
        """Set nonce.

        set_nonce(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NONCE, value)

    def get_nonce(self, ):
        """Get nonce attribute value.

        get_nonce()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NONCE, None)

    def remove_nonce(self, ):
        """Remove nonce attribute.

        remove_nonce()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NONCE in self.attrs:
            del self.attrs[self.AttributeNames.NONCE]
        return self

    def set_title(self, value):
        """Set title attribute value.

        set_title(value)

        @Arguments:
        - `value`: title value.

        <input type="text" title="this is title">

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TITLE, value)

    def remove_title(self, ):
        """Remove title attribute.

        remove_title()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.TITLE in self.attrs:
            del self.attrs[self.AttributeNames.TITLE]
        return self

    def get_title(self, ):
        """Get title attribute value.

        get_title()

        @Return:

        @Error:
        """
        if self.AttributeNames.TITLE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.TITLE])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# style.py ends here
