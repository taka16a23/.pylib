#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""body -- body tag

"""
from .html_tag import HtmlTag


class Body(HtmlTag):
    """Body

    Body is a HtmlTag.
    Responsibility:

    HTML の <body> 要素は、 HTML 文書のコンテンツを示す要素です。
    <body> 要素は文書中に一つだけ配置できます。

    コンテンツカテゴリー	区分化ルート
    許可されている内容	フローコンテンツ
    タグの省略	開始タグは、内容の先頭が空白文字、コメント、 <script> 要素、 <style> 要素でない場合は省略可能です。終了タグは、 <body> 要素に内容または開始タグがあり、かつ、直後のノードがコメントでない場合は省略可能です。
    許可されている親要素	<html> 要素の子要素でなければなりません。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLBodyElement
    <body> 要素は HTMLBodyElement インターフェイスを提供します。
    <body> 要素は document.body プロパティからアクセス可能です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """
        onafterprint
        ユーザーによる印刷データ作成直後に呼び出す関数
        onbeforeprint
        ユーザーによるブラウザーへの印刷指示直後に呼び出す関数
        onbeforeunload
        文書のアンロード (ページ遷移、リロード) の直前に呼び出す関数
        onblur
        文書からフォーカスが外されたときに呼び出す関数
        onerror
        文書を正常にロードできなかった際に呼び出す関数
        onfocus
        文書にフォーカスが当たった際に呼び出す関数
        onhashchange
        文書の現在のアドレスのフラグメント識別子 (ハッシュ文字 '#' から始まる部分) が変更された際に呼び出す関数
        onlanguagechange
        言語が変更された際に呼び出す関数
        onload
        文書の読み込み完了時に呼び出す関数
        onmessage
        文書が API からメッセージを受信した際に呼び出す関数
        onoffline
        ネットワークとの交信が不能になった際に呼び出す関数
        ononline
        ネットワークとの交信が発生あるいは回復した際に呼び出す関数
        onpopstate
        ユーザーによるセッション履歴のナビゲート時に呼び出す関数
        onredo
        ユーザーがトランザクション履歴を元に戻した際に呼び出す関数
        onresize
        文書を表示するウィンドウがリサイズされた際に呼び出す関数
        onstorage
        ストレージ領域が変化した際に呼び出す関数
        onundo
        ユーザーがトランザクション履歴をさかのぼることによって後方へ移動した際に呼び出す関数
        onunload
        文書からの離脱時に呼び出す関数
        """
        ONAFTERPRINT = 'onafterprint'
        ONBEFOREPRINT = 'onbeforeprint'
        ONBEFOREUNLOAD = 'onbeforeunload'
        ONBLUR = 'onblur'
        ONERROR = 'onerror'
        ONFOCUS = 'onfocus'
        ONHASHCHANGE = 'onhashchange'
        ONLANGUAGECHANGE = 'onlanguagechange'
        ONLOAD = 'onload'
        ONMESSAGE = 'onmessage'
        ONOFFLINE = 'onoffline'
        ONONLINE = 'ononline'
        ONPOPSTATE = 'onpopstate'
        ONREDO = 'onredo'
        ONRESIZE = 'onresize'
        ONSTORAGE = 'onstorage'
        ONUNDO = 'onundo'
        ONUNLOAD = 'onunload'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='body', tags=[], attrs=None, **kwargs)

    def set_onafterprint(self, value):
        """Set onafterprint.

        set_onafterprint(value)

        @Arguments:
        - `value`: onafterprint attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONAFTERPRINT, value)
        return self

    def get_onafterprint(self, ):
        """Get onafterprint attribute value.

        get_onafterprint()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONAFTERPRINT, None)

    def remove_onafterprint(self, ):
        """Remove onafterprint attribute value.

        remove_onafterprint()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONAFTERPRINT in self.attrs:
            del self.attrs[self.AttributeNames.ONAFTERPRINT]
        return self

    def set_onbeforeunload(self, value):
        """Set onbeforeunload.

        set_onbeforeunload(value)

        @Arguments:
        - `value`: onbeforeunload attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONBEFOREUNLOAD, value)
        return self

    def get_onbeforeunload(self, ):
        """Get onbeforeunload attribute value.

        get_onbeforeunload()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONBEFOREUNLOAD, None)

    def remove_onbeforeunload(self, ):
        """Remove onbeforeunload attribute value.

        remove_onbeforeunload()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONBEFOREUNLOAD in self.attrs:
            del self.attrs[self.AttributeNames.ONBEFOREUNLOAD]
        return self

    def set_onblur(self, value):
        """Set onblur.

        set_onblur(value)

        @Arguments:
        - `value`: onblur attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONBLUR, value)
        return self

    def get_onblur(self, ):
        """Get onblur attribute value.

        get_onblur()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONBLUR, None)

    def remove_onblur(self, ):
        """Remove onblur attribute value.

        remove_onblur()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONBLUR in self.attrs:
            del self.attrs[self.AttributeNames.ONBLUR]
        return self

    def set_focus(self, value):
        """Set focus.

        set_focus(value)

        @Arguments:
        - `value`: focus attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.FOCUS, value)
        return self

    def get_focus(self, ):
        """Get focus attribute value.

        get_focus()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FOCUS, None)

    def remove_focus(self, ):
        """Remove focus attribute value.

        remove_focus()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FOCUS in self.attrs:
            del self.attrs[self.AttributeNames.FOCUS]
        return self

    def set_onhashchange(self, value):
        """Set focus.

        set_onhashchange(value)

        @Arguments:
        - `value`: onhashchange attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONHASHCHANGE, value)
        return self

    def get_onhashchange(self, ):
        """Get onhashchange attribute value.

        get_onhashchange()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONHASHCHANGE, None)

    def remove_onhashchange(self, ):
        """Remove onhashchange attribute value.

        remove_onhashchange()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONHASHCHANGE in self.attrs:
            del self.attrs[self.AttributeNames.ONHASHCHANGE]
        return self

    def set_onlanguagechange(self, value):
        """Set onlanguagechange.

        set_onlanguagechange(value)

        @Arguments:
        - `value`: onlanguagechange attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONLANGUAGECHANGE, value)
        return self

    def get_onlanguagechange(self, ):
        """Get onlanguagechange attribute value.

        get_onlanguagechange()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONLANGUAGECHANGE, None)

    def remove_onlanguagechange(self, ):
        """Remove onlanguagechange attribute value.

        remove_onlanguagechange()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONLANGUAGECHANGE in self.attrs:
            del self.attrs[self.AttributeNames.ONLANGUAGECHANGE]
        return self

    def set_onload(self, value):
        """Set onload.

        set_onload(value)

        @Arguments:
        - `value`: onload attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONLOAD, value)
        return self

    def get_onload(self, ):
        """Get onload attribute value.

        get_onload()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONLOAD, None)

    def remove_onload(self, ):
        """Remove onload attribute value.

        remove_onload()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONLOAD in self.attrs:
            del self.attrs[self.AttributeNames.ONLOAD]
        return self

    def set_onmessage(self, value):
        """Set onmessage.

        set_onmessage(value)

        @Arguments:
        - `value`: onmessage attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONMESSAGE, value)
        return self

    def get_onmessage(self, ):
        """Get onmessage attribute value.

        get_onmessage()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONMESSAGE, None)

    def remove_onmessage(self, ):
        """Remove onmessage attribute value.

        remove_onmessage()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONMESSAGE in self.attrs:
            del self.attrs[self.AttributeNames.ONMESSAGE]
        return self

    def set_onoffline(self, value):
        """Set onoffline.

        set_onoffline(value)

        @Arguments:
        - `value`: onoffline attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONOFFLINE, value)
        return self

    def get_onoffline(self, ):
        """Get onoffline attribute value.

        get_onoffline()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONOFFLINE, None)

    def remove_onoffline(self, ):
        """Remove onoffline attribute value.

        remove_onoffline()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONOFFLINE in self.attrs:
            del self.attrs[self.AttributeNames.ONOFFLINE]
        return self

    def set_ononline(self, value):
        """Set ononline.

        set_ononline(value)

        @Arguments:
        - `value`: ononline attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONONLINE, value)
        return self

    def get_ononline(self, ):
        """Get ononline attribute value.

        get_ononline()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONONLINE, None)

    def remove_ononline(self, ):
        """Remove ononline attribute value.

        remove_ononline()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONONLINE in self.attrs:
            del self.attrs[self.AttributeNames.ONONLINE]
        return self

    def set_onpopstate(self, value):
        """Set onpopstate.

        set_onpopstate(value)

        @Arguments:
        - `value`: onpopstate attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONPOPSTATE, value)
        return self

    def get_onpopstate(self, ):
        """Get onpopstate attribute value.

        get_onpopstate()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONPOPSTATE, None)

    def remove_onpopstate(self, ):
        """Remove onpopstate attribute value.

        remove_onpopstate()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONPOPSTATE in self.attrs:
            del self.attrs[self.AttributeNames.ONPOPSTATE]
        return self

    def set_onredo(self, value):
        """Set onredo.

        set_onredo(value)

        @Arguments:
        - `value`: onredo attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONREDO, value)
        return self

    def get_onredo(self, ):
        """Get onredo attribute value.

        get_onredo()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONREDO, None)

    def remove_onredo(self, ):
        """Remove onredo attribute value.

        remove_onredo()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONREDO in self.attrs:
            del self.attrs[self.AttributeNames.ONREDO]
        return self


    def set_onresize(self, value):
        """Set onresize.

        set_onresize(value)

        @Arguments:
        - `value`: onresize attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONRESIZE, value)
        return self

    def get_onresize(self, ):
        """Get onresize attribute value.

        get_onresize()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONRESIZE, None)

    def remove_onresize(self, ):
        """Remove onresize attribute value.

        remove_onredo()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONRESIZE in self.attrs:
            del self.attrs[self.AttributeNames.ONRESIZE]
        return self

    def set_onstorage(self, value):
        """Set onstorage.

        set_onstorage(value)

        @Arguments:
        - `value`: onresize attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONSTORAGE, value)
        return self

    def get_onstorage(self, ):
        """Get onstorage attribute value.

        get_onstorage()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONSTORAGE, None)

    def remove_onstorage(self, ):
        """Remove onstorage attribute value.

        remove_onstorage()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONSTORAGE in self.attrs:
            del self.attrs[self.AttributeNames.ONSTORAGE]
        return self

    def set_onundo(self, value):
        """Set onundo.

        set_onundo(value)

        @Arguments:
        - `value`: onundo attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONUNDO, value)
        return self

    def get_onundo(self, ):
        """Get onundo attribute value.

        get_onundo()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONUNDO, None)

    def remove_onundo(self, ):
        """Remove onundo attribute value.

        remove_onundo()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONUNDO in self.attrs:
            del self.attrs[self.AttributeNames.ONUNDO]
        return self

    def set_onunload(self, value):
        """Set onunload.

        set_onunload(value)

        @Arguments:
        - `value`: onunload attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ONUNLOAD, value)
        return self

    def get_onunload(self, ):
        """Get onunload attribute value.

        get_onunload()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ONUNLOAD, None)

    def remove_onunload(self, ):
        """Remove onunload attribute value.

        remove_onunload()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ONUNLOAD in self.attrs:
            del self.attrs[self.AttributeNames.ONUNLOAD]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# body.py ends here
