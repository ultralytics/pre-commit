<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# Ultralytics Pre-commit Hooks 🤖

Welcome to the official repository housing Ultralytics' pre-commit hooks, tailor-made to promote high coding standards and enable streamlined codebase quality management. 

## ✨ About This Repository

Within this repository, you'll find a curated selection of pre-commit hooks, each purpose-built by our team at [Ultralytics](https://ultralytics.com) to ensure a meticulous approach to coding practices.

### Repository Blueprint

The blueprint of the repository encompasses:

- A `hooks` directory featuring the individual Python scripts embodying the hooks.
- A `.pre-commit-hooks.yaml` located at the root level, which outlines the hooks accessible for installation.

#### Hooks in the `hooks` Directory

Each individual hook is materialized through a Python script residing in the `hooks` directory. For instance, the `capitalize_comments.py` script appoints itself the role of capitalizing the initial letter of standalone inline comments.

#### Manifesting Hooks in `.pre-commit-hooks.yaml`

Every installable hook receives its declaration within the `.pre-commit-hooks.yaml` file. A hook's narrative here looks akin to:

```yaml
- id: hook-id
  name: 'Descriptive Hook Name'
  entry: hooks/hook_script.py
  language: python
  types: [python]
```

Dissected, the keys represent:
- `id`: A distinct identifier for the hook.
- `name`: A brief, yet descriptive, title shedding light on the hook's essence.
- `entry`: The pathway to the script encasing the hook's logic.

## 🛠 Adding New Pre-Commit Hooks

To contribute a brand-new hook:
1. **Craft the Hook Script**: Pen down a Python script with the hook's functionality and integrate it within the `hooks` directory, ensuring robust error checks and decipherable output.
2. **Unveil the Hook**: Introduce a fresh stanza in the `.pre-commit-hooks.yaml` adhering to the aforementioned schema.
3. **Local Testing**: Validate the hook on a local scale within a project to guarantee its intended conduct.
4. **Commit & Promulgate**: Post-validation, commit these modifications and push them up to this repository.

## 📥 How to Install Hooks into Your Project

You can latch these hooks onto your primary project by referencing this remote hook repository in your project's `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/ultralytics/pre-commit
  rev: main  # Substitutable with a specific git tag/revision
  hooks:
    - id: hook-id
```

To activate the hooks, execute this within your project's sanctuary:

```bash
pre-commit install
```

Following this, any commit you contrive will automatically enlist the pre-commit hooks delineated here as part of your version control rituals.

## 🚀 Contribute and Collaborate

Your insights are invaluable! Our open-source endeavors conversely thrive with community contributions. To embark, peruse our [Contributing Guide](https://docs.ultralytics.com/help/contributing) and don't hesitate to impart your feedback via our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 to every last one of our contributors!

<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
  <img src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors" width="100%">
</a>

## 🔒 License

At Ultralytics, you are presented with a duo of license alternatives fitting a spectrum of scenarios:

- **AGPL-3.0 License**: This OSI-celebrated open-source license is the perfect match for students, hobbyists, and open collaboration aficionados, promoting a culture of knowledge interchange. Peek into the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for further insight.
- **Enterprise License**: Petite to grande businesses shall find this license particularly apt for intertwining Ultralytics software and AI models into proprietary goods and services sans the open-source requisites tied to AGPL-3.0. When commercial routes beckon, converse through [Ultralytics Licensing](https://ultralytics.com/license).

## 📬 Contact

We are all ears for bug reports or feature solicitations through [GitHub Issues](https://github.com/ultralytics/pre-commit/issues). Furthermore, hop onto our [Discord](https://ultralytics.com/discord) for engaging dialogue and community support!

<div align="center">
  <a href="https://github.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics on GitHub"/>
  </a>
  <a href="https://www.linkedin.com/company/ultralytics/">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics on LinkedIn"/>
  </a>
  <a href="https://twitter.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics on Twitter"/>
  </a>
  <a href="https://youtube.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics on YouTube"/>
  </a>
  <a href="https://www.tiktok.com/@ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics on TikTok"/>
  </a>
  <a href="https://www.instagram.com/ultralytics/">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics on Instagram"/>
  </a>
  <a href="https://ultralytics.com/discord">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Join Ultralytics Discord"/>
  </a>
</div>
