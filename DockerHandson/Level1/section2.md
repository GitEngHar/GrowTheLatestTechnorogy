# webサーバの構築

## 参考資料

**Linux** の操作で分からないことがあれば ココ を見よう  
**Docker** の操作で分からないことがあれば ココ を見よう  
**DockerPlayGround** の操作で分からないことがあれば ココ を見よう  

## 2-1 実行環境にログイン

[Docker Playground](https://labs.play-with-docker.com/)で実施します

## 2-2 DockerPlayGroundに自分のhtmlファイルをコピーしよう

- 何をやるのか
  - DockerPlayGround環境に `index.html` を作成し、自分の `htmlファイル` の中身をコピーしよう
- 手順  
  1. ターミナルでDockerホスト(DockerPlayGround環境)に `index.html` ファイルを作成してください
  2. `index.html` に全てのユーザーが実行・閲覧・書き込みできる権限を付与してください
  3. DockerPlayGroundのEditorを利用して `index.html` の中身を自分のhtmlファイルに置き換えてください

## 2-3 Dockerplayground環境でwebコンテナを起動する

- 何をやるのか
  - DockerPlayground環境で `webサーバコンテナ` を作成しよう
- 手順
  1. 開発環境(DockerPlayGround)にsshする
  2. dockerコマンドで `8080port` で接続できるwebコンテナを立てる
  3. サーバ(コンテナ)が起動しているか確認

## 2-4 コンテナに自分のhtmlを配置してwebページを公開しよう

- 何をやるのか
  - webサーバのコンテナで自分のwebページを動かして、ブラウザで自己紹介ページを確認しよう
- 手順
  1. Dockerコンテナの `/usr/local/apache2/htdocs/` にindex.htmlをコピーします
  2. webページにアクセスしましょう

自分のページが表示されれば Lv1完了になります。お疲れ様です🎉

webサーバを構築し自分のページをサーバで稼働させ、アクセスすることができました(ブラウザリンクを送ればスマホからも見れます)

## 次につなげるための....少し考えてみよう

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
