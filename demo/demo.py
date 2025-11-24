import sys
import time
from prettiprint import ConsoleUtils


def demo_messages(cu: ConsoleUtils) -> None:
    cu.header("Messages & Events")
    cu.success("Operation completed successfully.")
    cu.info("Fetching configuration from remote store...")
    cu.warning("API rate limit approaching (80%).")
    cu.error("Failed to connect to primary database.")
    cu.event("Log line at INFO level", level="INFO")
    cu.event("A successful operation event", level="SUCCESS")
    cu.event("Low disk space on node-7", level="WARNING")
    cu.event("Dead-letter queue growing rapidly", level="ERROR")
    cu.event("This is a DEBUG detail (only at verbosity >= 3)", level="DEBUG")


def demo_structure(cu: ConsoleUtils) -> None:
    cu.header("Structure: Panel, Markdown, Code, Rule")
    cu.panel("This message sits inside the default panel.", title="Default Panel")
    cu.panel("This message is blue on white inside a bold red panel.", title="Panel w/ [u]style[/u] & [u]border_style[/u] Args", style="blue on white", border_style="bold red")
    cu.panel("This message sits inside a [b]magenta[/b], [b]double box[/b] panel.", title="Panel w/ [b]border_style[/b] & [b]box[/b] Args", border_style="magenta", box="double")
    cu.panel("This message sits inside an [u]expanded[/u] [b]and[/b] [u]padded[/u] panel.", title="Panel w/ [b]padding[/b] & [b]expand[/b] Args", padding=1, expand=True)
    cu.markdown(
        "# Markdown Title\n"
        "- Bulleted item\n"
        "- **Bold** and *italics*\n"
        "> Blockquote\n\n"
        "```python\n"
        "def hello(name: str) -> str:\n"
        ' return f"Hello, {name}!"\n'
        "```"
    )
    cu.code(
        "import math\n\narea = math.pi * (10 ** 2)\nprint(area)",
        language="python",
        title="Syntax-Highlighted Code",
    )
    p_cmd = (
        f'PGPASSWORD="{cu.mask_secret("SuperSecretP@$$", keep=3)}" '
        f"psql -U aCoolUsername -h psqldb-pretti-printclust-prettiprint.dbuser -p 1234 -d PrettiPrintDatabase "
        f"-v ON_ERROR_STOP=1 "
        f'-f "/mnt/path/to/some-random/sql-file/temp.sql"'
    )
    cu.code(f"{p_cmd}", language="bash", title="Syntax-Highlighted Code w/ [b]wrap=True[/b] Arg", wrap=True)
    cu.rule("Adding 5 spaces between this horizontal rule (line) and the next")
    cu.spacer(5)
    cu.rule("End of structure demo")


def demo_data(cu: ConsoleUtils) -> None:
    cu.header("Data: Table, Dictionary, JSON, Tree")
    headers = ["Key", "Value"]
    rows = [["ENV", "prod"], ["REGION", "us-east-1"], ["REPLICAS", 3]]
    cu.table(headers, rows, title="Simple Table", expand=False)

    conf = {"env": "prod", "region": "us-east-1", "replicas": 3, "feature_x": True}
    cu.dictionary(conf, title="Key/Value Dictionary")
    cu.dictionary(conf, title="Key/Value Dictionary w/ [b]expand=False[/b] Arg", expand=False)

    api_payload = {"status": "ok", "items": [{"id": 1}, {"id": 2}], "meta": {"page": 1}}
    cu.json(api_payload, title="JSON Payload")

    nested = {
        "config": {
            "db": {"host": "localhost", "port": 5432},
            "cache": {"enabled": True, "ttl": 600},
        },
        "services": ["auth", "payments", "search"],
    }
    cu.tree(nested, title="Nested Structure")


def demo_secrets_and_kv(cu: ConsoleUtils) -> None:
    cu.header("Secrets & Key/Value")
    cu.key_value("USER", "service_account")
    cu.key_value("PASSWORD", "p@ssw0rd!", secret=True, keep=3)


def demo_progress_and_status(cu: ConsoleUtils) -> None:
    cu.header("Progress & Status")
    with cu.status("Connecting to remote service..."):
        time.sleep(0.5)

    with cu.progress() as prog:
        t1 = prog.add_task("Uploading artifacts", total=20)
        t2 = prog.add_task("Indexing search", total=10)
        for _ in range(20):
            prog.update(t1, advance=1)
            if prog.tasks[1].completed < prog.tasks[1].total:
                prog.update(t2, advance=1)
            time.sleep(0.04)
    cu.success("All tasks finished.")


def demo_prompts(cu: ConsoleUtils) -> None:
    cu.header("Prompts (skipped if non-interactive)")
    if sys.stdin.isatty():
        name = cu.prompt("Enter your name")
        proceed = cu.confirm("Proceed with deployment?")
        cu.info(f"Hello, {name}. Proceed = {proceed}")
    else:
        cu.warning("stdin is not a TTY; skipping interactive prompts.")


def demo_exceptions(cu: ConsoleUtils) -> None:
    cu.header("Exceptions (Rich Tracebacks)")
    try:
        _ = [1, 2, 3][5]
    except Exception:
        cu.print_exception()


def demo_themes(cu: ConsoleUtils) -> None:
    cu.header("Theme Switch")
    cu.info("Currently using theme: dark")
    cu.set_theme("light")
    cu.info("Now using theme: light")
    cu.set_theme("mono")
    cu.info("Now using theme: mono")
    cu.set_theme("dark")
    cu.info("Switched back to theme: dark")


def main() -> None:
    cu = ConsoleUtils(theme="dark", verbosity=2)

    cu.header("ConsoleUtils — Full Feature Demo")
    cu.event("Starting demo run", level="INFO")

    demo_messages(cu)
    demo_structure(cu)
    demo_data(cu)
    demo_secrets_and_kv(cu)
    demo_progress_and_status(cu)
    demo_prompts(cu)
    demo_exceptions(cu)
    demo_themes(cu)

    cu.event("Demo run complete", level="SUCCESS")
    cu.success("Done.")


def test_demo_main_runs_without_error():
    """Simple sanity check – just call main()."""
    main()  # will raise if anything goes wrong


if __name__ == "__main__":
    main()
