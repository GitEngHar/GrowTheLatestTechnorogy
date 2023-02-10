### ドキュメント概要
- Dockerってこんなに凄いんだ！がわかる内容
  - namespace機能便利。お互いの環境に影響を与えないでサービスを構築できる。
  - 環境構築がすごく楽
  - 違うversionになったらimage変えればいい!
  - 一回yamlファイルで構成組んじゃえば同じシステムをすぐ構築できる！
  - (仮想化特有のメリットもあるけど個人的にはDockerの良さって感じはしてないので相談したいです)
- Dockerってこうやって動きます！
  - Linuxで動くDocker
  - Windowsで動くDocker
    - wsl(windows subsystem for linux)でwindows上にlinuxが動いててその上にdockerだから結局は一緒そう
      - wslはlinuxosではあるけどハードウェアはwindowsなので、docker => linux => windowsのやり取りは必要になる
      - ioのやり取りがlinux単体のdockerとは異なるのでwindows dockerは設定が別途必要なものもあるよ(systemdを使いたいときとか)  
- Dockerに向いていないこと
  - アプリケーションのエンドポイントを提供するためオーケストレーションには向いてなさそう
    - あまり該当の記事がない;;

### 達成条件
- Dockerがどうやって動いているか理解できる
- Dockerに向いていないことを理解できる
- Dockerを使うメリットが理解できる

### 完了目安
- 要相談

### 参考資料
- [公式サイト すごいいい感じにまとまってる](https://docs.docker.jp/get-started/overview.html#:~:text=Docker%20%E3%81%AF%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%92%E9%96%8B%E7%99%BA,%E6%99%82%E9%96%93%E3%81%A7%E6%8F%90%E4%BE%9B%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82)