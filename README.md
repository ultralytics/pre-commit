<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

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

## Contribute

We love your input! Ultralytics open-source efforts would not be possible without help from our community. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started, and fill out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) to send us feedback on your experience. Thank you 🙏 to all our contributors!

<!-- SVG image from https://opencollective.com/ultralytics/contributors.svg?width=990 -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

## License

Ultralytics offers two licensing options to accommodate diverse use cases:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/licenses/) open-source license is ideal for students and enthusiasts, promoting open collaboration and knowledge sharing. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for more details.
- **Enterprise License**: Designed for commercial use, this license permits seamless integration of Ultralytics software and AI models into commercial goods and services, bypassing the open-source requirements of AGPL-3.0. If your scenario involves embedding our solutions into a commercial offering, reach out through [Ultralytics Licensing](https://ultralytics.com/license).

## Contact

For Ultralytics bug reports and feature requests please visit [GitHub Issues](https://github.com/ultralytics/xview-yolov3/issues), and join our [Discord](https://ultralytics.com/discord) community for questions and discussions!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>

