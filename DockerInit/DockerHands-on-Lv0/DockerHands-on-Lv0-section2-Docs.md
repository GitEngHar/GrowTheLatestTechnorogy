### 目的
画像にあるDockerがコンテナを設置するまでの流れを理解する

### 内容
取り掛かる前にDockerセットアップ☞[docker実行環境](https://github.com/GitEngHar/GrowTheLatestTechnorogy/blob/main/docker-start.md)

#### Docker Appに接続まで
![docker ライフサイクル図 (1)](https://user-images.githubusercontent.com/119464648/231908418-25ee8d27-f87d-465a-87c0-99c3ad602877.png)

[Link](https://lucid.app/lucidchart/866ecd6c-b04d-4d22-85b8-05d3eb88be21/edit?invitationId=inv_000ea0a9-a973-4597-82b9-347d42da4e5f&page=0_0#)

#### ライフサイクルの説明
![image](https://user-images.githubusercontent.com/119464648/227698270-fb13cfda-f57c-4687-959d-bb35512e15da.png)


### やってみよう

#### runコマンドを実行する

実行形式
` docker run httpd -p 80:8080 `

| コマンド                | 説明                   |
|---------------------|----------------------|
| docker              | docker機能を利用するコマンド    |
| run                 | imageを指定してコンテナを作成、起動 |
| -p 接続側ポート:ホスト側ポート | コンテナに接続するポート番号を設定    |



```

```

上の実装でコンテナライフサイクルを説明してみる。

> webサーバ(httpd)のimageを取得する
$  docker image pull httpd

docker imageをdockerリポジトリから取得している。
以下のログに注目。

> Using default tag: latest
latest: Pulling from library/httpd
f1f26f570256: Pull complete
a6b093ae1967: Pull complete
6b400bbb27df: Pull complete
d9833ead928a: Pull complete
ace056404ed3: Pull complete

imageにはタグというものがついており、image名:タグでバージョンごとにimageを分けることができている。

` Using default tag: latest ` このログはデフォルトでlatest(最新版)がダウンロードされるように設定されてある。実行したコマンド` docker image pull httpd `を見ると、バージョンを何も指定していないのがわかる。

`latest: Pulling from library/httpd` 最新版のhttpdイメージがdockerレジストリから取得されようとしている。ちなみに、docker レジストリはimageがおかれる場所です。

imageをpull(ダウンロード)した後にrunでコンテナを構築することでコンテナを起動させます。これがDockerのライフサイクルです。

ちなみに、imageが存在しなくても` docker run --name web-nginx nginx `等でコンテナを構築するコマンドを実行しても、imageが自動的にpullされコンテナが構築されます。試してみてください！！
