<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🛠 Ultralytics Pre-commit Hooks

This repository contains pre-commit hooks developed by [Ultralytics](https://ultralytics.com) for ensuring code quality and standards in our software development practices. By leveraging these hooks, developers can automate the process of code validation, thus maintaining a high level of code hygiene.

## 🗂 Repository Structure

The repository is thoughtfully structured to facilitate easy navigation and understanding:

- A `hooks` directory comprising all the individual Python scripts, each serving as a distinct hook for specific checks or code quality assurances.
- The `.pre-commit-hooks.yaml` file located at the root, which specifies the available hooks for easy integration into your projects.

### Hook Scripts in `hooks` Directory 📂

Each script housed within the `hooks` directory is a self-contained Python program designed to carry out a particular pre-commit check. For example:

- `capitalize_comments.py`: This script ensures that the first letter of standalone inline comments begins with a capital letter, fostering readability and a professional codebase demeanor.

### Defining Hooks in `.pre-commit-hooks.yaml` 📘

Hooks available for installation are declared within the `.pre-commit-hooks.yaml` file. An example definition would resemble:

```yaml
- id: hook-id
  name: 'A Name Describing What the Hook Does'
  entry: hooks/name_of_your_hook_script.py
  language: python
  types: [python]
```

Where the elements are as follows:
+ `hook-id` represents a unique identifier for the hook you are configuring.
+ `A Name Describing What the Hook Does`: A brief, intuitive name that indicates the functionality of the hook.
+ `name_of_your_hook_script.py` is the filename for the Python script that resides in the `hooks` directory and codifies the logic for the hook.

## ➕ Adding Additional Hooks

If you're interested in contributing a fresh hook, here's how you can add one:

1. **Craft Your Hook Script**: Write a Python script that encapsulates the functionality of your new hook. This script should be placed within the `hooks` directory. For maintainability and ease-of-understanding, ensure your script contains appropriate error handling and outputs useful messages.
2. **Declare Your New Hook**: Extend the `.pre-commit-hooks.yaml` with a new block that follows the definition pattern showcased earlier.
3. **Local Testing**: Before integrating your hook into the repository, ensure that you have tested it in a local project setting to affirm its operational behavior.
4. **Sync to Repository**: After satisfactory local validation, commit your work to the repository and initiate a push to share your hook with the community.

## 🔧 Installing Hooks in Your Project

To harness the power of Ultralytics pre-commit hooks within your project, add their specifications into your `.pre-commit-config.yaml` like so:

```yaml
- repo: https://github.com/ultralytics/pre-commit-hooks
  rev: main  # You might prefer pinning this to a specific git tag or commit SHA.
  hooks:
    - id: hook-id
```

Execute this command within your project's directory to set up the pre-commit framework:

```bash
pre-commit install
```
With this action, the identified pre-commit hooks from Ultralytics will now be a part of your workflow, automatically running during the commit phase.

## 💡 Contribute

Ultralytics thrives on community collaboration; we immensely value your involvement! We urge you to peruse our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for detailed insights on how you can participate. Don't forget to share your feedback with us by contributing to our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 goes out to everyone who has already contributed!

<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

## 📄 License

Ultralytics presents two distinct licensing paths to accommodate a variety of scenarios:

- **AGPL-3.0 License**: This official [OSI-approved](https://opensource.org/licenses/) open-source license is perfectly aligned with the goals of students, enthusiasts, and researchers who believe in the virtues of open collaboration and shared wisdom. Details are available in the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) document.
- **Enterprise License**: Tailored for commercial deployment, this license authorizes the unfettered integration of Ultralytics software and AI models within commercial goods and services, without the copyleft stipulations of AGPL-3.0. Should your use case demand an enterprise solution, direct your inquiries to [Ultralytics Licensing](https://ultralytics.com/license).

## 📮 Contact

For bugs or feature suggestions pertaining to Ultralytics, please lodge an issue via [GitHub Issues](https://github.com/ultralytics/pre-commit/issues). You're also invited to participate in our [Discord](https://ultralytics.com/discord) community to engage in discussions and seek advice!

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
