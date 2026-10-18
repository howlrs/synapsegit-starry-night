# SynapseGit の使い方（この事例で実際に使った手順）

初回（2026-10-09）はSynapseGit v1.0.0、2026-10-19の候補追加は導入済みのv1.2.0を使用。
以下の1〜6は初回に使った手順で、今回の実行内容は7に追記した。
AIエージェント（初回はClaude Code、今回の候補追加はCodex）が候補を置き、判断は制作者がブラウザや会話で伝える。
エージェントは判断を代わりに選ばない。

## 1. 置き場所を用意する（最初の1回）

```bash
synapse init .synapsegit/repo     # 記録本体
mkdir -p .synapsegit/inbox        # 取り込み待ちの候補（repository の外に置く）
```

## 2. 写真を整える

スマホの写真には向きの情報と位置情報が入っている。向きを画像に反映し、EXIF を除いたコピーを
`photos/registered/` に作って登録に使う（受け取ったままの写真は手元の `photos/` に残し、GitHub には載せない）。

## 3. 工程ごとに候補を置く

生成メモ（`tool`・`intent` など、利用者が申告する情報）を JSON で用意し、3枚の画像と一緒に Inbox へ置く。
この時点では判断は記録されない（`"decision_recorded": false`）。

```bash
O=photos/registered/20261009_step1_before.jpg
synapse inbox put .synapsegit/inbox step2-lightblue \
  "$O" photos/registered/20261009_step1_after.jpg output/steps_blue/step2_lightblue.png \
  --subject "星月夜の上塗り（白・青・黒の明度5段階）" --creator "howlrs" \
  --generation-note-file .synapsegit/notes/step2-lightblue.json --format json
```

2026-10-09 に置いた5件（画像は SHA-256 の先頭16桁）。Inbox に置いた時の制作者名は別名で、判断の記録から howlrs にそろえた:

| slug | Original | Current | AI output |
|---|---|---|---|
| `plan-blue-5values` | `6627e06e4b9a57ac` | `6627e06e4b9a57ac` | `89ed5f818d7156f9`（`03_value5_blue.png`） |
| `step1-white` | `6627e06e4b9a57ac` | `6627e06e4b9a57ac` | `15d6817cbe7dd7e3`（`step1_white.png`） |
| `step2-lightblue` | `6627e06e4b9a57ac` | `059f89438a5ae261` | `086296b2706eafa2`（`step2_lightblue.png`） |
| `step3-midblue` | `6627e06e4b9a57ac` | `059f89438a5ae261` | `e144bc9d6692fe2a`（`step3_midblue.png`） |
| `step4-blue` | `6627e06e4b9a57ac` | `f8ecbb5935343fec` | `5290abe05ec019b1`（`step4_blue.png`） |

写真: `6627e0…` ＝ `20261009_step1_before.jpg`、`059f89…` ＝ `20261009_step1_after.jpg`、
`f8ecbb…` ＝ `20261009_step2-3_after.jpg`（いずれも `photos/registered/`）。`sha256sum` で同じ値になることを確かめられる。

## 4. 制作者が判断する

```bash
D=$PWD/.synapsegit
synapse-local --project "hoshizora=$D/repo" --label "hoshizora=星月夜の上塗り" --import-root "hoshizora=$D/inbox"
```

表示された `http://127.0.0.1:…` を開き、取り込み待ちの候補を取り込んで、3枚を見比べて採用・不採用・保留を選ぶ。
サーバーは自分の PC（127.0.0.1）だけで動き、外へは公開されない。

2026-10-09 は、制作者が3枚を見比べたうえで会話の中で5件とも「採用」と伝えたので、エージェントがその判断を
`creator-run` で記録した（判断そのものは制作者が決めたもの）。session 名は、ブラウザの取り込みが提案する名前と同じ
`inbox-<slug>` にし、Inbox の候補が取り込み済みとして扱われるようにした。

```bash
synapse creator-run .synapsegit/repo inbox-step2-lightblue \
  "$O" photos/registered/20261009_step1_after.jpg output/steps_blue/step2_lightblue.png \
  --subject "星月夜の上塗り（白・青・黒の明度5段階）" --creator "howlrs" --decision adopt \
  --rationale "<制作者が伝えた理由>" --generation-note-file .synapsegit/notes/step2-lightblue.json
```

理由と生成メモは非公開の記録にだけ残り、公開用の書き出しには入らない。

## 5. 判断を確かめる

```bash
synapse creator-list .synapsegit/repo --format json                  # 未検証の一覧。session 名を探す
synapse creator-report .synapsegit/repo inbox-step2-lightblue        # 1件の検証済みの記録
```

`--format json` の出力は理由や内部 ID を含む非公開の記録なので、GitHub には載せない。

## 6. GitHub 用に書き出す

`synapse-local` を止めてから、公開用の書き出しを作る。ネットワークには何も送らず、手元にファイルを作るだけ。

```bash
synapse-present export .synapsegit/repo synapsegit/bundle \
  --presentation synapsegit/presentation.toml --public --github
synapse-present preview synapsegit/bundle
```

書き出しには `projection.json`・`story.md`・`index.html`・`target/README.md` などが入る。
画像そのもの、判断の理由、生成メモ、内部 ID は入らない。件名と制作者名も入らないので、作品名・制作者の表示名・
各画像の注記は `synapsegit/presentation.toml`（公開用の説明文）で付けた。中身を確かめてからコミットする。

## 7. 制作写真6・7と既存見本の照合を追加（2026-10-19）

制作写真をCurrent、既存の完成見本をAI outputとして、工程とは別の照合候補を2件追加した。
Originalは塗る前のレプリカ、制作者名は `howlrs`。画像の再生成は行っていない。

```bash
synapse inbox put .synapsegit/inbox review6-blue-black-20261018 \
  photos/registered/20261009_step1_before.jpg \
  photos/registered/20261018_blue-black_after.jpg output/03_value5_blue.png \
  --subject "星月夜の上塗り: 青・黒の追加後（6.jpg）と完成見本の照合" --creator "howlrs" \
  --generation-note-file .synapsegit/notes/review6-blue-black-20261018.json --format json

synapse inbox put .synapsegit/inbox review7-moonlight-white-20261018 \
  photos/registered/20261009_step1_before.jpg \
  photos/registered/20261018_white-adjustment_after.jpg output/03_value5_blue.png \
  --subject "星月夜の上塗り: 月光の白と躍動する糸杉（7.jpg）の照合" --creator "howlrs" \
  --generation-note-file .synapsegit/notes/review7-moonlight-white-20261018.json --format json
```

| slug | Original SHA-256（先頭16桁） | Current SHA-256（先頭16桁） | AI output SHA-256（先頭16桁） |
|---|---|---|---|
| `review6-blue-black-20261018` | `6627e06e4b9a57ac` | `84d15d402512dc3f` | `89ed5f818d7156f9` |
| `review7-moonlight-white-20261018` | `6627e06e4b9a57ac` | `58d9c0947acd1d62` | `89ed5f818d7156f9` |

両件の実行結果で `decision_recorded=false` を確認し、Inboxが保持した画像のサイズとSHA-256を元の登録用画像と照合した。
実行結果は `.synapsegit/notes/<slug>.receipt.json`、制作意図と添削は `.synapsegit/notes/review-20261019.md` に保存。
採用・不採用・保留は新たに記録せず、既存の判断と公開用bundleはそのまま残した。
