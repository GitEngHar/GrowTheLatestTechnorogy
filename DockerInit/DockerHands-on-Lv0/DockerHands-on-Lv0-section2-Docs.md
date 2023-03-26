### Why
画像にあるDockerがコンテナを設置するまでの流れを理解する

### 内容
取り掛かる前にDockerセットアップ☞[docker実行環境](https://github.com/GitEngHar/GrowTheLatestTechnorogy/blob/main/docker-start.md)

コンテナをアプリケーションのエンドポイントだとすると、下の画像ではDockerがアプリケーションを設置するまでの流れを表しているよ。

![image](https://user-images.githubusercontent.com/119464648/227698270-fb13cfda-f57c-4687-959d-bb35512e15da.png)

#### わかった気になれる用語

- コンテナイメージ(Container Image)
  - コンテナを作るときに元になるファイルだよ
  - Imageにはwebサーバやwebアプリケーションがあり、カスタマイズすることもできるよ
- Docker Client
  - Dockerには多くのコマンドがあるよ。
  - 例：Docker run (コンテナを起動)、Docker image pull (イメージ)
    - docker buildもコマンドで、dockerfileといわれるファイルを読み込んでimageを作ってくれるよ 
  - DockerClientはコマンドの入力をHostに伝えるよ
- Docker Host
  - DockerDeamonが動いてるNode（サーバ等々）
    - Daemonはサーバ上でずっと動いているプログラムだよ  
  - Dockerホスト上でコンテナは動いてるよ
- Dockerレジストリ
  - DockerのImageを置いておく場所だよ
  - githubとにていて、プライベート、パブリックで保管ができる
  - Dockerレジストリから欲しいimageをローカルにダウンロードするよ 

### やってみよう

#### DockerClientとDockerHost

```
### docker versionでClientとHost(Server)情報を出力
$ docker version
Client:
 Cloud integration: v1.0.29
 Version:           20.10.22
 API version:       1.41
 Go version:        go1.18.9
 Git commit:        3a2c30b
 Built:             Thu Dec 15 22:36:18 2022
 OS/Arch:           windows/amd64
 Context:           default
 Experimental:      true

Server: Docker Desktop 4.16.2 (95914)
 Engine:
  Version:          20.10.22
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.18.9
  Git commit:       42c8b31
  Built:            Thu Dec 15 22:26:14 2022
  OS/Arch:          linux/amd64
～～省略
```
docker clientがdocker hostのdeamonに対してversionを教えろ！って要求して帰ってきているよ

```
### deamonを起動していないときの出力
$ docker version
error during connect: This error may indicate that the docker daemon is not running.: Get "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/version": open //./pipe/docker_engine: The system cannot find the file specified.
Client:
 Cloud integration: v1.0.29
 Version:           20.10.22
 API version:       1.41
 Go version:        go1.18.9
 Git commit:        3a2c30b
 Built:             Thu Dec 15 22:36:18 2022
 OS/Arch:           windows/amd64
 Context:           default
 Experimental:      true
```

Docker Desktopのプロセスを停止してみてみると、ホストのdeamonが起動してないので、commandを受け付けずエラーが返ってきている。

### イメージを使ってコンテナをbuildする
コンテナはイメージファイルをもとに構築(build)される

コンテナは役割のある仮想化システムの資源(リソース)で、webサーバだったりログの収集コンテナだったり、色々なコンテナを作成できる

基本的には1コンテナは1つの役割で、webサーバ専用コンテナとログ収集専用コンテナのように作られる

```

### 今ダウンロード済みのimageを確認(何も取得済みのimageはなさそう)
$  docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

### webサーバ(httpd)のimageを取得する
$  docker image pull httpd
Using default tag: latest
latest: Pulling from library/httpd
f1f26f570256: Pull complete
a6b093ae1967: Pull complete
6b400bbb27df: Pull complete
d9833ead928a: Pull complete
ace056404ed3: Pull complete
Digest: xxxxx
Status: Downloaded newer image for httpd:latest
docker.io/library/httpd:latest

### ダウンロードしたimageを確認してみる
$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
httpd        latest    192d41583429   3 days ago   145MB

### webサーバのコンテナを作成してみる
$ docker run -d --name web-test httpd
182b4eeb816a3d732177953714aab5833c439c9539faf32a69e91dfae4eaa8ab

### コンテナの起動を確認
$ docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS     NAMES
182b4eeb816a   httpd     "httpd-foreground"   17 seconds ago   Up 14 seconds   80/tcp    web-test

```

上の実装でコンテナライフサイクルを説明してみる。

> ### webサーバ(httpd)のimageを取得する
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

