### Why

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
  - DockerClientはコマンドの入力をHostに伝えるよ
- Docker Host
  - DockerDeamonが動いてるNode（サーバ等々）
    - Daemonはサーバ上でずっと動いているプログラムだよ  
  - Dockerホスト上でコンテナは動いてるよ
- Dockerレジストリ
  - DockerのImageを置いておく場所だよ
  - githubとにていて、プライベート、パブリックで保管ができる
  - Dockerレジストリから欲しいimageをローカルにダウンロードするよ 
