# 星月夜の上塗り（白・青・黒の明度5段階）

> SynapseGit provider-neutral publication view · visibility `public` · network operations `0`

IKEA の星月夜レプリカに白・青・黒のアクリルを重ね、明度5段階の絵に描き替える制作の記録。  
AI（Claude Code）が明度の見本と工程ごとの地図を提案し、制作者が工程ごとに採用・不採用・保留を判断した。  
画像そのものはこのリポジトリの photos/registered/ と output/ にあり、下の SHA\-256 で照合できる。

Creator label: **howlrs** (author supplied)
Proposal agent label: **Claude Code（make\_values.py／make\_steps.py で作成した見本と地図）** (author supplied)

## Reading this history

This view separates the original, the recorded current state, the AI-attributed proposal, and the Human decision. OIDs verify byte identity in the source repository; they do not prove authorship, truth, copyright, permission, or physical change.

## 計画: 明度5段階の完成見本

Session: `inbox-plan-blue-5values`

### Work history

| Role | Public caption | Verified source OID | Rendering |
|---|---|---|---|
| Original | 塗る前のレプリカ（photos/registered/20261009\_step1\_before.jpg） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| Current | 塗る前のレプリカ（Original と同じ写真） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| AI\-attributed proposal | 明度5段階の見本（output/03\_value5\_blue.png） | `blob:sg-oid-v1:sha256:89ed5f818d7156f9658503834a5aa0d1a7715e68d9bcf582faddc59e0d3b7140` | Raw asset bytes are not copied by the M0/M1 safe publication profile |

### Proposal and Human decision

- Proposal attribution: Caller\-supplied output recorded by the workflow as AI\-attributed; no model invocation is independently verified
- Human disposition: **adopt**
- Selected role: **AI\-attributed proposal**
- Proposal retained in history even when unselected: `true`

No public decision note was supplied. The source rationale remains redacted because its stored visibility is private and its training-use policy is prohibited.

### Evidence

The current comparison reports **identical** with comparability **partial**. This compares primary Blob bytes only; it is not a pixel, semantic, or physical\-change analysis.

### Technical provenance

- Proposal Ref: `proposal/creator-agent/inbox-plan-blue-5values`
- Decision Ref: `decision/creator/inbox-plan-blue-5values`
- Base head: `commit:sg-oid-v1:sha256:d864d469f74666b17a664b156271ac243a513820e0f5e19234a1bcda7d0ae3e0`
- Proposal head: `commit:sg-oid-v1:sha256:f83efe893ed12d03a187b43c8a6eb8af0d85c1abbd9422338c81b0e0236920c5`
- Decision head: `commit:sg-oid-v1:sha256:fbf99e4feb9c8f88f37ea02d441e8e314892be4a73da13d4bd14f14f5c6eb3c0`
- Projection fingerprint: `projection-source-v1:sha256:14cf952d90f48c931877c5c716ee1da7376ad5904e9a3c97ed755d49db385461`
- Objects verified by session fsck: `105`

## 工程1: 白

Session: `inbox-step1-white`

### Work history

| Role | Public caption | Verified source OID | Rendering |
|---|---|---|---|
| Original | 塗る前のレプリカ（photos/registered/20261009\_step1\_before.jpg） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| Current | 工程1の前（塗る前と同じ写真） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| AI\-attributed proposal | 工程1の地図（output/steps\_blue/step1\_white.png）。赤い輪郭が白で塗る場所 | `blob:sg-oid-v1:sha256:15d6817cbe7dd7e368bca0d2b1b6541d933f20f34b5a1966373dcc5e8afc9f5f` | Raw asset bytes are not copied by the M0/M1 safe publication profile |

### Proposal and Human decision

- Proposal attribution: Caller\-supplied output recorded by the workflow as AI\-attributed; no model invocation is independently verified
- Human disposition: **adopt**
- Selected role: **AI\-attributed proposal**
- Proposal retained in history even when unselected: `true`

No public decision note was supplied. The source rationale remains redacted because its stored visibility is private and its training-use policy is prohibited.

### Evidence

The current comparison reports **identical** with comparability **partial**. This compares primary Blob bytes only; it is not a pixel, semantic, or physical\-change analysis.

### Technical provenance

