# ディレクトリの目的
ここではGLTでDockerを習得する前の準備です。以下を行います。
Linuxの基礎知識を身に着ける / Dockerが動作できる環境を構築する

## Docker・Githubを利用・開発できる環境を構築する

### 必要なものと環境構築
- InterNetに接続できるPC
- vsCodeInstall
  - こちらから[お使いのOS](https://code.visualstudio.com/download)に合わせてInstallしてください
    - installで迷った場合は[こちら](https://www.javadrive.jp/vscode/install/index1.html)を参考にしてください 
- DockerHubのアカウント
  - お持ちでない方は[こちら](https://hub.docker.com/signup/)で作成してください(作成は無料です)
- GitHubのアカウント
  - お持ちでない方は[こちら](https://reffect.co.jp/html/create_github_account_first_time/)を参考に作成してください(作成は無料です)
  - 開発者として参加する場合はコラボレーターに登録されている必要があります
    - GitEngHarから招待される必要があるため連絡してください

### Dockerの動作環境
公式で提供されている無料の環境があるので[こちら](https://labs.play-with-docker.com/)を利用します

## Githubで何ができるのか・何をするのかを知る

### 概要
GLTではGithubを利用しコンテンツ制作等を行っていきます

以下に機能イメージがつくよう、要望ごとのGithubの機能を紹介します。

#### 制作物の過程を記録したい・バグを改修した記録を残したい
[Issue機能](https://github.com/GitEngHar/GrowTheLatestTechnorogy/issues)を用いて掲示板のように記録を蓄積できます
Issueの例を見ると用途が想像しやすいとおもわれます。([こちら](https://github.com/GitEngHar/GrowTheLatestTechnorogy/issues/1)から確認)

#### 制作物をGithubへアップロードしたい
制作物をコミュニティで掲載する前に内容を確認し、バグがないか & 要件を満たせているかなど確認する必要があります

コミュニティで掲載されるためには main というブランチに反映する必要があります(mainブランチは木の幹だと思ってください)

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/6d8210b6-fc57-4979-8c4c-273350368054)

main に 反映する前に反映してもよいか内容を確認する必要があります。そのため、反映したい変更内容を記録している main ではないブランチが必要です(他ブランチは木の枝のようなものです)

内容を確認し問題なければ変更点をmainに合流(marge)させ、ブランチの変更点が main に反映されます。(木の枝が幹に合体されるのは想像しずらいかも)

変更点を確認するためのレビューがPullRequest(通称PR)です
PRの例は[こちら](https://github.com/GitEngHar/GrowTheLatestTechnorogy/pull/21)にあります

#### GitHubのリポジトリ(ソースコード等)をLocalへ取得したい
リポジトリをCloneすることでローカル環境にソースコード等をコピーできます

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/04488073-768a-4d7a-bda2-d4c094655328)

上画像中の ` https://~省略~ ` をコピーし以下のようにローカルへコピーできます
docker環境でgithubを扱う想定なのでコマンドのInstallは不要です。前述で紹介してある環境ではgitコマンドが初めから利用できます

```
$ git clone https://github.com/GitEngHar/GrowTheLatestTechnorogy.git
```

Localへのクローンで認証は不要ですが、ブランチを main へマージするためのPullRequestを上げたいとなれば、認証が必要です。

認証にはTokenを作成する必要があるため、[こちら](https://capybara-notebook.com/github_accesstoken/)を参考に作成してください。

実際には以下のようにUser名とパスワードを聞かれるので、User名は自分のGithubアカウント名を入力し、パスワードにはToken値を入力すると良いです。
```
Username for 'https://github.com': GitEngHar(ユーザ名)
Password for 'https://ユーザー名@github.com': Token値
```
