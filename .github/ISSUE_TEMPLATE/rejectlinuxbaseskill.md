---
name: RejectLinuxBaseSkill
about: Docker開発前によく使うLinuxコマンドを知っておく
title: ''
labels: reject
assignees: ''

---

## 環境構築

1. [DockerPlayground](https://labs.play-with-docker.com/)へログイン

2. 環境にsshする
画面上部にsshコマンドが生成されているのでTerminalやコマンドプロンプトを開きコピー＆ペーストし環境にsshする
例 :  ` ssh ip172-18-123-78-cissaq8gahsduhasdihdvlh0@direct.labs.play-with-docker.com `

<details>

<summary> 実行例 </summary>

```bash
$ ssh ip172-18-123-78-cissaq8gahsduhasdihdvlh0@direct.labs.play-with-docker.com
Connecting to 20.228.211.183:8022
###############################################################
#                          WARNING!!!!                        #
# This is a sandbox environment. Using personal credentials   #
# is HIGHLY! discouraged. Any consequences of doing so are    #
# completely the user's responsibilites.                      #
#                                                             #
# The PWD team.                                               #
###############################################################
[node1] (local) root@192.168.0.28 ~
```

</details>
以降はsshしたターミナルで作業をしてください

3. リポジトリをclone
` git clone https://github.com/GitEngHar/GrowTheLatestTechnorogy.git `

4. 作業ディレクトリへ移動
` cd /root/GrowTheLatestTechnorogy/GLT-Reserve/LinuxBaseSkill `

### 問題

解答例を参考に以下の設問に回答してください

解答例
Q0. ssh先環境のOSを出力してください

```text
[node1] (local) root@192.168.0.28 ~
$ uname -o
Linux
```

Q1. 現在のディレクトリ位置を表示してください

```text

```

Q2. itemsディレクトリの中身を表示してください

```text

```

Q3.  itemsディレクトリ内のredファイルのみを表示してください

```text

```

Q4. /var/glt/itemsのred ファイル以外を表示してください

```text

```

Q5. itemsディレクトリ内のredファイルの中身を表示してください

```text

```

Q6. itemsディレクトリ内のredファイルで先頭文字がoである文字のみを出力してください

```text

```

Q7. 以下を確認し認識できたらチェックボタンにチェックをつけてください

- [ ] daemonプロセスログを確認する場合は `journalctl -u [プロセス名]` で確認できます
- [ ] 特定のエンドポイント("<https://192.168.1.1:8080/support/>" など)にリクエストを送る場合は `curl` コマンドを利用できます
- [ ] 上記以外にもユースケースを実現できる方法があります
