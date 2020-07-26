#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""input -- input tag

"""
from .html_tag import HtmlTag


class Input(HtmlTag):
    """Input

    Input is a HtmlTag.
    Responsibility:

    HTML の <input> 要素は、ユーザーからデータを受け取るための、
    ウェブベースのフォーム用の対話的なコントロールを作成するために使用します。
    端末とユーザーエージェントによりますが、
    広範に渡る種類のデータ入力やコントロールウィジェットが利用できます。
    <input> 要素は入力型と属性の組み合わせの数が非常に多いため、
    HTML の中で最も強力かつ最も複雑な要素の一つです。

    <input> の型
    <input> の動作は type 属性の値に応じて大きく異なりますので、
    個別のリファレンスページでさまざまな型を扱っています。
    この属性を指定しない場合の既定の型は text です。

    利用可能な型は次の通りです。

    button	プッシュボタンで、既定の動作を持たず、 value 属性の値 (既定では空) を表示します。
    checkbox	チェックボックスで、選択または未選択のうちひとつの値をとることができます。
    color	色を指定するためのコントロールです。対応しているブラウザーでは、アクティブになったときにカラーピッカーが開きます。		HTML5
    date	日付 (時刻を除く年、月、日) を入力するためのコントロールです。対応しているブラウザーでは、アクティブになったときに日付ピッカーまたは年月日の数値のホイールが開きます。		  HTML5
    datetime-local	タイムゾーン情報がない日付と時刻を入力するためのコントロールです。対応しているブラウザーでは、アクティブになったときに日付ピッカーまたは日付および時刻部分の数値のホイールが開きます。		HTML5
    email	電子メールアドレスを編集するための欄です。 text 入力欄のように見えますが、対応しているブラウザーや動的なキーボードのある端末では、入力値を検証したり、関連するキーボードを表示したりします。		HTML5
    file	ユーザーがファイルを選択するコントロールです。 accept 属性を使用して、コントロールが選択することができるファイル形式を定義することができます。
    hidden	表示されないコントロールですが、その値はサーバーに送信されます。隣の列には例がありますが、非表示です。
    image	グラフィックの submit ボタンです。 src 属性で定義された画像を表示します。 alt 属性は src の画像が見つからないときに表示されます。
    month	タイムゾーン情報がない年と月を入力するためのコントロールです。		HTML5
    number	数値を入力するためのコントロールです。対応していればスピナーを表示し、既定の検証を追加します。動的キーボードを持つ一部の端末では、テンキーを表示します。		HTML5
    password	入力値を隠す1行テキストフィールド。サイトが安全ではない場合はユーザーに警告します。
    radio	ラジオボタンで、同じ name の値を持つ複数の選択肢から一つの値を選択することができます。
    range	厳密な値であることが重要ではない数値を入力するためのコントロールです。範囲のウィジェットを表示し、既定では中央の値になります。 min と max の組み合わせで、受け入れる値の範囲を定義することができます。		HTML5
    reset	フォームのコントロールを既定値に初期化するボタンです。推奨しません。
    search	検索文字列を入力するための単一行のテキスト欄です。入力値から改行が自動的に取り除かれます。対応しているブラウザーでは、入力欄を初期化するための削除アイコンが表示されることがあり、欄の内容を消去するために使用することができます。 Displays a search icon instead of enter key on some devices with dynamic keypads.		HTML5
    submit	フォームを送信するボタンです。
    tel	電話番号を入力するためのコントロールです。動的なテンキーを備えた一部の機器では、電話用のテンキーを表示します。		HTML5
    text	既定値です。単一行の入力欄です。改行は自動的に入力値から取り除かれます。
    time	タイムゾーン情報がない時刻を入力するためのコントロールです。		HTML5
    url	URL 入力するための入力欄です。 text 入力欄のように見えますが、対応しているブラウザーや動的なキーボードのある端末では、入力値を検証したり、関連するキーボードを表示したりします。		HTML5
    week	年と週番号で構成される日付を入力するためのコントロールです。週番号はタイムゾーンを伴いません。		HTML5

    属性
    <input> 要素は属性があるためたいへん強力です。上記の例で説明している type 属性が最も重要です。すべての <input> 要素が、 HTMLInputElement インターフェイスに基づいているため、、技術的にはまったく同じ属性を共有しています。しかし実際には、ほとんどの属性は一部の特定の入力型にのみ影響を与えます。さらに、属性によっては入力欄に影響を及ぼす方法が入力型によって異なり、入力型によって異なる方法で影響を与えることがあります。

    この節では、すべての属性に簡単な説明を書いた一覧表を示します。その後で、それぞれの属性がどの入力型に関連付けられているか、より詳細に説明された一覧を示します。ほとんど、またはすべての入力型に共通する属性については、以下でより詳細に定義します。特定の入力型に固有の属性、またはすべての入力型に共通するが、特定の入力型で使用されたときに特別な動作をする属性は、それぞれの型のページで示します。この要素はグローバル属性を含みます。 <input> に関連して特に重要な属性は強調表示されています。

    <input> 要素の属性で、グローバル HTML 属性を含むもの
    属性	型	説明
    accept	file	ファイルアップロードコントロールで期待されるファイル形式のヒント
    alt	image	image 型の alt 属性です。アクセシビリティのために必要です。
    autocomplete	すべて	フォームの自動補完機能のためのヒント
    autofocus	すべて	ページが読み込まれたときに、自動的にそのフォームコントロールにフォーカスを設定する
    capture	file	ファイルアップロードコントロールのメディアキャプチャのインプットメソッド
    checked	radio, checkbox	コマンドやコントロールがチェックされているか
    dirname	text, search	フォーム送信時に要素の方向性を送信するために使用するフォームフィールドの名前です。
    disabled	すべて	コントロールが無効であるかどうか
    form	すべて	コントロールを form 要素に関連付ける
    formaction	image, submit	フォームの送信に使用する URL
    formenctype	image, submit	フォームの送信に使用するデータセットのエンコード種別
    formmethod	image, submit	フォームの送信に使用する HTTP メソッド
    formnovalidate	image, submit	フォームの送信でフォームの検証をバイパス
    formtarget	image, submit	フォーム送信に使用する閲覧コンテキスト
    height	image	<img> の height 属性と同じで、垂直の高さ
    list	ほぼすべて	自動補完オプションの入った <datalist> の id 属性の値
    max	数値型	最大値
    maxlength	password, search, tel, text, url	value の最大長 (文字数)
    min	数値型	最小値
    minlength	password, search, tel, text, url	value の最小長 (文字数)
    multiple	email, file	論理属性。複数の値を許可するかどうか
    name	すべて	入力欄コントロールの名前。名前/値の組の部分としてフォームと一緒に送信される
    pattern	password, text, tel	value が一致すると妥当となるパターン
    placeholder	password, search, tel, text, url	フォームコントロールが空の時にフォームコントロール内に表示される内容
    readonly	ほぼすべて	論理属性。値が編集できない
    required	ほぼすべて	論理属性。フォームが送信できるようにするためには値が必要
    size	email, password, tel, text	コントロールの大きさ
    src	image	<img> の src 属性と同じで、画像リソースのアドレス
    step	numeric types	有効な増分
    type	all	入力フォームコントロールの型
    value	all	このフォームコントロールの現在の値。名前/値の組の部分としてフォームと一緒に送信される
    width	image	<img> の width 属性と同じ
    標準属性の説明に続いて、いくつかの追加の非標準属性を列挙します。

    accept
    file 入力型に対してのみ有効です。 accept 属性は file
    アップロードコントロールの中でどのファイル形式が選択可能であるかを定義します。
    file 入力型を参照してください。

    alt
    image ボタンに対してのみ有効です。
    alt 属性は画像の代替テキストを提供し、 src の画像が存在しないか、
    または読み込みに失敗した場合にこの属性の値を表示します。
    image 入力型を参照してください。

    autocomplete
    (論理属性ではありません!) autocomplete 属性は空白区切りの文字列の値を取り、
    指定された場合は、入力欄が提供する自動補完機能の種類を示します。
    自動補完のよくある実装は、以前同じ入力欄に入力された値を単に
    再呼び出しするものですが、もっと複雑な自動補完もあり得ます。
    例えば、ブラウザーが端末の連絡先リストと連携して、
    email 入力欄でメールアドレスを自動補完したりする可能性もあります。
    許可されている値はautocomplete 属性の値を参照してください。

    autocomplete 属性は hidden, text, search, url, tel, email, date, month,
    week, time, datetime-local, number, range, color, password で有効です。
    この属性は数値またはテキストデータを返さない入力型では効果がなく、
    checkbox, radio, file とすべてのボタン型を除いたすべての入力型で有効になります。

    詳しい情報については HTML の autocomplete 属性を参照してください。
    パスワードセキュリティに関する情報や、 autocomplete が
    hidden に対して他の入力型とどう異なるのかについての情報があります。

    autofocus
    論理属性で、指定された場合は、ページの読み込みが完了したとき
    (またはその要素を含む <dialog> が表示されたとき) に、
    自動的にその入力欄がフォーカスを持つことを示します。

    注: autofocus 属性がついた要素は、 DOMContentLoaded
    イベントが発生する前にフォーカスを得ることがあります。

    文書中で一つの要素だけが autofocus 属性を持つことができます。
    複数の要素に付けた場合は、最初にこの属性を持つ要素がフォーカスを受け取ります。

    autofocus は hidden 型の入力欄にはフォーカスを受け取ることができないため、
    使用することができません。

    警告: フォームコントロールに自動的にフォーカスを与えると、
    読み上げ技術を利用している視覚障碍者を混乱させる可能性があります。
    autofocus が割り当てられると、読み上げソフトは予告なしに
    フォームコントロールにその人を「テレポート」させることになるからです。

    autofocus 属性を適用する際には、アクセシビリティを慎重に検討してください。
    フォームコントロールにフォーカスを自動的に設定すると、
    読み込み時にページのスクロールが発生します。
    フォーカスを与えると、一部のタッチ端末では動的なキーボードを表示させることにもなります。
    読み上げソフトはフォーカスを受けているフォームコントロールの
    ラベルをアナウンスする一方、ラベルよりも前は何もアナウンスしませんし、
    小さな端末を使用している視力のあるユーザーは、
    同様に先行するコンテンツによって作成された文脈を見逃してしまいます。

    capture
    HTML Media Capture 仕様書で導入され、 file 入力型に対してのみ有効です。
    capture 属性は、どのメディア (マイク、ビデオ、カメラ) を
    使用して新しいファイルをキャプチャし、対応するシナリオで file
    アップロードコントロールを使用してアップロードするかを定義します。
    file 入力型を参照してください。

    checked
    radio 型と checkbox 型の両方で有効で、 checked は論理属性です。
    radio 型に存在した場合、そのラジオボタンが同じ名前のラジオボタンの
    グループの中で現在選択されているものであることを示します。
    checkbox 型に存在した場合、 (ページが読み込まれたとき) 既定で
    チェックボックスがチェックされていることを示します。
    このチェックボックスが現在チェックされているかどうかを示すものではありません。
    チェックボックスの状態が変更された場合でも、
    このコンテンツ属性はその変更を反映しません。
    (HTMLInputElement の checked IDL 属性のみが更新されます。)

    注: 他の入力コントロールとは異なり、チェックボックスやラジオボタンの値は、
    現在 checked の状態にある場合に送信データに含まれます。
    存在する場合、チェックされたコントロールの名前と値が送信されます。

    例えば、 name が fruit で、 value が cherry である
    チェックボックスがチェックされていると、送信されるフォームデータには
    fruit=cherry が含まれます。
    チェックボックスがチェックされていない場合、フォームデータには全く含まれません。
    チェックボックスやラジオボタンの既定の value は on です。

    dirname
    text および search 入力型のみに有効で、
    dirname 属性によって要素の書字方向を送信することができます。
    これが含まれていると、フォームコントロールは2組の名前と値を送信します。
    1組目は name と value であり、2組目は名前が dirname の値で、
    値に ltr または rtl がブラウザーによって設定されます。

    <form action="page.html" method="post">
      <label>Fruit: <input type="text" name="fruit" dirname="fruit.dir" value="cherry"></label>
      <input type="submit"/>
    </form>
    <!-- page.html?fruit=cherry&fruit.dir=ltr -->
    上記のフォームが送信されると、入力欄は name / value の組である
    fruit=cherry と、 dirname / 書字方向の組である fruit.dir=ltr が送信されます。

    disabled
    論理属性で、存在する場合、ユーザーが入力欄と対話できないことを示します。
    無効な入力欄は、ふつうより薄い色や、
    その他のフィールドが使用できないことを示すことを示す形で表示されます。

    特に、無効になった入力欄は click イベントを受け取らず、
    フォームと共に送信されることもありません。

    メモ: 仕様書で要件とはされていませんが、 Firefox は既定で、
    ページを再読み込みしても <input> を 動的に無効化した状態を維持します。
    この機能は autocomplete 属性で制御することができます。

    form
    文字列で、入力欄が関連づけられた <form> 要素 (つまり、フォームオーナー) を
    指定します。
    存在する場合、この文字列値は同一文書内の <form> 要素の id と
    一致している必要があります。この属性が指定されない場合は、
    <input> 要素は直近の内包するフォームに (もしあれば) 関連付けられます。

    form 属性によって、入力欄を文書内のどこに置いても、
    文書内の他の場所にあるフォームと関連付けることができます。

    メモ: 入力欄は一つのフォームとしか関連付けることができません。

    formaction
    image および submit 入力型でのみ有効です。
    詳しくは submit 入力型を参照してください。

    formenctype
    image および submit 入力型でのみ有効です。
    詳しくは submit 入力型を参照してください。

    formmethod
    image および submit 入力型でのみ有効です。
    詳しくは submit 入力型を参照してください。

    formnovalidate
    image および submit 入力型でのみ有効です。
    詳しくは submit 入力型を参照してください。

    formtarget
    image および submit 入力型でのみ有効です。
    詳しくは submit 入力型を参照してください。

    height
    image 入力型でのみ有効です。
    height はグラフィックの送信ボタンの表現を表示するための画像ファイルの高さを示します。
    image 入力型を参照してください。

    id
    すべての入力欄を含む、すべての要素で有効なグローバル属性で、
    文書全体で一意でなければならない一意の識別子 (ID) を定義します。
    その目的は、リンクする際に要素を識別することです。
    この値は、ラベルとフォームコントロールをリンクするための
    <label> の for 属性の値として使用されます。 <label> を参照してください。

    inputmode
    すべての要素で有効なグローバル属性です、
    この要素やその内容を編集する際に使用される
    仮想キーボード設定の種類をブラウザーに示すヒントを提供します。
    値としては none, text, tel, url, email, numeric, decimal,
    search があります。

    list
    list 属性で与えられる値は、同じ文書内にある <datalist> 要素の
    id としてください。
    <datalist> は、この入力欄でユーザーに提案する事前定義された値のリストを提供します。
    リストに type と互換性のない値が含まれていた場合は、提案の選択肢には含まれません。
    この値は提案として使用されるものであり、要件ではありません。
    ユーザーはこの定義済みリストから選択することもできるし、
    別な値を提供することもできます。

    これは text, search, url, tel, email, date, month, week, time,
    datetime-local, number, range, color で有効です。

    仕様書によれば、 list 属性は hidden, password, checkbox,
    radio, file それにボタン型では対応していません。

    ブラウザーによっては、カスタムカラーパレットが提案されたり、
    範囲に沿ったチェックマークが表示されたり、<select>のように開くものの、
    リストにない値を入力できるようになったりすることもあります。
    他の入力型についてはブラウザーの互換性一覧表を参照してください。

    <datalist> 要素を参照してください。

    max
    date, month, week, time, datetime-local, number, range
    で有効であり、許可される値の範囲の最大値を定義します。
    要素に入力された value がこれを超えた場合、要素は制約の検証に失敗します。
    max 属性の値が数値でない場合は、要素に最大値は設定されません。

    特殊な場合があります。
    データ型が期間を表す場合 (日付や時刻など)、 max の値は min の値よりも
    小さくなる場合があり、これは範囲が折り返す可能性があることを表します。
    例えば、これによって午後10時から午前4時までの自国の範囲を指定することができます。

    maxlength
    text, search, url, tel, email, password で有効であり、
    ユーザーがフィールドに入力することができる文字数 (UTF-16 コード単位) を定義します。
    これは 0 以上の整数値でなければなりません。
    maxlength が指定されなかった場合、または無効な値が指定された場合は、
    その入力欄には最大長が設定されません。
    この値は minlength の値以上である必要もあります。

    欄に入力されたテキストの文字数が UTF-16 コード単位で maxlength よりも多いと、
    この入力欄は制約の検証に失敗します。
    既定では、ブラウザーはユーザーが maxlength 属性で許可された
    文字数以上を入力するのを防ぎます。詳しくはクライアント側検証を参照してください。

    min
    date, month, week, time, datetime-local, number, range で有効であり、
    許可される値の範囲の最も低い値を定義します。
    要素に入力された value がこれを下回った場合、要素は制約の検証に失敗します。
    min 属性の値が数値でない場合は、要素に最小値は設定されません。

    この値は max 属性の値以下である必要があります。
    min 属性が存在するものの、指定されていなかったり無効であったりした場合は、
    min の値は適用されません。
    min 属性が有効であり、値が空ではなく min 属性で許可された最小値よりも
    小さかった場合、制約の検証によりフォームの送信が行われません。
    詳しくはクライアント側検証を参照してください。

    特殊な場合があります。
    データ型が期間を表す場合 (日付や時刻など)、 max の値は min の値よりも
    小さくなる場合があり、これは範囲が折り返す可能性があることを表します。
    例えば、これによって午後10時から午前4時までの自国の範囲を指定することができます。

    minlength
    text, search, url, tel, email, password で有効であり、
    ユーザーがフィールドに入力することができる最小文字数 (UTF-16 コード単位) を
    定義します。これは負数ではなく、 maxlength で指定された値以下の
    整数値でなければなりません。
    minlength が指定されなかった場合、または無効な値が指定された場合は、
    その入力欄には最小文字数が設定されません。

    欄に入力されたテキストの文字数が UTF-16 コード単位で minlength よりも少ないと、
    この入力欄は制約の検証に失敗します。詳しくはクライアント側検証を参照してください。

    multiple
    論理属性の multiple は、設定されている場合、
    ユーザーがウィジェット内でコンマ区切りで複数のメールアドレスを入力できること、
    または file 入力欄で複数のpファイルを選択することが出えきる
    input. See the email and file input type.

    name
    入力コントロールの名前を指定する文字列です。
    この名前はフォームデータが送信される時に、コントロールの値と共に送信されます。

    name に入れるもの
    name は (厳密にはそうではありませんが) 必須の属性と考えてください。
    入力欄に name が指定されていなかった場合や name が空欄だった場合、
    その入力欄の値はフォームと一緒に送信されません。
    (無効なコントロール、チェックされていないラジオボタン、
    チェックされていないチェックボックス、リセットボタンも送信されません。)

    特殊な場合が2つあります。

    _charset_ : <input> 要素の hidden 型として使用された場合、
    入力欄の value には自動的に、
    フォームを送信するのに使用される文字エンコーディングが
    ユーザーエージェントによって設定されます。
    isindex: 歴史的な理由で、 isindex という名前は許可されていません。
    name とラジオボタン
    name 属性はラジオボタンでは独特の動きをします。

    同名のラジオボタングループ内で、一度にチェックできるラジオボタンは1つのみです。
    そのグループ内のラジオボタンを選択すると、
    同じグループ内の現在選択されているラジオボタンの選択が自動的に解除されます。
    チェックされたラジオボタンの値は、フォームが送信された場合、
    名前と一緒に送信されます。

    同名のラジオボタンが連続したグループにタブ移動した場合、
    そのうちの1つにチェックが入っていると、それがフォーカスを受け取ります。
    ソース順でグループ化されていない場合、グループのうちの1つがチェックされていた場合は、
    タブ移動でグループ内の最初のラジオボタンに出会ったときに、
    チェックが入っていないラジオボタンをすべてスキップして、
    そのグループがフォーカスを受け取ります。
    言い換えれば、1つがチェックされている場合、
    グループ内のチェックされていないラジオボタンはスキップされます。
    どれもチェックされていない場合、同名グループの最初のボタンに到達したときに、
    ラジオボタングループがフォーカスを受け取ります。

    グループ内のラジオボタンにフォーカスがある場合、矢印キーを使用すれば、
    ラジオボタンがソースの順序でグループ化されていなくても、
    同じ名前のすべてのラジオボタンに移動することができます。

    HTMLFormElement.elements
    入力要素に name が与えられると、
    その名前は所有するフォーム要素の HTMLFormElement.elements
    プロパティのプロパティになります。
    name が guest に設定されている入力と、
    name が hat-size に設定されている入力がある場合、
    以下のコードを使用することができます。

    let form = document.querySelector("form");

    let guestName = form.elements.guest;
    let hatSize = form.elements["hat-size"];
    このコードを実行すると、 guestName が HTMLInputElement の
    guest フィールドになり、 hatSize が hat-size フィールドの

    警告: フォームの組み込みプロパティに対応する name を
    フォーム要素に与えないようにします。
    なぜなら、対応する入力への参照で定義済みのプロパティや
    メソッドをオーバーライドしてしまうからです。

    pattern
    pattern 属性は、指定された場合、入力の value が
    一致すれば値が制約の検証を通過したとみなされる正規表現を指定します。
    これは RegExp 型で使用される有効な JavaScript の正規表現でなければならず、
    これは正規表現のガイドで説明されている通りです。
    正規表現をコンパイルする際には 'u' フラグが指定され、
    パターンが ASCII ではなく Unicode コードポイントのシーケンスとして扱われます。
    パターンのテキストの周囲にスラッシュを指定しないでください。

    pattern 属性が存在するが、指定されていないか無効な場合、
    正規表現は適用されず、この属性は完全に無視されます。
    pattern 属性が有効で、空でない値がパターンと一致しない場合、
    制約の検証によりフォームの送信ができなくなります。

    ヒント: pattern 属性を使用する場合は、期待される書式をユーザーに
    知らせる説明文を近くに配置してください。
    また、パターンに一致させるための要件が何であるかを説明するために、
    title 属性を含めることもできます。
    ほとんどのブラウザーはこのタイトルをツールチップとして表示します。
    ツールチップは改善手段です。

    詳しくはクライアント側検証を参照してください。

    placeholder
    placeholder 属性は、フィールドでどのような情報が期待されているかについて、
    ユーザーに簡単なヒントを与える文字列です。
    説明的なメッセージではなく、予想されるデータのタイプを示す単語または
    短いフレーズである必要があります。
    テキストには、改行を含めてはいけません。

    注: placeholder 属性は、フォームを説明するためには他の方法ほど
    意味的に有用ではなく、コンテンツに予期せぬ技術的な問題を引き起こす可能性があります。
    詳細はLabels in <input>: 入力欄 (フォーム入力) 要素を参照してください。

    readonly
    論理属性で、存在すれば、ユーザーが入力欄の値を編集できないことを示します。
    readonly 属性は text, search, url, tel, email, date, month,
    week, time, datetime-local, number, password の各入力型が対応しています。

    詳しくは HTML attribute: readonly を参照してください。

    required
    required は論理属性であり、所有するフォームが送信される前に、
    ユーザーが入力欄の値を指定しなければならないことを示します。
    required 属性は text, search, url, tel, email, date, month,
    week, time, datetime-local, number, password, checkbox, radio,
    file の各入力型で対応しています。

    See Client-side validation and the HTML attribute:
    required for more information.

    size
    Valid for email, password, tel, and text input types only.
    Specifies how much of the input is shown.
    Basically creates same result as setting CSS width property
    with a few specialities. The actual unit of the value depends
    on the input type. For password and text it's number of
    characters (or em units) and pixels for others.
    CSS width takes precedence over size attribute.

    src
    Valid for the image input button only,
    the src is string specifying the URL of the image
    file to display to represent the graphical submit button.
    See the image input type.

    step
    Valid for the numeric input types, including number,
    date/time input types, and range, the step
    attribute is a number that specifies the granularity
    that the value must adhere to.

    If not explicitly included, step defaults to 1 for number and range,
    and 1 unit type (second, week, month, day) for the date/time
    input types.
    The value can must be a positive number—integer or float—or
    the special value any, which means no stepping is implied,
    and any value is allowed (barring other constraints,
    such as min and max).

    If any is not explicity set, valid values for the number,
    date/time input types, and range input types are equal
    to the basis for stepping - the min value and increments of
    the step value, up to the max value, if specified.

    For example, if you have <input type="number" min="10" step="2">,
    then any even integer, 10 or greater, is valid.
    If omitted, <input type="number">, any integer is valid,
    but floats (like 4.2) are not valid,
    because step defaults to 1. For 4.2 to be valid,
    step would have had to be set to any, 0.1, 0.2,
    or any the min value would have had to be a number ending in
    .2, such as <input type="number" min="-5.2">

    Note: When the data entered by the user doesn't adhere to the
    stepping configuration, the value is considered invalid in
    contraint validation and will match the :invalid pseudoclass.

    The default stepping value for number inputs is 1,
    allowing only integers to be entered, unless the stepping base
    is not an integer. The default stepping value for time is
    1 second (with 900 being equal to 15 minutes).

    See Client-side validation for more information.

    tabindex
    Global attribute valid for all elements, including all the input
    types, an integer attribute indicating if the element can
    take input focus (is focusable), if it should participate to
    sequential keyboard navigation.
    As all input types except for input of type hidden are focusable,
    this attribute should not be used on form controls,
    because doing so would require the management of the focus order
    for all elements within the document with the risk of harming
    usability and accessibility if done incorrectly.

    title
    Global attribute valid for all elements, including all input types,
    containing a text representing advisory information related to
    the element it belongs to. Such information can typically,
    but not necessarily, be presented to the user as a tooltip.
    The title should NOT be used as the primary explanation of
    the purpose of the form control.
    Instead, use the <label> element with a for attribute set to the
    form control's id attribute. See Labels below.

    type
    文字列で、表示するコントロールの型を指定します。
    例えば、チェックボックスを生成するには、 checkbox の値が使用されます。
    省略された場合 (または不明な値が指定された場合) は、入力型に text が使用され、
    テキストの入力欄が生成されます。

    許可されている値は<input> の型にあります。

    value
    入力コントロールの値です。
    HTML の中で指定されると、これは初期値となり、
    その後で JavaScript を使用してそれぞれの HTMLInputElement
    オブジェクトの value プロパティにアクセスすることで、
    いつでも変更したり受け取ったりすることができます。
    value 属性は常に省略可ですが、 checkbox, radio, hidden
    においては必須だと考えてください。

    width
    Valid for the image input button only,
    the width is the width of the image file to display to
    represent the graphical submit button. See the image input type.

    標準外の属性
    The following non-standard attributes are also available on
    some browsers.
    As a general rule, you should avoid using them unless it can't be
    helped.

    属性	説明
    autocorrect	A string indicating whether or not autocorrect
                is on or off. Safari only.
    incremental	Whether or not to send repeated search events to
                allow updating live search results while the user is
                still editing the value of the field.
                WebKit and Blink only (Safari, Chrome, Opera, etc.).
    mozactionhint	A string indicating the type of action that
                will be taken when the user presses the Enter or Return
                key while editing the field; this is used to determine
                an appropriate label for that key on a virtual keyboard.
                Firefox for Android only.
    orient	Sets the orientation of the range slider. Firefox only.
    results	The maximum number of items that should be displayed
                in the drop-down list of previous search queries.
                Safari only.
    webkitdirectory	A Boolean indicating whether or not to only
                allow the user to choose a directory
                (or directories, if multiple is also present)
    autocorrect
    Safari 拡張である autocorrect 属性は文字列で、
                ユーザーがこの欄を編集している間に自動修正を
                有効にするかどうかを示します。次の値が許されています。

    on
    構成されていれば、打ち間違いの自動修正や、テキストの置き換え処理を有効にします。
    off
    自動修正やテキストの置き換えを無効にします。
    incremental
    mozactionhint
    A Mozilla extension, supported by Firefox for Android, which provides a hint as to what sort of action will be taken if the user presses the Enter or Return key while editing the field. This information is used to decide what kind of label to use on the Enter key on the virtual keyboard.

    Note: This has been standardized as the global attribute enterkeyhint, but is not yet widely implemented. To see the status of the change being implemented in Firefox, see bug 1490661.

    Permitted values are: go, done, next, search, and send. The browser decides, using this hint, what label to put on the enter key.

    orient
    results
    The results attribute—supported only by Safari—is a numeric value that lets you override the maximum number of entries to be displayed in the <input> element's natively-provided drop-down menu of previous search queries.

    The value must be a non-negative decimal number. If not provided, or an invalid value is given, the browser's default maximum number of entries is used.

    webkitdirectory
    The Boolean webkitdirectory attribute, if present, indicates that only directories should be available to be selected by the user in the file picker interface. See HTMLInputElement.webkitdirectory for additional details and examples.

    Note: Though originally implemented only for WebKit-based browsers, webkitdirectory is also usable in Microsoft Edge as well as Firefox 50 and later. However, even though it has relatively broad support, it is still not standard and should not be used unless you have no alternative.

    メソッド
    以下のメソッドは DOM 内で <input> を表現する HTMLInputElement インターフェイスで提供されます。親インターフェイスである HTMLElement, Element, Node, EventTarget で指定されているメソッドも使用できます。

    checkValidity()
    要素の妥当性チェックを直ちに実行し、値が妥当でない場合は文書に対して invalid イベントを要素に発生させます。
    reportValidity()
    要素の値が妥当性チェックを通った場合は true を返します。そうでなければ、 false を返します。
    select()
    要素が選択可能な場合、 <input> 要素の内容を選択します。選択可能なテキストコンテンツがない要素 (カラーピッカーまたはカレンダー日付入力など) では、このメソッドは何もしません。
    setCustomValidity()
    入力要素の値が妥当ではないときに表示するカスタムメッセージを設定します。
    setRangeText()
    入力要素内の文字の指定された範囲のコンテンツを、指定された文字列に設定します。 selectMode 引数を使用して、既存のコンテンツに影響させる方法を制御することができます。
    setSelectionRange()
    テキストの入力要素内で、指定された文字の範囲を選択します。テキスト入力欄として表現されない入力欄では何もしません。
    stepDown()
    数値入力欄の値を既定で1、または指定された数値の単位だけ減少させます。
    stepUp()
    数値入力欄の値を既定で1、または指定された数値の単位だけ増加させます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        ACCEPT = 'accept'
        ALT = 'alt'
        AUTOCOMPLETE = 'autocomplete'
        AUTOFOCUS = 'autofocus'
        CAPTURE = 'capture'
        CHECKED = 'checked'
        DIRNAME = 'dirname'
        DISABLED = 'disabled'
        FORM = 'form'
        FORMACTION = 'formaction'
        FORMENCTYPE = 'formenctype'
        FORMMETHOD = 'formmethod'
        FORMNOVALIDATE = 'formnovalidate'
        FORMTARGET = 'formtarget'
        HEIGHT = 'height'
        LIST = 'list'
        MAX = 'max'
        MAXLENGTH = 'maxlength'
        MIN = 'min'
        MINLENGTH = 'minlength'
        MULTIPLE = 'multiple'
        NAME = 'name'
        PATTERN = 'pattern'
        PLACEHOLDER = 'placeholder'
        READONLY = 'readonly'
        REQUIRED = 'required'
        SIZE = 'size'
        SRC = 'src'
        STEP = 'step'
        TYPE = 'type'
        VALUE = 'value'
        WIDTH = 'width'

    class FormEnctype(object):
        """FormEnctype

        FormEnctype is a object.
        Responsibility:
        """
        DEFAULT = 'application/x-www-form-urlencoded'
        FILE = 'multipart/form-data'
        TEXT = 'text/plain'

    class FormMethod(object):
        """FormMethod

        FromMethod is a object.
        Responsibility:
        """
        GET = 'get'
        POST = 'post'
        DIALOG = 'dialog'

    class FormTarget(object):
        """FormTarget

        FormTarget is a object.
        Responsibility:
        """
        SELF = 'self'
        BLANK = 'blank'
        PARENT = 'parent'
        TOP = 'top'

    class InputType(object):
        """InputType

        InputType is a object.
        Responsibility:

        <input> の型
        <input> の動作は type 属性の値に応じて大きく異なりますので、個別のリファレンスページでさまざまな型を扱っています。この属性を指定しない場合の既定の型は text です。

        利用可能な型は次の通りです。

        型	説明	基本的な例	仕様書
        button	プッシュボタンで、既定の動作を持たず、 value 属性の値 (既定では空) を表示します。
        checkbox	チェックボックスで、選択または未選択のうちひとつの値をとることができます。
        color	色を指定するためのコントロールです。対応しているブラウザーでは、アクティブになったときにカラーピッカーが開きます。		HTML5
        date	日付 (時刻を除く年、月、日) を入力するためのコントロールです。対応しているブラウザーでは、アクティブになったときに日付ピッカーまたは年月日の数値のホイールが開きます。		  HTML5
        datetime-local	タイムゾーン情報がない日付と時刻を入力するためのコントロールです。対応しているブラウザーでは、アクティブになったときに日付ピッカーまたは日付および時刻部分の数値のホイールが開きます。		HTML5
        email	電子メールアドレスを編集するための欄です。 text 入力欄のように見えますが、対応しているブラウザーや動的なキーボードのある端末では、入力値を検証したり、関連するキーボードを表示したりします。		HTML5
        file	ユーザーがファイルを選択するコントロールです。 accept 属性を使用して、コントロールが選択することができるファイル形式を定義することができます。
        hidden	表示されないコントロールですが、その値はサーバーに送信されます。隣の列には例がありますが、非表示です。
        image	グラフィックの submit ボタンです。 src 属性で定義された画像を表示します。 alt 属性は src の画像が見つからないときに表示されます。
        month	タイムゾーン情報がない年と月を入力するためのコントロールです。		HTML5
        number	数値を入力するためのコントロールです。対応していればスピナーを表示し、既定の検証を追加します。動的キーボードを持つ一部の端末では、テンキーを表示します。		HTML5
        password	入力値を隠す1行テキストフィールド。サイトが安全ではない場合はユーザーに警告します。
        radio	ラジオボタンで、同じ name の値を持つ複数の選択肢から一つの値を選択することができます。
        range	厳密な値であることが重要ではない数値を入力するためのコントロールです。範囲のウィジェットを表示し、既定では中央の値になります。 min と max の組み合わせで、受け入れる値の範囲を定義することができます。		HTML5
        reset	フォームのコントロールを既定値に初期化するボタンです。推奨しません。
        search	検索文字列を入力するための単一行のテキスト欄です。入力値から改行が自動的に取り除かれます。対応しているブラウザーでは、入力欄を初期化するための削除アイコンが表示されることがあり、欄の内容を消去するために使用することができます。 Displays a search icon instead of enter key on some devices with dynamic keypads.		HTML5
        submit	フォームを送信するボタンです。
        tel	電話番号を入力するためのコントロールです。動的なテンキーを備えた一部の機器では、電話用のテンキーを表示します。		HTML5
        text	既定値です。単一行の入力欄です。改行は自動的に入力値から取り除かれます。
        time	タイムゾーン情報がない時刻を入力するためのコントロールです。		HTML5
        url	URL 入力するための入力欄です。 text 入力欄のように見えますが、対応しているブラウザーや動的なキーボードのある端末では、入力値を検証したり、関連するキーボードを表示したりします。		HTML5
        week	年と週番号で構成される日付を入力するためのコントロールです。週番号はタイムゾーンを伴いません。		HTML5
        """
        BUTTON = 'button'
        CHECKBOX = 'checkbox'
        COLOR = 'color'
        DATE = 'date'
        DATETIME_LOCAL = 'datetime-local'
        EMAIL = 'email'
        FILE = 'file'
        HIDDEN = 'hidden'
        IMAGE = 'image'
        MONTH = 'month'
        NUMBER = 'number'
        PASSWORD = 'password'
        RADIO = 'radio'
        RANGE = 'range'
        RESET = 'reset'
        SEARCH = 'search'
        SUBMIT = 'submit'
        TEL = 'tel'
        TEXT = 'text'
        TIME = 'time'
        URL = 'url'
        WEEK = 'week'

    class Loading(object):
        """Loading

        Loading is a object.
        Responsibility:
        """
        EAGER = 'eager'
        lazy = 'lazy'

    class Referrerpolicy(object):
        """Referrerpolicy

        Referrerpolicy is a object.
        Responsibility:
        """
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_WHEN_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_WHEN_CROSS_ORIGIN = 'origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='input', tags=[], attrs=None, **kwargs)

    def set_accept(self, value):
        """Set accept attribute.

        set_accept(value)

        @Arguments:
        - `value`: accept value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ACCEPT, value)

    def remove_accept(self, ):
        """Remove accept attribute.

        remove_accept()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.ACCEPT)
        return self

    def get_accept(self, ):
        """Get accept attribute.

        get_accept()

        @Return: (str) accept value.

        @Error:
        """
        if self.AttributeNames.ACCEPT not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.ACCEPT])

    def set_alt(self, value):
        """Set alt attribute.

        set_alt(value)

        @Arguments:
        - `value`: alt value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ALT, value)

    def remove_alt(self, ):
        """Remove alt attribute.

        remove_alt()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.ALT)
        return self

    def get_alt(self, ):
        """Get alt attribute.

        get_alt()

        @Return: (str) alt value.

        @Error:
        """
        if self.AttributeNames.ALT not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.ALT])

    def get_autocomplete(self, ):
        """Get autocomplete attribute values.

        get_autocomplete()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.AUTOCOMPLETE, None)

    def append_autocomplete(self, value):
        """Append autocomplete values.

        append_autocomplete(value)

        @Arguments:
        - `value`:

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.AUTOCOMPLETE, value)
        return self

    def remove_autocomplete(self, value):
        """Remove autocomplete value.

        remove_autocomplete(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.AUTOCOMPLETE, value)
        return self

    def clear_autocomplete(self, ):
        """Clear autocomplete.

        clear_autocomplete()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.AUTOCOMPLETE)
        return self

    def delete_autocomplete(self, ):
        """Delete autocomplete.

        delete_autocomplete()

        @Return: this instance

        @Error:
        """
        self.remove_attribute(self.AttributeNames.AUTOCOMPLETE)
        return self

    def set_autofocus(self, ):
        """Set autofocus.

        set_autofocus()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOFOCUS, None)

    def remove_autofocus(self, ):
        """Remove autofocus.

        remove_autofocus()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOFOCUS in self.attrs:
            del self.attrs[self.AttributeNames.AUTOFOCUS]
        return self

    def is_autofocus(self, ):
        """Check autofocus enabled.

        is_autofocus()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.AUTOFOCUS in self.attrs

    def set_capture(self, ):
        """Set capture.

        set_capture()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CAPTURE, '')

    def remove_capture(self, ):
        """Remove capture.

        remove_capture()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CAPTURE in self.attrs:
            del self.attrs[self.AttributeNames.CAPTURE]
        return self

    def is_capture(self, ):
        """Check capture enabled.

        is_capture()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.CAPTURE in self.attrs

    def set_checked(self, ):
        """Set checked.

        set_checked()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CHECKED, '')

    def remove_checked(self, ):
        """Remove checked.

        remove_checked()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CHECKED in self.attrs:
            del self.attrs[self.AttributeNames.CHECKED]
        return self

    def is_checked(self, ):
        """Check checked attribute.

        is_checked()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.CHECKED in self.attrs

    def set_dirname(self, value):
        """Set dirname.

        set_dirname(value)

        @Arguments:
        - `value`: dirname

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DIRNAME, value)

    def get_dirname(self, ):
        """Get dirname attribute value.

        get_dirname()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DIRNAME, None)

    def remove_dirname(self, ):
        """Remove dirname attribute.

        remove_dirname()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DIRNAME in self.attrs:
            del self.attrs[self.AttributeNames.DIRNAME]
        return self

    def disable_input(self, ):
        """Disable input as set disable attribute.

        disable_input()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.INPUT in self.attrs:
            del self.attrs[self.AttributeNames.INPUT]
        return self

    def enable_input(self, ):
        """Enable input as remove enable attribute.

        enable_input()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.INPUT, '')

    def is_enable_input(self, ):
        """Check enabled input.

        is_enable_input()

        @Return: True if enable input

        @Error:
        """
        return self.AttributeNames.INPUT not in self.attrs

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

    def set_form_action(self, value):
        """Set form action.

        set_form_action(value)

        @Arguments:
        - `value`: form action value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMACTION, value)

    def get_form_action(self, ):
        """Get form action attribute value.

        get_form_action()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMACTION, None)

    def remove_form_action(self, ):
        """Remove form action attribute.

        remove_form_action()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMACTION in self.attrs:
            del self.attrs[self.AttributeNames.FORMACTION]
        return self

    def set_formenctype(self, value):
        """Set formenctype.

        set_formenctype(value)

        @Arguments:
        - `value`: formenctype value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMENCTYPE, value)

    def get_formenctype(self, ):
        """Get formenctype attribute value.

        get_formenctype()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMENCTYPE, None)

    def remove_formenctype(self, ):
        """Remove formenctype attribute.

        remove_formenctype()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMENCTYPE in self.attrs:
            del self.attrs[self.AttributeNames.FORMENCTYPE]
        return self

    def set_formmethod(self, value):
        """Set formmethod.

        set_formmethod(value)

        @Arguments:
        - `value`: formmethod value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMMETHOD, value)

    def get_formmethod(self, ):
        """Get formmethod attribute value.

        get_formmethod()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMMETHOD, None)

    def remove_formmethod(self, ):
        """Remove formmethod attribute.

        remove_formmethod()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMMETHOD in self.attrs:
            del self.attrs[self.AttributeNames.FORMMETHOD]
        return self

    def remove_formnovalidate(self, ):
        """Remove formnovalidate from attributes.

        remove_formnovalidate()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMNOVALIDATE in self.attrs:
            del self.attrs[self.AttributeNames.FORMNOVALIDATE]
        return self

    def set_formnovalidate(self, ):
        """Set formnovalidate to attribute.

        set_formnovalidate()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMNOVALIDATE, '')

    def is_formnovalidate(self, ):
        """Check has formnovalidate on attributes.

        is_formnovalidate()

        @Return:

        @Error:
        """
        return self.AttributeNames.FORMNOVALIDATE not in self.attrs

    def set_formtarget(self, value):
        """Set formtarget.

        set_formtarget(value)

        @Arguments:
        - `value`: formtarget value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMTARGET, value)

    def get_formtarget(self, ):
        """Get formtarget attribute value.

        get_formtarget()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMTARGET, None)

    def remove_formtarget(self, ):
        """Remove formtarget attribute.

        remove_formtarget()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMTARGET in self.attrs:
            del self.attrs[self.AttributeNames.FORMTARGET]
        return self

    def set_height(self, value):
        """Set height.

        set_height(value)

        @Arguments:
        - `value`: height value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.HEIGHT, value)

    def get_height(self, ):
        """Get height attribute value.

        get_height()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HEIGHT, None)

    def remove_height(self, ):
        """Remove height attribute.

        remove_height()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HEIGHT in self.attrs:
            del self.attrs[self.AttributeNames.HEIGHT]
        return self

    def append_list(self, value):
        """Append list attribute values.

        append_list(value)

        @Arguments:
        - `value`: id

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.LIST, value)
        return self

    def remove_list(self, value):
        """Remove list value.

        remove_list(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.LIST, value)
        return self

    def clear_list(self, ):
        """Clear list.

        clear_list()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.LIST)
        return self

    def delete_list(self, ):
        """Delete list.

        delete_list()

        @Return: this instance

        @Error:
        """
        self.remove_attribute(self.AttributeNames.LIST)
        return self

    def set_max(self, value):
        """Set max.

        set_max(value)

        @Arguments:
        - `value`: max value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MAX, value)

    def get_max(self, ):
        """Get max attribute value.

        get_max()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MAX, None)

    def remove_max(self, ):
        """Remove max attribute.

        remove_max()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MAX in self.attrs:
            del self.attrs[self.AttributeNames.MAX]
        return self

    def set_maxlength(self, value):
        """Set maxlength.

        set_maxlength(value)

        @Arguments:
        - `value`: maxlength value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MAXLENGTH, value)

    def get_maxlength(self, ):
        """Get maxlength attribute value.

        get_maxlength()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MAXLENGTH, None)

    def remove_maxlength(self, ):
        """Remove maxlength attribute.

        remove_maxlength()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MAXLENGTH in self.attrs:
            del self.attrs[self.AttributeNames.MAXLENGTH]
        return self

    def set_min(self, value):
        """Set min.

        set_min(value)

        @Arguments:
        - `value`: min value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MIN, value)

    def get_min(self, ):
        """Get min attribute value.

        get_min()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MIN, None)

    def remove_min(self, ):
        """Remove min attribute.

        remove_min()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MIN in self.attrs:
            del self.attrs[self.AttributeNames.MIN]
        return self

    def set_minlength(self, value):
        """Set minlength.

        set_minlength(value)

        @Arguments:
        - `value`: minlength value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MINLENGTH, value)

    def get_minlength(self, ):
        """Get minlength attribute value.

        get_minlength()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MINLENGTH, None)

    def remove_minlength(self, ):
        """Remove minlength attribute.

        remove_minlength()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MINLENGTH in self.attrs:
            del self.attrs[self.AttributeNames.MINLENGTH]
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

    def set_pattern(self, value):
        """Set pattern.

        set_pattern(value)

        @Arguments:
        - `value`: pattern value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.PATTERN, value)

    def get_pattern(self, ):
        """Get pattern attribute value.

        get_pattern()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.PATTERN, None)

    def remove_pattern(self, ):
        """Remove pattern attribute.

        remove_pattern()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.PATTERN in self.attrs:
            del self.attrs[self.AttributeNames.PATTERN]
        return self

    def set_placeholder(self, value):
        """Set placeholder.

        set_placeholder(value)

        @Arguments:
        - `value`: placeholder value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.PLACEHOLDER, value)

    def get_placeholder(self, ):
        """Get placeholder attribute value.

        get_placeholder()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.PLACEHOLDER, None)

    def remove_placeholder(self, ):
        """Remove placeholder attribute.

        remove_placeholder()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.PLACEHOLDER in self.attrs:
            del self.attrs[self.AttributeNames.PLACEHOLDER]
        return self

    def set_readonly(self, ):
        """Set readonly.

        set_readonly()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.READONLY, None)

    def remove_readonly(self, ):
        """Remove readonly.

        remove_readonly()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.READONLY in self.attrs:
            del self.attrs[self.AttributeNames.READONLY]
        return self

    def is_readonly(self, ):
        """Check readonly enabled.

        is_readonly()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.READONLY in self.attrs

    def set_size(self, value):
        """Set size.

        set_size(value)

        @Arguments:
        - `value`: name value

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

    def set_src(self, value):
        """Set src.

        set_src(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SRC, value)

    def get_src(self, ):
        """Get src attribute value.

        get_src()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SRC, None)

    def remove_src(self, ):
        """Remove src attribute.

        remove_src()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SRC in self.attrs:
            del self.attrs[self.AttributeNames.SRC]
        return self

    def set_step(self, value):
        """Set step.

        set_step(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.STEP, value)

    def get_step(self, ):
        """Get step attribute value.

        get_step()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.STEP, None)

    def remove_step(self, ):
        """Remove step attribute.

        remove_step()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.STEP in self.attrs:
            del self.attrs[self.AttributeNames.STEP]
        return self

    def set_tabindex(self, value):
        """Set tabindex.

        set_tabindex(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TABINDEX, value)

    def get_tabindex(self, ):
        """Get tabindex attribute value.

        get_tabindex()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TABINDEX, None)

    def remove_tabindex(self, ):
        """Remove tabindex attribute.

        remove_tabindex()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TABINDEX in self.attrs:
            del self.attrs[self.AttributeNames.TABINDEX]
        return self

    def set_title(self, value):
        """Set title.

        set_title(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TITLE, value)

    def get_title(self, ):
        """Get title attribute value.

        get_title()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TITLE, None)

    def remove_title(self, ):
        """Remove title attribute.

        remove_title()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TITLE in self.attrs:
            del self.attrs[self.AttributeNames.TITLE]
        return self

    def set_input_type(self, value):
        """Set input type.

        set_input_type(value)

        @Arguments:
        - `value`: type value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TYPE, value)

    def get_input_type(self, ):
        """Get input type attribute value.

        get_input_type()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TYPE, None)

    def remove_input_type(self, ):
        """Remove input type attribute.

        remove_input_type()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TYPE in self.attrs:
            del self.attrs[self.AttributeNames.TYPE]
        return self

    def set_value(self, value):
        """Set value.

        set_value(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.VALUE, value)

    def get_value(self, ):
        """Get value attribute value.

        get_value()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.VALUE, None)

    def remove_value(self, ):
        """Remove value attribute.

        remove_value()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.VALUE in self.attrs:
            del self.attrs[self.AttributeNames.VALUE]
        return self

    def set_width(self, value):
        """Set width.

        set_width(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.WIDTH, value)

    def get_width(self, ):
        """Get width attribute value.

        get_width()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.WIDTH, None)

    def remove_width(self, ):
        """Remove width attribute.

        remove_width()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.WIDTH in self.attrs:
            del self.attrs[self.AttributeNames.WIDTH]
        return self

    def set_ismap(self, ):
        """set ismap attribute value.

        set_ismap()

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ISMAP, None)

    def remove_ismap(self, ):
        """Remove ismap attribute.

        remove_ismap()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.ISMAP in self.attrs:
            del self.attrs[self.AttributeNames.ISMAP]
        return self

    def set_loading(self, value):
        """Set loading.

        set_loading(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.LOADING, value)

    def get_loading(self, ):
        """Get loading attribute value.

        get_loading()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LOADING, None)

    def remove_loading(self, ):
        """Remove loading attribute.

        remove_loading()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LOADING in self.attrs:
            del self.attrs[self.AttributeNames.LOADING]
        return self

    def set_referrerpolicy(self, value):
        """Set referrerpolicy.

        set_referrerpolicy(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.REFERRERPOLICY, value)

    def get_referrerpolicy(self, ):
        """Get referrerpolicy attribute value.

        get_referrerpolicy()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.REFERRERPOLICY, None)

    def remove_referrerpolicy(self, ):
        """Remove referrerpolicy attribute.

        remove_referrerpolicy()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.REFERRERPOLICY in self.attrs:
            del self.attrs[self.AttributeNames.REFERRERPOLICY]
        return self

    def set_src(self, value):
        """Set src.

        set_src(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SRC, value)

    def get_src(self, ):
        """Get src attribute value.

        get_src()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SRC, None)

    def remove_src(self, ):
        """Remove src attribute.

        remove_src()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SRC in self.attrs:
            del self.attrs[self.AttributeNames.SRC]
        return self

    def set_srcset(self, value):
        """Set srcset.

        set_srcset(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SRCSET, value)

    def get_srcset(self, ):
        """Get srcset attribute value.

        get_srcset()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SRCSET, None)

    def remove_srcset(self, ):
        """Remove srcset attribute.

        remove_srcset()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SRCSET in self.attrs:
            del self.attrs[self.AttributeNames.SRCSET]
        return self

    def set_width(self, value):
        """Set width.

        set_width(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.WIDTH, value)

    def get_width(self, ):
        """Get width attribute value.

        get_width()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.WIDTH, None)

    def remove_width(self, ):
        """Remove width attribute.

        remove_width()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.WIDTH in self.attrs:
            del self.attrs[self.AttributeNames.WIDTH]
        return self

    def set_usemap(self, value):
        """Set usemap.

        set_usemap(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.USEMAP, value)

    def get_usemap(self, ):
        """Get usemap attribute value.

        get_usemap()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.USEMAP, None)

    def remove_usemap(self, ):
        """Remove usemap attribute.

        remove_usemap()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.USEMAP in self.attrs:
            del self.attrs[self.AttributeNames.USEMAP]
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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# input.py ends here