- Proposal Ref: `proposal/creator-agent/inbox-step1-white`
- Decision Ref: `decision/creator/inbox-step1-white`
- Base head: `commit:sg-oid-v1:sha256:6e71835992b9006959ba4a6302ba70c39219df90928a7ac5184cf89f62311d64`
- Proposal head: `commit:sg-oid-v1:sha256:ee46f491f8ee223376e4d7eca2dee954a477934ba5b6f556e1cbf8f4bc131fb5`
- Decision head: `commit:sg-oid-v1:sha256:18fdac0fef57ce871ce035db944ded4c1facecbc4b42cedc65667ef3e6553001`
- Projection fingerprint: `projection-source-v1:sha256:14cf952d90f48c931877c5c716ee1da7376ad5904e9a3c97ed755d49db385461`
- Objects verified by session fsck: `105`

## 工程2: 明るい青

Session: `inbox-step2-lightblue`

### Work history

| Role | Public caption | Verified source OID | Rendering |
|---|---|---|---|
| Original | 塗る前のレプリカ（photos/registered/20261009\_step1\_before.jpg） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| Current | 工程1（白）の後（photos/registered/20261009\_step1\_after.jpg） | `blob:sg-oid-v1:sha256:059f89438a5ae261230bdad08af74185acf7363ccd1ef8e4d14c1ad6ca7ee7ba` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| AI\-attributed proposal | 工程2の地図（output/steps\_blue/step2\_lightblue.png） | `blob:sg-oid-v1:sha256:086296b2706eafa2e8fa5a108563bf6f70580c3f7c7d91059509dca38e59516a` | Raw asset bytes are not copied by the M0/M1 safe publication profile |

### Proposal and Human decision

- Proposal attribution: Caller\-supplied output recorded by the workflow as AI\-attributed; no model invocation is independently verified
- Human disposition: **adopt**
- Selected role: **AI\-attributed proposal**
- Proposal retained in history even when unselected: `true`

No public decision note was supplied. The source rationale remains redacted because its stored visibility is private and its training-use policy is prohibited.

### Evidence

The current comparison reports **different** with comparability **partial**. This compares primary Blob bytes only; it is not a pixel, semantic, or physical\-change analysis.

### Technical provenance

- Proposal Ref: `proposal/creator-agent/inbox-step2-lightblue`
- Decision Ref: `decision/creator/inbox-step2-lightblue`
- Base head: `commit:sg-oid-v1:sha256:dee46c46f4775aceab929f109c5d6e90f271e9f7abbaceae8ae1ecfebfaee64f`
- Proposal head: `commit:sg-oid-v1:sha256:9596e8ac1239e909afc5e53775ceac8c1322574d64784257203bb8d3298b1664`
- Decision head: `commit:sg-oid-v1:sha256:347765f28f92de62b6512c61d22c4c70fcef4cf385857448705103417860f24a`
- Projection fingerprint: `projection-source-v1:sha256:14cf952d90f48c931877c5c716ee1da7376ad5904e9a3c97ed755d49db385461`
- Objects verified by session fsck: `105`

## 工程3: 中間の青

Session: `inbox-step3-midblue`

### Work history

| Role | Public caption | Verified source OID | Rendering |
|---|---|---|---|
| Original | 塗る前のレプリカ（photos/registered/20261009\_step1\_before.jpg） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| Current | 工程1の後の写真で代用（工程2と3を続けて塗り、その間の写真がないため） | `blob:sg-oid-v1:sha256:059f89438a5ae261230bdad08af74185acf7363ccd1ef8e4d14c1ad6ca7ee7ba` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| AI\-attributed proposal | 工程3の地図（output/steps\_blue/step3\_midblue.png） | `blob:sg-oid-v1:sha256:e144bc9d6692fe2ad6cb2d880a6a94dac516022114f67e21fb51dfdc9d49a193` | Raw asset bytes are not copied by the M0/M1 safe publication profile |

### Proposal and Human decision

- Proposal attribution: Caller\-supplied output recorded by the workflow as AI\-attributed; no model invocation is independently verified
- Human disposition: **adopt**
- Selected role: **AI\-attributed proposal**
- Proposal retained in history even when unselected: `true`

No public decision note was supplied. The source rationale remains redacted because its stored visibility is private and its training-use policy is prohibited.

### Evidence

The current comparison reports **different** with comparability **partial**. This compares primary Blob bytes only; it is not a pixel, semantic, or physical\-change analysis.

### Technical provenance

