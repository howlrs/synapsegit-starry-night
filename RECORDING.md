# 制作記録の方針（SynapseGit）

## 前提

- 素材は IKEA で購入した、ゴッホ「星月夜」の**完成した絵のレプリカ**。
- その上にアクリル絵の具の**白・青・黒**を載せ、明度5段階で**抽象化**する。
  手順は `painting_steps.md`、見本は `output/03_value5_blue_legend.png`。
- 最初の写真は「絵の具を載せる前の、完成状態の星月夜（レプリカそのまま）」。
- 記録するのは、そこへ**絵の具を重ねていく過程**。

## 保存場所

| 用途 | 場所 |
|---|---|
| 撮影した写真（元ファイルは別に残し、ここへコピー） | `photos/` |
| 登録用のコピー（向きを直し、位置情報入りの EXIF を除いたもの） | `photos/registered/` |
| 生成メモ（登録1件ごと） | `.synapsegit/notes/<slug>.json` |
| 進捗と添削 | `progress.md`、比較画像は `review/` |
| GitHub（public の事例リポジトリ。載せる分だけ） | https://github.com/howlrs/synapsegit-starry-night |
| SynapseGit の repository | `.synapsegit/repo` |
| SynapseGit の Inbox（取り込み待ちの候補） | `.synapsegit/inbox` |

## 1件ごとの3枚の割り当て

| 枠 | 入れるもの |
|---|---|
| Original（元の状態） | 絵の具を載せる前のレプリカの写真（全件共通） |
| Current（今の状態） | その工程を始める前の写真。工程1は Original と同じ写真 |
| AI output（AIの提案） | その工程の地図 `output/steps_blue/stepN_*.png`。計画全体の1件目は `output/03_value5_blue.png` |

- 塗り終えた写真は、次の工程の Current になる。
- 制作者が描いた絵の写真は AI output 欄に入れない。
- 採用・不採用・保留（Human Decision）は制作者がブラウザで選ぶ。エージェントは代わりに選ばない。

| 件 | slug（案） | AI output |
|---|---|---|
| 計画 | `plan-blue-5values` | `output/03_value5_blue.png` |
| 工程1 白 | `step1-white` | `output/steps_blue/step1_white.png` |
| 工程2 明るい青 | `step2-lightblue` | `output/steps_blue/step2_lightblue.png` |
| 工程3 中間の青 | `step3-midblue` | `output/steps_blue/step3_midblue.png` |
| 工程4 青 | `step4-blue` | `output/steps_blue/step4_blue.png` |
| 工程5 黒 | `step5-black` | `output/steps_blue/step5_black.png` |
| 仕上げ | `finish` | `output/03_value5_blue.png` |
| 完成 | `complete` | `output/03_value5_blue.png`（Current＝完成写真。見本と最終比較） |

## 記録の粒度

- **SynapseGit への登録は工程ごとに1件**（上の表の8件）。AIの提案（地図）と人の判断が対応する単位だから。
- 作業後の状態と既存見本を照合する場合は、工程の記録と区別した `review...` の候補を追加する。
  完了した工程や採用済みの判断とは扱わない。
- **写真は作業の区切りごと**に撮り、`photos/` に残す（その日の作業終わり、工程の終わり）。
  登録に使うのは各工程の開始前の写真で、それ以外の途中写真は `photos/` に残すだけ。
- 一定時間ごとの撮影はしない。提案のない記録が増え、乾く前の手を止めることにもなるため。
- 工程3のように広い工程で区切りを記録したい場合は、区画別の地図を作り、区画ごとに1件とする。
- 写真のファイル名は `YYYYMMDD_工程_before|after.jpg`（例: `20261012_step1_before.jpg`）。

## 撮影条件

- 毎回キャンバス全体を正面から、四隅が入るように撮る
- 位置・距離・照明を毎回そろえる。フラッシュは使わず、光は斜め横から
- JPEG か PNG（iPhone は「互換性優先」）。1枚64MBまで

## 決まったこと

- 制作者名: `howlrs`（2026-10-09。公開する howlrs のリポジトリに合わせた。Inbox の5件は別名で登録済み）
- Original（塗る前のレプリカ）: `photos/20261009_step1_before.jpg`
- スマホ（Pixel）の写真には位置情報が入っているので、SynapseGit には `photos/registered/` の
  コピーを登録する。`photos/` の写真は受け取ったファイルと同じ内容のまま残す。

## 写真の一覧

