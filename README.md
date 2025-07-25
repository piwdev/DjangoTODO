### TODOアプリ

- Front = Django Template(HTML, CSS, Javascript)

- Back = Django

###  プロンプト
#### 要件
- DBには以下のTABLEがある
 table name = tasks (タスク)
 columns = id(pk), title(件名), description(説明), start_date(期限_開始日), until_date(期限_終了日), done_at(完了日)
  補足=tasksテーブルはユーザーがやらないといけないTODOを管理するテーブル。
 -  本アプリにログイン機能はない。Userも作らない。アクセスしている人なら誰でも新しいTODOタスクを追加できる。
 - url = '/' : tasksテーブルにあるデータを表示する。
 - url = '/api/tasks/add' : 新しいタスクをDBに追加する。
 - url = '/add/input' :  ユーザが新しいタスクの情報を入力するinput formを画面に表示する。 このurlの画面で新しいタスクを登録するために必要な情報を入力後、画面にある'ADD' buttonをclickしたら、'/api/tasks/add' を経由して、DBへの登録が成功したら '/'に遷移。
