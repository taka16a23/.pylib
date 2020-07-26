#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""iframe -- iframe tag

"""
from .html_tag import HtmlTag


class Iframe(Htmltag):
    """Iframe

    Iframe is a Htmltag.
    Responsibility:

    HTML のインラインフレーム要素 (<iframe>) は、
    入れ子になった閲覧コンテキストを表現し、
    現在の HTML ページに他のページを埋め込むことができます。

    それぞれの閲覧コンテキストは、セッション履歴と文書を持ちます。
    他の閲覧コンテキストを埋め込んでいる閲覧コンテキストは、
    親閲覧コンテキストと呼ばれます。最上位の閲覧コンテキストは (親を持たないもの) は、
    通常はブラウザーのウィンドウで、 Window オブジェクトで表されます。

    それぞれの閲覧コンテキストは完全な文書環境であるため、
    ページの中で <iframe> を使用するごとに、
    必要となるメモリやその他の計算リソースが増加します。
    理論的には好きなだけ <iframe> を使用することができますが、
    パフォーマンスの問題を確認してください。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 埋め込みコンテンツ, 対話型コンテンツ, 知覚可能コンテンツ
    許可されている内容	なし。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	埋め込みコンテンツを受け入れるすべての要素。
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	application, document, img, none, presentation
    DOM インターフェイス

    allow
    機能ポリシーを <iframe> に指定します。プライバシー、アクセス制限と情報セキュリティの記事に、セキュリティ問題や <iframe> と機能ポリシーがシステムの安全を保つためにどのように機能するかの詳細について書かれています。
    allowfullscreen
    この <iframe> が requestFullscreen() を呼び出して全画面モードにすることができる場合は、 true に設定します。
    この属性は古い属性とみなされており、 allow="fullscreen" に更新されました。
    allowpaymentrequest
    異なるオリジンの <iframe> で Payment Request API の実行を許可する場合は true に設定します。
    この属性は古い属性とみなされており、 allow="payment" に更新されました。
    csp
    埋め込みリソースを制限するコンテンツセキュリティポリシーです。詳しくは HTMLIFrameElement.csp をご覧ください。
    height
    フレームの高さを CSS ピクセル数で示します。既定値は 150 です。
    importance
    <iframe> の src 属性内でのリソースのダウンロード優先度です。許されている値は次の通りです。
    auto (既定値)
    設定なし。ブラウザーはリソースの優先度を決めるために、独自の経験則を使用します。
    high
    このリソースは、より優先度の低いページリソースよりも前にダウンロードします。
    low
    このリソースは、より優先度の高いページリソースの後にダウンロードします。
    loading
    ブラウザーが iframe をどのように読み込むかを示します。
    eager: 可視ビューポートの外にあるかどうかに関わらず、 iframe を直ちにロードします (これが既定値です)。
    lazy: ブラウザーで定義されたビューポートからの計算された距離に達するまで iframe の読み込みを延期します。
    name
    埋め込み閲覧コンテキストのターゲット表の名前です。 <a>, <form>, <base> 要素における target 属性の値、 <input> や <button> 要素における formtarget 属性の値、 window.open() メソッドの windowName 引数の値として使用することができます。
    referrerpolicy
    フレームのリソースにアクセスする際にどのリファラーを送信するかを示します。
    no-referrer: Referer ヘッダーを送信しません。
    no-referrer-when-downgrade (既定値): Referer ヘッダーは TLS (HTTPS) のないオリジンには送信しません。
    origin: 送信するリファラーを、参照しているページのオリジン (スキーム, ホスト名, ポート番号) に限定します。
    origin-when-cross-origin: 他のオリジンへ送信されるリファラーは、スキーム、ホスト名、ポート番号に制限します。同一オリジンへの移動では、パスも含めます。
    same-origin: リファラーは同じオリジンには送信しますが、異なるオリジンへのリクエストにはリファラー情報を送信しません。
    strict-origin: プロトコルのセキュリティ水準が同じ (HTTPS→HTTPS) である場合は、文書のオリジンのみをリファラーとして送信しますが、宛先の安全性が劣る場合 (HTTPS→HTTP) には送信しません。
    strict-origin-when-cross-origin: 同一オリジンへのリクエストには URL 全体を送信し、プロトコルのセキュリティ水準が同じ (HTTPS→HTTPS) である場合は、文書のオリジンのみをリファラーとして送信し、宛先の安全性が劣る場合 (HTTPS→HTTP) にはヘッダーを送信しません。
    unsafe-url: リファラーにオリジンおよびパスを含めます (ただし、フラグメント、パスワード、ユーザー名は含めません)。オリジンやパスの情報が TLS で保護されたリソースから安全性の劣るオリジンへ漏えいしますので、これは安全ではありません。
    sandbox
    フレーム内のコンテンツに追加の制約を適用します。この属性の値は、空にするとすべての制約を適用し、空白区切りのトークンにすると特定の制約を外します。
    allow-downloads-without-user-activation : ユーザーの操作なしでダウンロードが発生することを許可します。
    allow-downloads : ユーザーの操作により発生するダウンロードを許可します。
    allow-forms: リソースがフォームを送信することを許可します。このキーワードが使用されない場合は、フォーム送信がブロックされます。
    allow-modals: リソースがモーダルウィンドウを開くことができるようにします。
    allow-orientation-lock: リソースがスクリーンの方向をロックすることができるようにします。
    allow-pointer-lock: リソースが Pointer Lock API を使用できるようにします。
    allow-popups: (window.open(), target="_blank", showModalDialog() のような) ポップアップを許可します。このキーワードを与えなければ、これらの機能は暗黙に失敗します。
    allow-popups-to-escape-sandbox: サンドボックス化された文書が、サンドボックスを継承するウィンドウではないウィンドウを開けるようにします。例えば、これによって安全に広告をサンドボックス化し、同じ制約を広告のリンク先のページに強制しないようにすることができます。
    allow-presentation: リソースがプレゼンテーションセッションを開始できるようにします。
    allow-same-origin: このトークンが使用されなかった場合、リソースは特殊なオリジンからのものであるとして扱い、常に同一オリジンポリシーに失敗します。
    allow-scripts: リソースがスクリプト (ただし、ポップアップウィンドウを作成しないもの) を実行できるようにします。
    allow-storage-access-by-user-activation : リソースが Storage Access API で親のストレージ容量へのアクセスを要求できるようにします。
    allow-top-navigation: リソースが最上位の閲覧コンテキスト (_top という名前のもの) に移動できるようにします。
    allow-top-navigation-by-user-activation: リソースが最上位の閲覧コンテキストに移動できるようにしますが、ユーザーの操作によって開始されたものに限ります。
    サンドボックスのメモ:
    埋め込まれた文書のオリジンが埋め込み先のページと同じである場合、 allow-scripts と allow-same-origin を同時に使用すると、埋め込まれた文書から sandbox 属性を削除することができるようになるため、絶対に避けるべきです。 — sandbox 属性をまったく使用しないよりも安全ではなくなります。
    攻撃者がサンドボックス化した iframe の外側にコンテンツを表示することができる場合、サンドボックス化は無意味です。例えば、閲覧者がフレームを新しいタブで開く場合などです。潜在的なダメージを抑えるため、そうしたコンテンツは別のオリジンから提供するようにもしてください。
    sandbox 属性は Internet Explorer 9 以前では対応していません。
    src
    埋め込むページの URL です。同一オリジンポリシーに従う空白ページを埋め込む場合は、 about:blank の値を使用してください。また、プログラムから <iframe> の src 属性を削除すると (例えば Element.removeAttribute() などで)、 Firefox (バージョン65以降)、 Chromium ベースのブラウザー、 Safari/iOS では about:blank が読み込まれます。
    srcdoc
    埋め込むインライン HTML で、 src 属性を上書きします。ブラウザーがブラウザーが srcdoc 属性に対応していない場合は、 src 属性の URL で代替されます。
    width
    フレームの幅を CSS ピクセル数で示します。既定値は 300 です。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='iframe', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# iframe.py ends here
