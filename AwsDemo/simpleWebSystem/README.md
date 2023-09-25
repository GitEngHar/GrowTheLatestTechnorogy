# 何をしているのか

MYSQLを操作できるバックエンドアプリケーションを公開。  
webサイトから入力したエンドポイントへSQLへGETを実行し、取得結果を表示している

<img src="https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/6bc77b19-3991-4ed5-9caa-20ac53169873" width="50%"></img>

## 再現方法

security Groupは以下の通り作成する
- cloud9-xxxx
  - cloud9利用時、自動で作成される 
- mysql-sg
  - in : 3306
    - source : publicsubnet , cloud9-xxxx
  - out : all  
- public-sg
  - in : 80
    - source : MYIP
  - out : all   

### 1 プライベート・パブリックそれぞれのサブネットを作成する
プライベート: privatesubnet
パブリック: publicsubnet

### 2 RDSをMysqlで作成する。設定値は以下の通り。
port : 3306
name , passwordは任意
所属ネットワーク : privatesubnet
securityGroup : mysql-sg(cloud9は未作成のためインバウンドに設定不可 , 項目5で設定します)

### 3 Mysqlにアクセスできるcloud9を作成する
所属ネットワーク : publicsubnet
sgはデフォルトで作成されるものを利用する

### 4 mysql-sgのインバウンドを設定する
インバウンドで3306 portへcloud9-xxxxの接続を許可します

### 5 cloud9でDataBaseを設定する
本ソースコードではテーブル内のカラムが固定になっているので、それ以外であれば設定は任意で問題ありません。
なお、以下の例に沿った手順を記載します
```
### 設定例
Database名 : SAMPLEDB
TABLE名 : certtb
カラム名とデータ型(固定) : certType varcher(255) , certName varcher(255) 
```
① MYSQLDBのエンドポイントを取得します  
RDS > データベース > (DB名)の接続とセキュリティに「エンドポイント」の記載があります

② cloud9でRDSデータベースに接続  
`mysql -h エンドポイント -P 3306 -u ユーザ名 -p`
接続できない場合はセキュリティグループ か 所属しているネットワークが誤っている可能性があります


③ データベースのテーブル、データを整える
```
#データベースの作成
CREATE SAMPLEDB;

#作成したデータベースに切り替える
USE SAMPLEDB;

#テーブルの作成
CREATE TABLE certtb(certType varchar(255),certName varchar(255))

#テーブルが作成されたのかを確認する
SHOW TABLES;
```
正しく作成されていれば問題なし

### 6 cloud9でImageをビルドするための環境を構築する

① リポジトリをclone  
`git clone https://github.com/GitEngHar/GrowTheLatestTechnorogy.git`

② 作業ディレクトリに移動
`cd ./GrowTheLatestTechnorogy/AwsDemo/simpleWebSystem/backend/`

### 7 cloud9でImageを作成してECRにPushする  
① AWS ECR リポジトリを作成する
以下画像のように、「aws → EXPROLER → リージョン → ECR → 右クリック 」でCreateRepositoryが見えるのでレポジトリを作成
リポジトリ名の入力を求められるので適当に入力してください  
![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/acd01585-afc3-4bf5-a419-f58976c4d26e)

② 作成したECRを開き手順を確認する  
Amazon ECR > リポジトリ > 作成したリポジトリ  
画面右上に「プッシュコマンドの表示」があるので押下  
![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/48a41497-c3e9-461c-b5d4-ffa75dac0739)

③ 手順を上から順にCloud9で実行していく  

④ 問題がなければECRにImageがプッシュされるので②同様にECRを開いてImageが存在するか確認してください
存在すればbackend機能のImageを作成し、ECRに登録する作業は終了です

⑤ frontend Image作成の作業ディレクトリに移動
`cd ./AwsDemo/simpleWebSystem/front`

⑥ 本項番の①～④を実施してください

### 8 フロント・バックエンドのタスクを定義する

### 9 フロント・バックエンド　各サービスを作成する
①クラスタを作成
Amazon Elastic Container Service → クラスター から「クラスターの作成」を選択し、任意の名前でクラスタを作成してください

②作成したクラスタにバックエンドサービスを作成する

### 10 動作確認
