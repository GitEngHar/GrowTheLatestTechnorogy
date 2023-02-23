## Docker Fileについて
---
### 分かった気になれるDocker File
- 命令を記述ファイルだよ
- DockerFileでDockerImageを作ることができるよ
  - DockerImageを作ることをビルドするっていうよ
- DockerFileの命令はファイルの中身を上から下へ実行していくよ  
- コンテナが作られるまでの流れをまとめてみる
  - DockerFile => DockerImage => Container
   - 逆もできるよ！
     - Container => DockerImage => DockerFile 
     - オリジナルのコンテナを1つのファイルでいつでも呼び出し可能なんて便利すぎる✨

### Docker Fileを使ったwebコンテナの作成
記述する命令一覧

| 命令 | 内容 |
| - | - |
| FROM | 実行の元になるOS |
| RUN | DockerFileのbuildで実行されるコマンド |
| CMD | docker runで実行されるコマンド。推奨=>exec形式・shell形式あり |
| HEALTHCHECK | コンテナ稼働状況の監視 |

- ローカルディレクトリにファイルを作成。
  - 名前： ` DockerFile `
  - 以下ファイルの中身

```
FROM centos:7
RUN yum install -y httpd
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]
```

- dockerimageを作成
  - ` docker build -t my-app:latest . `
- 動作確認
  - ` docker run --name myapp -p 8080:80 my-app `
  - [ブラウザ](http://127.0.0.1:8080)で動作確認

### DockerFileのベストプラクティス
[Docker-docs-ja](https://docs.docker.jp/develop/develop-images/dockerfile_best-practices.html)

## Docker Compose
---
### 分かった気になれるDocker Compose
- 複数のコンテナを定義できるよ！
  - Lv1のMysql+wordpressが1つのファイルで作れちゃうよ
- Composeファイルでアプリケーションが作れちゃうよ！
  - ファイル1つでいつでも再構成できちゃうよ！

### Docker Composeを使ったwebサーバの構築

| セクション | 意味 |
| - | - |
| version | |
| services | |
| services.http-server | |
| services.http-server.image | |
| services.http-server.ports | |
| services.http-server.restart | |

- composeファイルの作成
  - ローカルディレクトリにファイルを作成
    - 名前: `docker-compose.yml`
    - 以下ファイルの中身

```
version: '3'
services:
  http-server:
    image: httpd
    ports:
      - 8080:80
    restart: always
```
- 動作検証
  - ` docker compose up `
  - [ブラウザ](http://127.0.0.1:8080)で動作確認

### Docker Composeを使ったwordpressサーバの構築

| セクション | 意味 |
| - | - |
| networks | |
| services.wordpress.depends_on | |
| services.wordpress.environment | |
| services.wordpress.networks | |

- composeファイルの作成
  - ローカルディレクトリにファイルを作成
    - 名前： ` docker-compose-wordpress.yaml `
    - 以下ファイルの中身

```
version: '3'
services:
  wordpress:
    depends_on:
      - mysql_db
    image: wordpress
    networks:
      - word_network
    ports:
      - 8080:80
    restart: always
    environment:
      WORDPRESS_DB_HOST: mysql_db
      WORDPRESS_DB_NAME: wordpressdb
      WORDPRESS_DB_USER: user01
      WORDPRESS_DB_PASSWORD: user01pass

  mysql_db:
    image: mysql:5.7
    networks:
      - word_network
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: P@ssw0rd 
      MYSQL_DATABASE: wordpressdb 
      MYSQL_USER: user01 
      MYSQL_PASSWORD: user01pass

networks:
  word_network:
```

- 動作検証
  - ` docker compose -f docker-compose-wordpress up `
  - [ブラウザ](http://127.0.0.1:8080)で動作確認

### これで完璧DockerFile


## 参考
[とほほ入門](https://www.tohoho-web.com/docker/dockerfile.html)
