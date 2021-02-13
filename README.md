# python-mysql
- pythonでmysqlを操作する時の備忘録

## 使い方
```
# mysqlコンテナを立てる
$ cd mysql
$ docker-compose up -d

$ python main.py
```

## 階層
```
├── LICENSE
├── README.md
├── main.py
├── mysql
│   ├── docker-compose.yml # mysqlコンテナの設定
│   ├── log # mysqlのlog
│   │   └── mysql
│   └── mysql
│       ├── Dockerfile
│       ├── conf.d 
│       │   └── my.conf # mysqlのconf
│       └── initdb.d # テストデータ
│           ├── schema.sql
│           └── testdata.sql
└── venv.sh
```
