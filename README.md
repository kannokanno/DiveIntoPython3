

check.pyの使い方。

 % python check.py exercises/chap2/q0002.py

とすると、標準出力にいろいろメッセージが出る。

前半は循環複雑度を測定した結果である。
5以上は好ましくない。

後半はpep8のチェックである(pep8.pyを使用)


testの行い方

 % python -m tests.chap2.q0002

とすると、
exercises/chap2/q0002.py
がunittestされる。
結果が標準出力にでるので、全てokであること


