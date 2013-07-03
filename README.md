
Dive Into Python3 の章立てに沿った問題と問題への回答を検証するためのunittest

## 環境設定の仕方

使いたいpythonをインストール済みであること.

まずvirtualenvをインストールしよう. 配布サイト https://pypi.python.org/pypi/virtualenv を参照.

次にこのgit repositoryをcloneし、その中でvirtualenvを実行します。
具体的にはpython3.3で行う場合は

    % virtualenv --clear --no-site-packages --python=python3.3 py3.3 

などとする。

    % source py3.3/bin.activate

でenvを有効にする。

次にpipを使って依存しているpackageを入れる

    % pip install -r freeze.txt

これでcheck.pyに必要なものがインストールされる。

## check.pyの使い方。

    % python check.py exercises/chap2/q0002.py

とすると、標準出力にいろいろメッセージが出る。

前半は循環複雑度を測定した結果である。
5以上は好ましくない。

後半はpep8のチェックである(pep8.pyを使用)


## testの行い方

    % python -m tests.chap2.q0002

とすると、
exercises/chap2/q0002.py
がunittestされる。
結果が標準出力にでるので、全てokであること

testの実装が間違っていると思われる場合はissueをたててください