| ファイル | 受け取った名前 | 撮影時刻 | 内容 |
|---|---|---|---|
| `20261009_step1_before.jpg` | 3.jpg | 2026-10-09 17:20 | 塗る前のレプリカ（Original） |
| `20261009_prep_a.jpg` | 2.jpg | 17:21 | 塗る前。青のチューブを置いた写真 |
| `20261009_prep_b.jpg` | 1.jpg | 17:23 | 塗る前。パレットと絵の具を並べた準備 |
| `20261009_step1_after.jpg` | 4.jpg | 17:41 | 工程1（白）の後 ＝ 工程2の開始前 |
| `20261009_step2-3_after.jpg` | 5.jpg | 18:46 | 工程2・3と空の一部の黒の後 ＝ 工程4の開始前 |
| `20261018_blue-black_after.jpg` | 6.jpg | 2026-10-18 18:35 | 青と黒を追加した後（工程4・5に相当する作業を併せて実施） |
| `20261018_white-adjustment_after.jpg` | 7.jpg | 2026-10-18 23:52 | 黒の境界に白を置き、白で各色を和らげた後（最新） |

6・7の元ファイルはJPEG。
撮影時刻は EXIF の撮影日時を参照した。受領したままのコピーを `photos/`、
向きを確認して EXIF 等のメタデータを除いたコピーを `photos/registered/` と `docs/images/` に保存した。

## 記録の履歴

| 日付 | 件 | 使った写真 | slug | 判断 |
|---|---|---|---|---|
| 2026-10-09 | repository と Inbox を作成（候補の登録はまだ） | — | — | — |
| 2026-10-09 | 計画 | O・C: step1_before | `plan-blue-5values` | 採用 |
| 2026-10-09 | 工程1 白 | O・C: step1_before | `step1-white` | 採用 |
| 2026-10-09 | 工程2 明るい青 | C: step1_after | `step2-lightblue` | 採用 |
| 2026-10-09 | 工程3 中間の青 | C: step1_after（※） | `step3-midblue` | 採用 |
| 2026-10-09 | 工程4 青 | C: step2-3_after | `step4-blue` | 採用（塗る前の判断） |

判断は 2026-10-09、制作者が会話で伝えたものを `creator-run` で記録した（session 名 `inbox-<slug>`）。
理由は計画〜工程3に制作者の言葉をそのまま入れた。工程4は理由なしで記録し、SynapseGit が既定の英文を入れた。
公開用の書き出しは `synapsegit/bundle/`、説明文は `synapsegit/presentation.toml`（公開用の判断メモは制作者の確認を経て掲載）。

※ 工程2と3は続けて塗り、その間の写真がない。工程3の Current は工程2の開始前と同じ写真で、
生成メモにもそう書いた。空の一部の黒（工程5の一部）は工程4より先に塗った。

当時の次回予定（2026-10-10）: `progress.md` の直したい点を反映して工程4を塗る → 写真を共有 → `step5-black` を登録（Current＝工程4の後の写真）。

2026-10-18: 6.jpg（青・黒の後）と7.jpg（白による調整の後）を受領し、写真の保存と `progress.md` の追記を行った。
6は青と黒を併せて進めた後の写真なので、「工程4だけの後＝黒を塗る前」の写真としては扱わない。
写真を受領した時点ではSynapseGitを変更せず、以下の候補追加を2026-10-19に行った。
上の採用済みの登録履歴は2026-10-09時点のまま。

### 2026-10-19: 制作状態と完成見本の照合候補を追加

| slug | Current（実物の制作状態） | AI output | 状態 |
|---|---|---|---|
| `review6-blue-black-20261018` | `photos/registered/20261018_blue-black_after.jpg`（6.jpg） | `output/03_value5_blue.png`（既存見本） | Inboxに追加。判断の記録なし |
| `review7-moonlight-white-20261018` | `photos/registered/20261018_white-adjustment_after.jpg`（7.jpg） | `output/03_value5_blue.png`（既存見本） | Inboxに追加。判断の記録なし |

Originalは2件とも `photos/registered/20261009_step1_before.jpg`、制作者名は `howlrs`。
現在の状態から次の調整を考える記録として、実物写真をCurrent、既存のAIの完成見本をAI outputに置いた。
今回、新しい見本画像の生成は行っていない。

生成メモと実行結果は `.synapsegit/notes/<slug>.json`、`<slug>.receipt.json`。
制作意図と添削の詳細は `.synapsegit/notes/review-20261019.md` と `progress.md` に記録した。
両件の `decision_recorded=false` と、保存された3画像のSHA-256の一致を確認済み。
採用・不採用・保留の指定は受けていないため、新しいHuman Decisionは記録していない。
既存の5件の判断と公開用の書き出しは維持した。

GitHub への反映: 工程ごとに写真（`photos/registered/`・`docs/images/`）、`progress.md`、README の表を更新してコミットする。
判断が済んだら `synapse-local` を止め、`creator-report` で確かめてから `synapse-present export --public --github` で書き出し、
中身を確かめて `synapsegit/` に置く。`.synapsegit/` は `.git/info/exclude`、元写真は `.gitignore` で除外している。

`synapse-local` の起動: `D=$PWD/.synapsegit; synapse-local --project "hoshizora=$D/repo" --label "hoshizora=星月夜の上塗り" --import-root "hoshizora=$D/inbox"`
