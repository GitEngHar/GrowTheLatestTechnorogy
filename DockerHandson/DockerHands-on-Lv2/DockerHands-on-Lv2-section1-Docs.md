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