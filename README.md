# Ultralytics Pre-commit Hooks

This repository contains pre-commit hooks developed by [Ultralytics](https://ultralytics.com) for ensuring code quality and standards.

## Repository Structure

The repository is structured as follows:

- A `hooks` directory that contains all the individual Python scripts which act as the hooks.
- A `.pre-commit-hooks.yaml` file at the root, which defines the hooks that are available for installation.

### Hook Scripts in `hooks` Directory

Each hook is a Python script placed inside the `hooks` directory. For example, the `capitalize_comments.py` script provides functionality to capitalize the first letter of standalone inline comments.

### Defining Hooks in `.pre-commit-hooks.yaml`

Each hook that's available for installation needs to be defined in the `.pre-commit-hooks.yaml` file. A hook definition looks like this:

```yaml
- id: hook-id
  name: 'Descriptive Hook Name'
  entry: hooks/hook_script.py
  language: python
  types: [python]
```

Where:

- `hook-id` is a unique identifier for the hook.
- `Descriptive Hook Name` is a short name that describes what the hook does.
- `hook_script.py` is the script in the `hooks` directory that implements the hook.

## Adding Additional Hooks

To add a new hook:

1. **Create the Hook Script**: Write a Python script that implements your hook and place it in the `hooks` directory. Ensure the script has the necessary error handling and provides meaningful output messages.
2. **Define the Hook**: Add a new entry for your hook in the `.pre-commit-hooks.yaml` file, following the structure mentioned above.
3. **Test the Hook**: It's important to test the new hook locally in a project to ensure it behaves as expected.
4. **Commit and Push**: Once you've tested the hook, commit your changes to this repository and push.

## Installing Hooks in Your Project

In your main project's `.pre-commit-config.yaml`, you can reference the remote hook repository:

```yaml
- repo: https://github.com/ultralytics/pre-commit
  rev: main  # or a specific git tag/revision
  hooks:
    - id: hook-id
```

Then, run the following command in your project directory:

```bash
pre-commit install
```

Now, whenever you make a commit in your project, the pre-commit hooks from this repository will be executed as part of the checks.

## Contributing

Contributions to expand and enhance these hooks are welcome! Please ensure that any new hooks are well-tested before submitting a pull request.
