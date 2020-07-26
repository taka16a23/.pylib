#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""summary -- summary tag

"""
from .html_tag import HtmlTag


class Summary(HtmlTag):
    """Summary

    Summary is a HtmlTag.
    Responsibility:

    HTML の概要明示要素 (<summary>) は、 <details> 要素の内容の要約、
    キャプション、説明、凡例を表します。
    <summary> 要素をクリックすると、親の <details>
    要素の開閉状態を切り替えることができます。

    許可されている内容	記述コンテンツ。または 見出しコンテンツ のうちひとつの要素
    タグの省略	不可。開始タグと終了タグの両方が必要。
    許可されている親要素	<details> 要素
    許可されている ARIA ロール	button
    DOM インターフェイス	HTMLElement

    使用上の注意
    <summary> 要素の中身には、見出しコンテンツ、プレーンテキスト、
    段落内で使用できる HTML が入れられます。

    <summary> 要素は、 <details> 要素の最初の子としてのみ使用できます。
    ユーザーが概要をクリックすると、親の <details> 要素が開閉し、
    <details> 要素に toggle イベントが送信され、
    状態が変化したことを知るために使用することができます。

    既定のラベルテキスト
    <details> 要素の最初の子が <summary> 要素でない場合、
    ユーザーエージェントは既定の文字列 (ふつうは「詳細」) を折りたたみボックスの
    ラベルとして使用します。

    既定のスタイル
    HTML 標準では、<summary> の既定のスタイルに display:list-item が
    含まれています。これで、ラベルの隣に既定で (多くは三角形で) 表示される
    折りたたみウィジェットのとして表示さえるアイコンを変更したり
    削除したりすることができます。

    スタイルを display:block に変更すると、展開用の三角印を削除することができます。

    詳しくはブラウザーの対応の節をご覧ください。すべてのブラウザーがこの要素の機能
    すべてに対応しているわけではありません。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='summary', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# summary.py ends here
