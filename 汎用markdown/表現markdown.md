
自分があまり使っていないこと→チェックボックス、表

### 見出し

*italic*
**太字**


リスト
* a
  * b

- a
  - b

1. a
   1. b


チェックbox
- [x] a
- [ ] b

表
<!-- 
Excel to Markdownにより、
shift+alt+vで
エクセル → 表へ
-->
| 左寄せ(デフォルト) |中央揃え| 右寄せ |
| ------------------ | :----------------------------: | -------------------------: |
|その１ | コロンでラインを挟むと中央揃え | 右側にコロンを書くと右寄せ |

エクセルから作成
| 22/1111                            | 22/1112                        |
|------------------------------------|--------------------------------|
| 増量品を新商品とするかの扱い                     | 目標                             |
|                                    | 変換前変換後テーブル関連をcodecommitに上げる    |
| 17時：販促会議                           | githubで自分リモートリポジトリを作成する        |
| ┗ PSI側の処理をあまり把握していないので、自分では判断できない。 | 自分の汎用.pyと関数をそこに入れておく、汎用mkdownも |


引用
>あいうえお
>>かきくけこ

pythonコード乗せる(ブロック)
```python
import pandas as pd
```

pythonコード乗せる(インライン)
プリント`print('A')`したい

水平線
***
---


リンク
[title](https)

画像
![画像](./image/test.PNG)


# Markdown All in Oneについて
[Official link](https://code.visualstudio.com/docs/languages/markdown)

ショートカット
目次の作成
`ctrl+shift+p`：`Markdown All in One: Create Table of Contents`

目次から除外
`<!-- omit in toc -->`

セクションの追加
`ctrl+shift+p `：`Markdown All in One: Add Update section numbers`


# Markdown Navigationについて

保存をすると、ファイルタブの下に`MARKDOWN NABIGATION`が表示される
