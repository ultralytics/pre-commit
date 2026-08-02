# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

Ultralytics Pre-commit (`ultralytics-pre-commit-hooks`, AGPL-3.0) is a small collection of [pre-commit](https://pre-commit.com/) hooks that enforce Ultralytics code-quality standards. Consumers reference this repository from their own `.pre-commit-config.yaml`; it is not published to PyPI.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Run a hook end-to-end exactly as a consumer would, from a scratch git repo
uvx pre-commit try-repo /path/to/this/clone capitalize-comments --all-files

# Run a hook script directly against files
python capitalize_comments.py path/to/file.py
```

- There is no test suite. CI is only `format.yml` (Ultralytics Actions autoformat, labels, PR summaries) and `cla.yml`; neither exercises the hooks.
- Always verify a hook change with `pre-commit try-repo` against a scratch repository — a hook that fails to resolve its entry point still reports as a normal hook failure, so nothing else in this repo will catch it.

## Architecture

Each hook is a standalone Python script at the repository root exposing a `main()` that processes the file paths pre-commit passes in `sys.argv[1:]`:

- `capitalize_comments.py` — capitalizes the first letter of standalone inline comments. It skips any line containing an `EXCLUDE_TERMS` token and any comment directly preceded by another comment, so only single-line comments are rewritten.

Three files must stay in sync for a hook to run:

- `capitalize_comments.py` (or any new hook script) defines `main()`.
- `pyproject.toml` `[project.scripts]` maps a console-script name to `module:main`.
- `.pre-commit-hooks.yaml` declares the hook's `id`, `name`, `description`, `entry`, `language`, and `types`.

`language: python` hooks resolve `entry` on `PATH` inside the isolated environment pre-commit builds from `pyproject.toml`, so `entry` must be a console-script name, never a filename — a filename fails at run time with ``Executable `...` not found``. The hook `id` is the consumer-facing contract: renaming one breaks every `.pre-commit-config.yaml` that references it.

## Conventions

- Every file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds headers automatically; don't add or revert them manually.
- Google-style docstrings and Ruff formatting at line length 120, applied automatically by `format.yml` on PRs.
- Hooks rewrite files in place and let pre-commit report the diff, so they must be idempotent: a second run over the same files must change nothing.
- `version` in `pyproject.toml` is pinned at `0.0.0` because consumers pin a git `rev` rather than a release — leave it alone.
