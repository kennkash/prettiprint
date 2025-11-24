# prettiprint ![](pre-commit-enabled.svg)![](version.svg)

Beautiful, consistent, and developer-friendly CLI output built on [Rich](https://github.com/Textualize/rich).

- Themes (`dark`, `light`, `mono`) with optional custom styles
- Structured output: headers, rules, panels, markdown, syntax-highlighted code
- Data helpers: tables, key-value dictionaries, JSON, trees
- Progress bars & spinners (elapsed/remaining time)
- Secrets masking with partial reveal
- Event/log lines with timestamps and levels
- Pretty tracebacks
- Interactive prompts & confirmations
- Verbosity control (0..3)
- Backward-compatible wrappers for your original functions

## 📚 Table of Contents

- [📄 Requirements](#requirements)
- [📦 Installation](#installation)
- [⬆️ Upgrade Package](#upgrade-package)
- [🛠 Development Setup](#development-setup)
- [⚡ Quick Start](#quick-start)
- [📘 API Overview](#api-overview)
	- [🔧 Initialization](#initialization)
	- [🧱 Structure & Layout Methods](#structure--layout-methods)
	- [✅ Message Methods](#message-methods)
	- [📊 Data Display Methods](#data-display-methods)
	- [🔐 Secret & Key Management](#secret--key-management)
	- [⏳ Progress & Status Methods](#progress--status-methods)
	- [✋ Prompt Methods](#prompt-methods)
	- [⚠ Exception Handling](#exception-handling)
	- [🎛 Configuration & Runtime Control](#configuration--runtime-control)
- [🖥️ External Resources](#external-resources)



## Requirements

- Python **3.9+**
- `rich>=14.2.0` (see [requirements.txt](requirements.txt))


## Installation

#### Command Line Interface

Install the package in your virtual environment:
```bash
pip install prettiprint --extra-index-url https://gitlab.smartcloud.samsungds.net/api/v4/projects/6621/packages/pypi/simple
```


#### requirements.txt

To add the package to various requirements.txt files:
```txt
<other requirements>

--extra-index-url https://gitlab.smartcloud.samsungds.net/api/v4/projects/6621/packages/pypi/simple
prettiprint
```


## Upgrade Package

#### Command Line Interface

Upgrade the package in your virtual environment:
```bash
pip install --upgrade prettiprint --extra-index-url https://gitlab.smartcloud.samsungds.net/api/v4/projects/6621/packages/pypi/simple
```

## Development Setup
```bash
pip install -r requirements.txt
```
```bash
pip install -r dev-requirements.txt
```

See also: [Makefile](https://gitlab.smartcloud.samsungds.net/k.kashmiry/prettiprint/-/blob/27e23efb8d492f0b1e8e95b2a481c53869ced4a4/Makefile)
<details>
<summary><strong>Example Use</strong></summary>
<!--All you need is a blank line-->

```bash
#CLI
make setup
make build
```
</details>





## Quick Start

```python
from prettiprint import ConsoleUtils

cu = ConsoleUtils(theme="dark", verbosity=2)

cu.header("Quick Start Demo")
cu.info("Connecting to service...")
cu.success("Connection established!")

cu.dictionary({"env": "prod", "region": "us-east-1", "env_password": cu.mask_secret("$upaS3cr3t", keep=3)}, title="Deployment Context")
cu.key_value("PASSWORD", "p@ssw0rd!", secret=True, keep=3)

with cu.status("Performing operation..."):
	time.sleep(1)
	pass
with cu.progress() as prog:
	task = prog.add_task("Uploading artifacts", total=10)
	for _ in range(10):
		prog.update(task, advance=1)
		time.sleep(0.4)
cu.success("All done!")
```
<details>
<summary><strong>Run the full <a href="demo/demo.py">demo</a></strong></summary>
<!--All you need is a blank line-->

```bash
python demo.py
```
</details>


## API Overview

### Initialization
```python
from prettiprint import ConsoleUtils
cu = ConsoleUtils(theme="dark", verbosity=2)
```

| Parameter | Type | Default | Description |
|------------------|-------|---------|-------------|
| theme | str | "dark" | Choose from `dark`, `light`, `mono` |
| emoji | bool | True | Enables emoji display → ✅/ℹ️/⚠️/❌ |
| timestamps | bool | True | Include timestamps in [event](src/prettiprint/prettiprint.py#L246) logs |
| verbosity | int | 1 | Levels: `0=silent`, `1=normal`, `2=verbose`, `3=debug` |
| enable_tracebacks| bool | True | Enables pretty Rich tracebacks |
| custom_styles | dict | None | Override or extend color styles from the [preset theme](src/prettiprint/prettiprint.py#L27) |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
# ============================#
#         Custom Styles       #
# ============================#

cu = ConsoleUtils(
	theme="dark", 
	verbosity=2,
	custom_styles={
		"panel": "bold magenta",
		"header": "white on blue",
		"success": "bold white on green"
	}
)
```
</details>

---

### Structure & Layout Methods

| Method | Description |
|-------|-------------|
| header(text, style=None) | Prints a section header |
| rule(text="", label_style=None, line_style=None) | Inserts a horizontal separator |
| spacer(size) | Add visual spacing between console elements; size (int,str) sets the number of spaces to add |
| panel(message, title=None, style=None, border_style=None, box=None, expand=False, padding=None) | Renders a bordered panel |
| markdown(text) | Renders Markdown content |
| code(text, language="python", title=None, wrap=False) | Syntax-highlighted code block; word wraps code when wrap=True  |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
# ============================#
#           Markdown          #
# ============================#

cu.markdown(
    "# Markdown Title\n"
    "- Bulleted item\n"
    "- **Bold** and *italics*\n"
    "> Blockquote\n\n"
    "```python\n"
    "def hello(name: str) -> str:\n"
    " return f\"Hello, {name}!\"\n"
    "```"
)
```
</details>

---

### Message Methods

| Method | Description |
|------------|-------------|
| success(message) | ✅ Green success message |
| info(message) | ℹ️ Informational message |
| warning(message) | ⚠️ Warning message |
| error(message) | ❌ Error message |
| event(message, level="INFO") | Timestamped log with severity level|

>>> [!note] Note
For the **event** method consider the following:
<details>
<summary><strong>Considerations</strong></summary>
<!--All you need is a blank line-->

1. If `verbosity < 2`, event() logs will <ins>**not**</ins> be output
2. If `verbosity < 3`, **DEBUG** event() logs will <ins>**not**</ins> be output

</details>
>>>

---

### Data Display Methods

| Method | Description |
|-------|-------------|
| table(headers, rows, title=None, header_style=None, expand=False) | Display tabular data |
| dictionary(mapping, title=None, expand=True) | Render key-value mappings |
| json(data, title=None) | Pretty-printed JSON |
| tree(obj, title="Structure") | Visualize nested data structures |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
# =========================#
#           Table          #
# =========================#

headers = ["Key", "Value"]
rows = [["ENV", "prod"], ["REGION", "us-east-1"], ["REPLICAS", 3]]
cu.table(headers, rows, title="Simple Table", expand=False)

# =========================#
#           Tree           #
# =========================#

nested = {
    "config": {
        "db": {"host": "localhost", "port": 5432},
        "cache": {"enabled": True, "ttl": 600},
    },
    "services": ["auth", "payments", "search"],
}
cu.tree(nested, title="Nested Structure")
```
</details>

---

### Secret & Key Management

| Method | Description |
|--------|-------------|
| key_value(key, value, secret=False, keep=3) | Print key/value pairs; masks the value when secret=True |
| mask_secret(secret, keep=3, mask="*") | Utility to mask secret strings |

---

### Progress & Status Methods

| Method | Description |
|--------|-------------|
| status(text) | Display a spinner during execution |
| progress(transient=True, show_speed=True, description="") | Show a progress bar for tasks |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
# =========================#
#          Status          #
# =========================#

with cu.status("Connecting to remote service..."):
	time.sleep(1)

# ==========================#
#         Progress          #
# ==========================#

with cu.progress() as prog:
	t1 = prog.add_task("Uploading artifacts", total=20)
	t2 = prog.add_task("Indexing search", total=10)
	for _ in range(20):
		prog.update(t1, advance=1)
		if prog.tasks[1].completed < prog.tasks[1].total:
			prog.update(t2, advance=1)
		time.sleep(0.4)
cu.success("All tasks finished.")
```
</details>

---

### Prompt Methods

| Method | Description |
|--------|-------------|
| prompt(message, password=False) | Ask the user for input |
| confirm(message, default=True) | Prompt for Yes/No confirmation |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
if sys.stdin.isatty():
	name = cu.prompt("Enter your name")
	proceed = cu.confirm("Proceed with deployment?")
	cu.info(f"Hello, {name}. Proceed = {proceed}")
else:
	cu.warning("stdin is not a TTY; skipping interactive prompts.")
```
</details>

---

### Exception Handling

| Method | Description |
|--------|-------------|
| print_exception() | Capture and display Rich-formatted exceptions |

<details>
<summary><strong>Example Code</strong></summary>
<!--All you need is a blank line-->

```python
try:
	_ = [1, 2, 3][5]
except Exception:
	cu.print_exception()
```
</details>

---

### Configuration & Runtime Control

| Method | Description |
|--------|-------------|
| set_theme(name, custom_styles=None) | Switch themes at runtime |
| set_verbosity(level) | Control verbosity of output |

>>> [!important] Verbosity Levels
+ `verbosity=0` → silent
    + **no logs** output
+ `verbosity=1` → normal
    + headers/tables/messages/panels etc.
    + **no event() logs** output
+ `verbosity=2` → verbose
    + **_most_ event() logs** output
        + INFO/SUCCESS/WARNING/ERROR
+ `verbosity=3` → debug
    + **all event() logs** output
        + DEBUG

The **default** verbosity level is `1`
>>>


## External Resources
+ Discover **style definitions** that can be used with the `style` parameter [here](https://rich.readthedocs.io/en/latest/style.html)