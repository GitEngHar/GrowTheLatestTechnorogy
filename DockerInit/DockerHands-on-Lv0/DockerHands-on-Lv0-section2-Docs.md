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

