#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""track -- track tag

"""
from .html_tag import HtmlTag


class Track(HtmlTag):
    """Track

    Track is a HtmlTag.
    Responsibility:

    HTML の <track> 要素はメディア要素 (<audio> および <video>) の子
    として使用します。この要素は自動的に処理される字幕など、
    時間指定されたテキストトラック (または時系列データ) を指定することができます。
    トラックは WebVTT (Web Video Text Tracks) 形式
    (.vtt ファイル) または Timed Text Markup Language (TTML) の形式を用います。

    コンテンツカテゴリ	なし
    許可されている内容	なし。この要素は空要素です。
    タグの省略	空要素であるため開始タグは必須、また終了タグを置いてはなりません。
    許可されている親要素	メディア要素で、任意のフローコンテンツより前。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLTrackElement

    属性
    この要素にはグローバル属性があります。

    default
    この属性は、別の track が適切であるとユーザーの設定が示さない限り有効に
    すべき track であることを表します。
    この属性はメディア要素ごとに 1 つの track 要素のみで使用できます。

    kind
    どのように使用するトラックであるかをを表します。
    省略した場合、デフォルトの種類は subtitles です。
    属性が存在しない場合は subtitles を使用します。
    属性に無効な値が含まれている場合は metadata を使用します
    (バージョン 52 より前の Chrome は、無効な値を subtitles として扱っていました)。
    以下のキーワードを使用できます:

    subtitles
    字幕は、視聴者が理解できないコンテンツの翻訳を提供します。
    例えば、英語の映画における英語以外の言語による会話やテキストです。
    字幕には追加コンテンツ、一般的には付加的な背景情報を含む場合があります。
    例えばスターウォーズの冒頭のテキストや、シーンの日時および場所です。

    captions
    クローズドキャプションは書写、あるいは音声の翻訳を提供します。
    これは音楽のキューやサウンドエフェクトといった重要な非言語情報を含む場合があります。
    これはキューのソース (例: 音楽、テキスト、キャラクター) を示すでしょう。
    耳が不自由なユーザーや音声をミュートしている場合に適しています。

    descriptions
    テキストによる動画コンテンツの説明です。
    目が不自由なユーザーや動画を視聴できない場合に適しています。

    chapters
    チャプタータイトルは、ユーザーがメディアリソースの操作を
    行う際に使用することを意図しています。

    metadata
    スクリプトが使用するトラック情報です。ユーザーには見えません。

    label
    使用可能なテキストトラックを一覧表示する際にブラウザーが使用する、
    ユーザーに見せるテキストトラックのタイトルです。

    src
    トラック (.vtt ファイル) のアドレスです。
    有効な URL であることが必要です。
    この属性は定義する必要があり、
    URL の値は文書として — track 要素の親要素である
    <audio> または <video> が crossorigin 属性を持たない限り
    — 同じオリジンを持たなければなりません。

    srclang
    テキストデータの言語です。有効な BCP 47 言語タグであることが必要です。
    kind 属性に subtitles を設定した場合は、srclang 属性を
    定義しなければなりません。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='track', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# track.py ends here
