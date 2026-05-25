# Changelog

## 0.9.0 (2026-05-25)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.8.0...v0.9.0)

### Features

* **predictions:** add packshot overload to subscribe() ([1d522a9](https://github.com/fashn-AI/fashn-python-sdk/commit/1d522a92d6fff6c0964d29deb1efbb68beb5f178))

## 0.8.0 (2026-05-25)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([e8109bd](https://github.com/fashn-AI/fashn-python-sdk/commit/e8109bdf07184d1f1c66ed5cee66d6b43ac1b448))

## 0.7.0 (2026-05-18)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([e1b440e](https://github.com/fashn-AI/fashn-python-sdk/commit/e1b440e05e4ad6b082e18cfd4e7f056c49e63006))
* **api:** api update ([a1a6cb7](https://github.com/fashn-AI/fashn-python-sdk/commit/a1a6cb772cd946607d9fbcf3fd23840a78a5b5ad))
* **internal:** implement indices array format for query and form serialization ([2ad8553](https://github.com/fashn-AI/fashn-python-sdk/commit/2ad8553b3b0f32bb5f953b3ede77d7b9e85c94cc))
* support setting headers via env ([db06aa1](https://github.com/fashn-AI/fashn-python-sdk/commit/db06aa15f32069c87827c14701c16fd109a9827f))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([a03fa63](https://github.com/fashn-AI/fashn-python-sdk/commit/a03fa6302db29741dfb21e68705f8433799e767c))
* **deps:** bump minimum typing-extensions version ([f371db9](https://github.com/fashn-AI/fashn-python-sdk/commit/f371db9150fdd1fb62b35b5180c82957b33d6c10))
* ensure file data are only sent as 1 parameter ([40b2510](https://github.com/fashn-AI/fashn-python-sdk/commit/40b251066a744f93e34b84a296abb92c999d8bd6))
* **predictions:** sync subscribe() overloads with all supported models ([a94eab3](https://github.com/fashn-AI/fashn-python-sdk/commit/a94eab3d2bfe26798dd5c2062e69136dd8dd40f6))
* **pydantic:** do not pass `by_alias` unless set ([24078c2](https://github.com/fashn-AI/fashn-python-sdk/commit/24078c2f2d14ae384353332b005b4d1bf6f32ca6))
* sanitize endpoint path params ([c9c800b](https://github.com/fashn-AI/fashn-python-sdk/commit/c9c800b90a93f3bedb64dcb805db42d114b2a416))
* use correct field name format for multipart file arrays ([cf6df15](https://github.com/fashn-AI/fashn-python-sdk/commit/cf6df152d0a0fdd0e700684c5363c853986ca5e3))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([f28a133](https://github.com/fashn-AI/fashn-python-sdk/commit/f28a133be651105500944e3c6a88e4c5561e7848))


### Chores

* **ci:** skip lint on metadata-only changes ([0f1e02d](https://github.com/fashn-AI/fashn-python-sdk/commit/0f1e02df1bce5fabc5680ac191c12f75ed1fa4d0))
* **ci:** skip uploading artifacts on stainless-internal branches ([2f7216d](https://github.com/fashn-AI/fashn-python-sdk/commit/2f7216d6d0eb62f28275e52f770a9b35017a7bb1))
* **internal:** codegen related update ([66d022e](https://github.com/fashn-AI/fashn-python-sdk/commit/66d022eca7aac5cf3e463128d6190e71a37701d7))
* **internal:** codegen related update ([10ee22f](https://github.com/fashn-AI/fashn-python-sdk/commit/10ee22fe2fda58d1c17d96c832dd3c8af69f30a7))
* **internal:** codegen related update ([af155c4](https://github.com/fashn-AI/fashn-python-sdk/commit/af155c47f95c63fbbe5c77ae6edee25313636a5b))
* **internal:** more robust bootstrap script ([b5c90dd](https://github.com/fashn-AI/fashn-python-sdk/commit/b5c90ddb504d42e506f54ad4887fd0695a299f5e))
* **internal:** reformat pyproject.toml ([42e397d](https://github.com/fashn-AI/fashn-python-sdk/commit/42e397dcb4be3a55c8a87ce8006f570f2815e3e7))
* **internal:** tweak CI branches ([37ccb08](https://github.com/fashn-AI/fashn-python-sdk/commit/37ccb08393eeafcf770a0aff863d26048694c1c1))
* **internal:** update gitignore ([da97841](https://github.com/fashn-AI/fashn-python-sdk/commit/da978417054aa58dc4391cba02065a39661957d3))

## 0.6.0 (2026-03-05)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.5.1...v0.6.0)

### Features

* **api:** api update ([6a37d54](https://github.com/fashn-AI/fashn-python-sdk/commit/6a37d54930e4a5d2a8104729b8e95616cc56d2b2))
* **api:** api update ([6e05eed](https://github.com/fashn-AI/fashn-python-sdk/commit/6e05eed508d1b5169878ae1f2e0db5bc4e9f701c))
* **api:** api update ([1b202d7](https://github.com/fashn-AI/fashn-python-sdk/commit/1b202d744e0b3b63f73b91c25517450c06ac3788))
* **api:** api update ([1d48316](https://github.com/fashn-AI/fashn-python-sdk/commit/1d4831692c89407350c9354ed429d8c130237b6e))


### Bug Fixes

* **client:** close streams without requiring full consumption ([7f2a317](https://github.com/fashn-AI/fashn-python-sdk/commit/7f2a317e7d260ab21533ede03a34512f0e5606fe))
* compat with Python 3.14 ([0ebd493](https://github.com/fashn-AI/fashn-python-sdk/commit/0ebd493f5e52fa10309be08f903aec130b788545))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([02e60a5](https://github.com/fashn-AI/fashn-python-sdk/commit/02e60a5a2183f4e5b59b8026e7b7b3cc14d1045c))
* ensure streams are always closed ([c42ad27](https://github.com/fashn-AI/fashn-python-sdk/commit/c42ad278ce0d9de79d7f67fc219148ed95002bc0))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([3187855](https://github.com/fashn-AI/fashn-python-sdk/commit/318785576a99bc3ab99e92ca33efcb38f35db5bc))


### Chores

* add missing docstrings ([3e29ffc](https://github.com/fashn-AI/fashn-python-sdk/commit/3e29ffcd2cd8e00828120746e534970f92242db3))
* add Python 3.14 classifier and testing ([d214363](https://github.com/fashn-AI/fashn-python-sdk/commit/d214363530ebd44f7aab7edc4be0701135527bd1))
* bump `httpx-aiohttp` version to 0.1.9 ([1ca3adb](https://github.com/fashn-AI/fashn-python-sdk/commit/1ca3adb8ee1213a45dbed667bcce82daf4e46e62))
* configure new SDK language ([9d24d33](https://github.com/fashn-AI/fashn-python-sdk/commit/9d24d33bc8f91630593f2ec7f3062b795879880d))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([d19fca5](https://github.com/fashn-AI/fashn-python-sdk/commit/d19fca5446149c51099bbd24a2c66df9e54bb7e4))
* **docs:** use environment variables for authentication in code snippets ([ce72987](https://github.com/fashn-AI/fashn-python-sdk/commit/ce729878af36fe5a632e25bfee9c922c44d246cd))
* **internal/tests:** avoid race condition with implicit client cleanup ([fae7724](https://github.com/fashn-AI/fashn-python-sdk/commit/fae77243aa7878d870f90cfa1aec174c9200c49e))
* **internal:** add missing files argument to base client ([e0a4b27](https://github.com/fashn-AI/fashn-python-sdk/commit/e0a4b277ab86c3d6e277b474ff788648e653c90a))
* **internal:** grammar fix (it's -&gt; its) ([d9db081](https://github.com/fashn-AI/fashn-python-sdk/commit/d9db0817a2d06ddd03709abf98b52e387af2ac03))
* **package:** drop Python 3.8 support ([ad4cdda](https://github.com/fashn-AI/fashn-python-sdk/commit/ad4cddad58cfc1ae717233193c9450ab8d981543))
* update lockfile ([d5dd0bd](https://github.com/fashn-AI/fashn-python-sdk/commit/d5dd0bd5166d2409743e5d4bca6e78141e762fbe))

## 0.5.1 (2025-10-16)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.5.0...v0.5.1)

### Bug Fixes

* add error details to time_out ([5f35072](https://github.com/fashn-AI/fashn-python-sdk/commit/5f35072dc703907f5a8cebf82b2391e9d0b2f132))

## 0.5.0 (2025-10-15)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([df2f734](https://github.com/fashn-AI/fashn-python-sdk/commit/df2f7341c02b3cc54d3aebdd9da428fa5d991bed))
* return credits used information on .subscribe response ([0bc5bd3](https://github.com/fashn-AI/fashn-python-sdk/commit/0bc5bd387547fef6b979dc96bcb7520e2ac98cd8))

## 0.4.0 (2025-10-14)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.3.0...v0.4.0)

### Features

* add subscribe method to readme ([646b54e](https://github.com/fashn-AI/fashn-python-sdk/commit/646b54e4144616bb66e1786ffd7240e024f81934))
* **api:** api update ([f2cee2f](https://github.com/fashn-AI/fashn-python-sdk/commit/f2cee2f380bab897f5dfd670e9b7b46cc7e44fd8))
* **api:** increase exponential backoff ([58f4dda](https://github.com/fashn-AI/fashn-python-sdk/commit/58f4ddac6953aeb62bda0ca6a6e4d8141bd5db4d))
* improve subscribe types ([69e957f](https://github.com/fashn-AI/fashn-python-sdk/commit/69e957f546ed478c97686fa16277ca5ceac6c8e3))
* subscribe method ([36bc09d](https://github.com/fashn-AI/fashn-python-sdk/commit/36bc09dfb2c795596b21f63a673a3fca502263e8))


### Bug Fixes

* code improvement ([daba9da](https://github.com/fashn-AI/fashn-python-sdk/commit/daba9da1dc5dffa0354df576a6fe7180469e7ca9))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([fecc0e9](https://github.com/fashn-AI/fashn-python-sdk/commit/fecc0e985d812a6b9fad8fd45bb89e7ef2c77858))
* **internal:** detect missing future annotations with ruff ([77108a8](https://github.com/fashn-AI/fashn-python-sdk/commit/77108a88d071abac0dfbcf0b0718f4de15a410a1))

## 0.3.0 (2025-09-19)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([7f876c9](https://github.com/fashn-AI/fashn-python-sdk/commit/7f876c9b44079101a58a7166808a633004e95741))
* improve future compat with pydantic v3 ([3fc2f9d](https://github.com/fashn-AI/fashn-python-sdk/commit/3fc2f9dc6403acbe64e80a1178a0347d17092ac3))
* **types:** replace List[str] with SequenceNotStr in params ([286ef4e](https://github.com/fashn-AI/fashn-python-sdk/commit/286ef4ef48e6d46aec17dfd6d3dda97a45f882bd))


### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([d8f2828](https://github.com/fashn-AI/fashn-python-sdk/commit/d8f28288999deebb4157b3aadec57b66c16ac23a))
* **internal:** update pydantic dependency ([3c83614](https://github.com/fashn-AI/fashn-python-sdk/commit/3c836141967893376cf27455b557502ffb4df84b))
* **tests:** simplify `get_platform` test ([79d1616](https://github.com/fashn-AI/fashn-python-sdk/commit/79d1616da404997d756b09df97a52d4c2f968bb9))
* **types:** change optional parameter type from NotGiven to Omit ([a4f7331](https://github.com/fashn-AI/fashn-python-sdk/commit/a4f73319526bf71f8d2deaad423cd9a063d0cf27))

## 0.2.0 (2025-09-02)

Full Changelog: [v0.1.2...v0.2.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.1.2...v0.2.0)

### Features

* **api:** api update ([d0c0d42](https://github.com/fashn-AI/fashn-python-sdk/commit/d0c0d42d7596cac8e93bb897053075d5054f2215))


### Bug Fixes

* avoid newer type syntax ([dde8e6a](https://github.com/fashn-AI/fashn-python-sdk/commit/dde8e6ac8238605cda949c416f4a297e49f44d6a))


### Chores

* **internal:** add Sequence related utils ([016f338](https://github.com/fashn-AI/fashn-python-sdk/commit/016f3385ce35a370a71ecbe21034ccd450575517))
* **internal:** update pyright exclude list ([61d426f](https://github.com/fashn-AI/fashn-python-sdk/commit/61d426f2120d380dd2f2e71af37a10a386eae009))

## 0.1.2 (2025-08-26)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.1.1...v0.1.2)

### Chores

* **internal:** change ci workflow machines ([94ff961](https://github.com/fashn-AI/fashn-python-sdk/commit/94ff961e1d80f4b1286cb40e057dd0d3c95c9d14))

## 0.1.1 (2025-08-25)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.1.0...v0.1.1)

### Documentation

* **readme:** add companies logo and docs links ([f9d3691](https://github.com/fashn-AI/fashn-python-sdk/commit/f9d36914b08a393c9c574449f044d9709fa74d98))

## 0.1.0 (2025-08-25)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([fe3a623](https://github.com/fashn-AI/fashn-python-sdk/commit/fe3a623d72d311534abceced08d840a6ca5314fe))
* **api:** manual updates ([b6a92ae](https://github.com/fashn-AI/fashn-python-sdk/commit/b6a92ae3f706f4ce1b9230883cac47aaec35560f))
* **api:** manual updates ([39f855f](https://github.com/fashn-AI/fashn-python-sdk/commit/39f855fe0bce79fa7b838b1730174e1424843e87))


### Chores

* configure new SDK language ([f7194c0](https://github.com/fashn-AI/fashn-python-sdk/commit/f7194c0976fc9f5656b1152814084af358e06c8e))
* update github action ([5959e35](https://github.com/fashn-AI/fashn-python-sdk/commit/5959e3515f9dbe77776331f33892843cc3cce6eb))
* update SDK settings ([fa39844](https://github.com/fashn-AI/fashn-python-sdk/commit/fa39844915b3dcd00282863b02b2ebff94229eec))
