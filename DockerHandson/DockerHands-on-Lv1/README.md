# DockerHands-on-Lv1の目的

あなたの成果物 を考えひな形を制作し、ひな形を更新します。

## 何を作るのか

DockerHands-onでは自己紹介ページの制作をします

## 進め方

### ①PC上で自己紹介ページを制作してみよう

あなたがエンジニアとして他の人に紹介するときの自己紹介ページを作成してみましょう
まずは、以下の要素を考えてみましょう (ページ制作は本筋ではないので簡素なもので大丈夫です)

1. 誰に見せるのか
1. どんな情報を盛り込むのか

自己紹介ページは以下を参考にしてみてください

- [【HTML初心者入門】メモ帳でホームページを作成する方法！ - WEBCAMP MEDIA](https://web-camp.io/magazine/archives/7725)

※ 注意点 `<meta charset="UTF-8">` を設定しない場合webページが文字化けするので気を付けてください

- [参考](https://web-camp.io/magazine/archives/96334)

#### 作成例 GLT Q&Aページ

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/9a737438-4cfc-4669-b41c-f195f5f7d248)

<details>

<summary> Q&Aのhtml </summary>

```html
<!doctype html>
  <html  lang="ja">
  <head>
    <meta charset="UTF-8">
    <title>GltDockerHandsOn</title>
  </head>
  <style type="text/css">
    <!--
    #QandA-1 {
      width: 100%;
      font-family: メイリオ;
      font-size: 14px; /*全体のフォントサイズ*/
    }
    #QandA-1 dt {
      background: #444; /* 「Q」タイトルの背景色 */
      color: #fff; /* 「Q」タイトルの文字色 */
      padding: 8px;
      border-radius: 2px;
    }
    #QandA-1 dt:before {
      content: "Q.";
      font-weight: bold;
      margin-right: 8px;
    }
    #QandA-1 dd {
      margin: 24px 16px 40px 32px;
      line-height: 140%;
      text-indent: -24px;
    }
    #QandA-1 dd:before {
      content: "A.";
      font-weight: bold;
      margin-right: 8px;
    }
    -->
  </style>
  <body>
    <h1>GLTの Q&A</h1>
    <div id="QandA-1">
      <dl>
        <dt>GLTは何をするの?</dt>
        <dd>技術を楽しむコンテンツを体験します<br>開発者としてコンテンツの制作や魅力あふれるデモンストレーションを作成いただけると嬉しいです</dd>
        <dt>GLTは何の略称??</dt>
        <dd>Grow the Latest Technology</dd>
        <dt>GLTは誰でも参加できるの??</dt>
        <dd>どなたでも参加可能です<br></dd>
      </dl>    
    </div>
    <footer></footer>    
  </body>
</html>
```
  
</details>

### ②webサーバの構築

#### 2-1 実行環境にログイン

[Docker Playground](https://labs.play-with-docker.com/)で実施します

#### 2-2 Dockerplayground環境でwebコンテナを起動する

- 手順
  1. 開発環境(DockerPlayGround)にsshする ([参考](https://tinyurl.com/5ft9mex7))
  2. dockerコマンドで `8080port` で接続できるwebコンテナを立てる ([参考](https://tinyurl.com/ybyfkhyr))
  3. サーバ(コンテナ)が起動しているか確認　([参考](https://tinyurl.com/4bffcpfv))

#### 2-3 自分のwebページをDockerPlayGroundで作成しよう

- 説明
  - サーバ起動時に設定されている初期webページは httpd の場合、 `htdocs/index.html` になります
  - `htdocs/index.html` を編集・上書きコピーすることで自分の公開したいページを表示することができます(httpd.confに初期表示ページで何を表示するか設定されてありますが、今回は簡単に表示できる方法を選びました)
- 手順  
  1. ターミナルでDockerホスト(DockerPlayGround環境)に `index.html` ファイルを作成してください ([参考](https://tinyurl.com/324rwrcc))
  2. `index.html` に全てのユーザーが実行・閲覧・書き込みできる権限を付与してください ([参考](https://tinyurl.com/bdfae7dm))
  3. DockerPlayGroundのEditorを利用して `index.html` の中身を自分のhtmlファイルに置き換えてください ([参考](https://tinyurl.com/4rwv2b3f))

#### 2-4 コンテナに自分のhtmlを配置してwebページを公開しよう

- 説明
  - webサーバのコンテナ内にある `index.html`ファイル をDockerPlaygroundにある `index.html`ファイル に置き換えることで自分のhtmlページをインターネットに公開します
- 手順
  1. Dockerコンテナの `/usr/local/apache2/htdocs/` にindex.htmlをコピーします ([参考](https://tinyurl.com/mr2a4v27))
  2. webページにアクセスしましょう ([参考](https://tinyurl.com/mue84xae))

自分のページが表示されれば Lv1完了になります。お疲れ様です🎉

webサーバを構築し自分のページをサーバで稼働させ、アクセスすることができました(ブラウザリンクを送ればスマホからも見れます)

### 次につなげるための....少し考えてみよう

このサーバを別の場所で起動したいとき、どうしますか？？ (少し考えてみましょう...)

友人から 「作ったサイト Dockerのコンテナで動かしてみてよー！」 とかいわれるかもしれません...

あなたならどのようにして動かしますか？？

<details>

<summary> 考えたら開いてみてください💡 </summary>

もう一度同じ手順をやろう！と思ったのではないでしょうか。

流石にそれは面倒かと思います。このwebページを webサーバを起動したときに一緒に動いていてほしいですよね。(いちいちhtmlをdockerにコピーしてなどせず)

それが `Imageファイル` というもので可能なんです！

Imageファイルはカスタマイズされたコンテナの状態を保持したファイルなので、この環境をImageファイル化すればどこでも簡単に再現できます

次のstepでは Docker Image を作成してみましょう！

</details>