- Proposal Ref: `proposal/creator-agent/inbox-step3-midblue`
- Decision Ref: `decision/creator/inbox-step3-midblue`
- Base head: `commit:sg-oid-v1:sha256:45e33ed559ebf78312b0037efc6e5f8c0c10ecea2b2aea7a7d7f3916f2256dbb`
- Proposal head: `commit:sg-oid-v1:sha256:379b54832710d148e502b2a70bd3b1610eaa8529fc67bbfd5f1c38a16e1699e0`
- Decision head: `commit:sg-oid-v1:sha256:0f2133a53c862bb0c72c26d49920228c0f07749881d532a1cf2aa865eeb7bb06`
- Projection fingerprint: `projection-source-v1:sha256:14cf952d90f48c931877c5c716ee1da7376ad5904e9a3c97ed755d49db385461`
- Objects verified by session fsck: `105`

## 工程4: 青

Session: `inbox-step4-blue`

### Work history

| Role | Public caption | Verified source OID | Rendering |
|---|---|---|---|
| Original | 塗る前のレプリカ（photos/registered/20261009\_step1\_before.jpg） | `blob:sg-oid-v1:sha256:6627e06e4b9a57ac237342a950f3454ef5c3afe99ed6a96885b84dcd269590b7` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| Current | 工程2・3と空の一部の黒の後（photos/registered/20261009\_step2\-3\_after.jpg） | `blob:sg-oid-v1:sha256:f8ecbb5935343fecb58e3476889d2a532b51c7868f290e01a5b4c8805f605784` | Raw asset bytes are not copied by the M0/M1 safe publication profile |
| AI\-attributed proposal | 工程4の地図（output/steps\_blue/step4\_blue.png） | `blob:sg-oid-v1:sha256:5290abe05ec019b1a4ab1ad33e7dc78a4544ff4399f87836e5d1138a16efb37c` | Raw asset bytes are not copied by the M0/M1 safe publication profile |

### Proposal and Human decision

- Proposal attribution: Caller\-supplied output recorded by the workflow as AI\-attributed; no model invocation is independently verified
- Human disposition: **adopt**
- Selected role: **AI\-attributed proposal**
- Proposal retained in history even when unselected: `true`

No public decision note was supplied. The source rationale remains redacted because its stored visibility is private and its training-use policy is prohibited.

### Evidence

The current comparison reports **different** with comparability **partial**. This compares primary Blob bytes only; it is not a pixel, semantic, or physical\-change analysis.

### Technical provenance

- Proposal Ref: `proposal/creator-agent/inbox-step4-blue`
- Decision Ref: `decision/creator/inbox-step4-blue`
- Base head: `commit:sg-oid-v1:sha256:17879ed286efb6290372c309d4931d5a64a69bde7ce8ed61eac33da161feeff1`
- Proposal head: `commit:sg-oid-v1:sha256:8ce4aec1c91f3298ce05e68b9324cc117124833eefbbe8fe701e51bdb0bfc8a4`
- Decision head: `commit:sg-oid-v1:sha256:0e283454e00a42956bcf00f13b380deb3969f5197f6f4f4a65fd2f5bbeeedb05`
- Projection fingerprint: `projection-source-v1:sha256:14cf952d90f48c931877c5c716ee1da7376ad5904e9a3c97ed755d49db385461`
- Objects verified by session fsck: `105`

## Disclosure and limits

- **byte\_identity\_only** — SynapseGit verifies stored bytes and graph relations; it does not prove authorship, truth, rights, permission, or physical change.
- **raw\_assets\_omitted** — Original, current, and proposal bytes are omitted by default to avoid leaking metadata, active content, or unrelated private material.
- **private\_rationale\_redacted** — The source CreatorReport does not expose a verified feedback visibility policy. Its rationale is therefore withheld; only a separately supplied public decision note may appear.
- **attribution\_is\_scoped** — The proposal is AI\-attributed by the recorded workflow. This bundle does not verify that a model generated the supplied bytes or identify a model invocation.
- **training\_prohibited** — Machine\-readable output is provided for inspection and interoperability, not as permission to train on the content.
- **local\_bundle\_only** — This export performs no Git, GitHub, Synapse service, upload, or other network operation and contains no remote publication receipt.
- **identifier\_correlation** — Artifact OIDs and technical Ref/Commit identifiers can correlate this view with another copy of the same history; review them before external publication.
- **bundle\_not\_signed** — Checksums detect accidental bundle damage but are not an identity signature or proof of who published the bundle.

Machine-readable semantics are available in [`projection.json`](./projection.json). Machine readability does not grant training permission; this bundle declares `training_use_policy=prohibited`.
