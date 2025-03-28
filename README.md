<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🛠️ Ultralytics Pre-commit Hooks

Welcome to the Ultralytics pre-commit hooks repository! This collection features hooks developed by [Ultralytics](https://www.ultralytics.com/) to enforce code quality and maintain consistent standards across our software projects. Integrating these hooks into your development workflow automates code validation, ensuring a high level of code hygiene and reducing manual review efforts. Learn more about the [pre-commit framework](https://pre-commit.com/) itself on their official website.

[![Ultralytics Actions](https://github.com/ultralytics/pre-commit/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/pre-commit/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## 🗂️ Repository Structure

This repository is organized for clarity and ease of use:

-   **`hooks/` directory:** Contains individual [Python](https://www.python.org/) scripts, each representing a distinct pre-commit hook designed for specific checks or code formatting tasks.
-   **`.pre-commit-hooks.yaml`:** The root configuration file defining the available hooks, making them discoverable and easy to integrate into your projects.

### Hook Scripts in `hooks` Directory 📂

Each script within the `hooks` directory is a standalone Python program performing a specific pre-commit task. For instance:

-   `capitalize_comments.py`: Ensures that standalone inline comments start with a capital letter, promoting readability and a professional coding style.

### Defining Hooks in `.pre-commit-hooks.yaml` 📘

The `.pre-commit-hooks.yaml` file lists all installable hooks. Here's an example structure for a hook definition:

```yaml
- id: hook-id # Unique identifier for the hook
  name: "A descriptive name for the hook" # User-friendly name
  entry: hooks/your_hook_script.py # Path to the hook script
  language: python # Specifies the language the script is written in
  types: [python] # File types the hook should run on
```

## ➕ Adding New Hooks

Interested in contributing a new hook? Follow these steps:

1.  **Create Your Hook Script:** Develop a Python script implementing your desired check or formatting logic. Place it in the `hooks/` directory. Ensure your script includes clear error messages and handles potential edge cases.
2.  **Declare the Hook:** Add a new entry for your hook in the `.pre-commit-hooks.yaml` file, following the structure shown above.
3.  **Test Locally:** Thoroughly test your hook in a local project environment using `pre-commit run --all-files` to confirm it works as expected before submitting.
4.  **Submit Your Contribution:** Commit your changes and create a Pull Request to the repository. Adhering to our [contribution guidelines](https://docs.ultralytics.com/help/contributing/) is appreciated.

## 🔧 Installing Hooks in Your Project

To use Ultralytics pre-commit hooks in your own project, add the following to your project's `.pre-commit-config.yaml` file:

```yaml
repos:
- repo: https://github.com/ultralytics/pre-commit-hooks
  rev: main # Pin to 'main' for the latest, or a specific git tag/commit SHA for stability
  hooks:
    - id: capitalize-comments # Example: Use the ID of the hook you want to include
    # Add other hook IDs as needed
```

After updating your configuration, run this command in your project's root directory to install the hooks:

```bash
pre-commit install
```

Now, the specified Ultralytics hooks will automatically run on your staged files each time you commit, helping maintain code quality effortlessly as part of your [Continuous Integration (CI)](https://www.ultralytics.com/glossary/continuous-integration-ci) process.

## 💡 Contribute

Ultralytics values community contributions! Your involvement helps us improve and grow. Please review our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for detailed information on how to participate. We also encourage you to share your feedback through our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A big thank you 🙏 to all our contributors! Check out some [tips on contributing to open-source projects](https://www.ultralytics.com/blog/tips-to-start-contributing-to-ultralytics-open-source-projects) on our blog.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 📄 License

Ultralytics offers two licensing options:

-   **AGPL-3.0 License:** An [OSI-approved](https://opensource.org/license/agpl-v3) open-source license ideal for students, researchers, and enthusiasts who value open collaboration. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for details.
-   **Enterprise License:** Designed for commercial use, this license allows seamless integration of Ultralytics software and AI models into commercial products and services, bypassing the open-source requirements of AGPL-3.0. For inquiries, visit [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📮 Contact

For bug reports or feature requests related to Ultralytics pre-commit hooks, please submit an issue on [GitHub Issues](https://github.com/ultralytics/pre-commit/issues). For general questions and discussions, join our vibrant community on [Discord](https://discord.com/invite/ultralytics)!

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
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
