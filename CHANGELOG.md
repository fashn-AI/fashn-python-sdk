# Changelog

## 0.5.2 (2025-11-04)

Full Changelog: [v0.5.1...v0.5.2](https://github.com/fashn-AI/fashn-python-sdk/compare/v0.5.1...v0.5.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([7f2a317](https://github.com/fashn-AI/fashn-python-sdk/commit/7f2a317e7d260ab21533ede03a34512f0e5606fe))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([1ca3adb](https://github.com/fashn-AI/fashn-python-sdk/commit/1ca3adb8ee1213a45dbed667bcce82daf4e46e62))
* **internal/tests:** avoid race condition with implicit client cleanup ([fae7724](https://github.com/fashn-AI/fashn-python-sdk/commit/fae77243aa7878d870f90cfa1aec174c9200c49e))
* **internal:** grammar fix (it's -&gt; its) ([d9db081](https://github.com/fashn-AI/fashn-python-sdk/commit/d9db0817a2d06ddd03709abf98b52e387af2ac03))

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
