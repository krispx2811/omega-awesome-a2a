# Contributing to Omega Awesome A2A

Thank you for your interest in contributing to Omega Awesome A2A! Your contributions play a significant role in building a comprehensive repository of resources in the multimodal AI domain. To make the process smooth and efficient for everyone, we’ve outlined the guidelines for contributing below.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Branching Strategy](#branching-strategy)
3. [Making Changes](#making-changes)
4. [Commit Messages](#commit-messages)
5. [Pull Request (PR) Guidelines](#pull-request-pr-guidelines)
6. [Code Review Process](#code-review-process)
7. [Code of Conduct](#code-of-conduct)

---

## Getting Started

Follow these steps to start contributing:

1. **Fork the Repository**
   - Click the **Fork** button in the top-right corner of this repository to create a copy in your GitHub account.

2. **Clone Your Fork**
   - Clone the forked repository to your local machine using:
     ```bash
     git clone https://github.com/<your-username>/omega-awesome-a2a.git
     ```
     Replace `<your-username>` with your GitHub username.

3. **Set Upstream Remote**
   - Link your fork to the original repository to stay updated:
     ```bash
     git remote add upstream https://github.com/krispx2811/omega-awesome-a2a.git
     ```

4. **Sync Your Fork**
   - Before starting any work, ensure your fork is up-to-date with the latest changes:
     ```bash
     git pull upstream main
     ```

5. **Install Dependencies**
   - If the repository requires specific tools or dependencies, install them by following instructions in the `README.md`.

---

## Branching Strategy

To ensure your changes don’t conflict with others, use branches effectively:

1. **Create a New Branch**
   - Use a descriptive name for your branch:
     ```bash
     git checkout -b feature/your-feature-name
     ```
     Replace `your-feature-name` with a short, clear description (e.g., `add-text-to-video-resource`).

2. **Branch Naming Conventions**
   - `feature/`: For new features or additions.
   - `bugfix/`: For fixing bugs.
   - `docs/`: For documentation updates.
   - `refactor/`: For code restructuring or optimization.

3. **Stay Focused**
   - Each branch should focus on one feature or fix. Avoid bundling multiple changes into a single branch.

---

## Making Changes

1. **Understand the Project**
   - Review the `README.md` and existing files to understand the project structure and purpose.

2. **Write Clean Code**
   - Follow consistent coding styles. Use descriptive variable names and add comments where necessary.
   - If the repository uses linters or formatters, ensure your code passes them.

3. **Add Tests (If Applicable)**
   - Write unit or integration tests for new features to ensure they work as intended.
   - Update existing tests if your changes affect them.

4. **Update Documentation**
   - If your changes affect the documentation, update files like `README.md` or add new markdown files.

5. **Test Your Changes**
   - Run your changes locally to confirm they work as expected.

---

## Commit Messages

Well-written commit messages make it easier to understand the history of a project. Follow this format:

1. **Structure**
   - Use this format for your commit messages:
     ```
     [Type]: Short description

     Detailed explanation (if necessary).
     ```

2. **Types**
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation update
   - `style`: Code style changes (e.g., formatting)
   - `refactor`: Code refactoring
   - `test`: Adding or updating tests
   - `chore`: Maintenance tasks

3. **Examples**
   - `feat: Add text-to-video resource`
   - `fix: Resolve broken link in README`
   - `docs: Update contributing guidelines`

---

## Pull Request (PR) Guidelines

When you’re ready to submit your changes, create a pull request with the following structure:

1. **PR Title**
   - Use a clear and concise title summarizing the changes.
     Example: `Add text-to-video AI resources`

2. **PR Description**
   - Provide a detailed explanation of your changes. Use this template:
     ```markdown
     ### Summary
     Briefly explain the purpose of the PR and the changes introduced.

     ### Changes
     - [List each change made in detail]
     - [Include file names or directories updated]

     ### Testing
     Describe how you tested the changes:
     - [e.g., Unit tests added]
     - [e.g., Manual testing steps]

     ### Related Issues
     Link to relevant issues, e.g., `Closes #123`.
     ```

3. **Ensure Your PR Meets These Requirements**
   - The branch has been rebased onto `main` if necessary.
   - Code follows the project's coding standards.
   - Documentation is updated where applicable.
   - Tests are added or updated, and all tests pass.

4. **Submit the PR**
   - Push your branch to your fork:
     ```bash
     git push origin feature/your-feature-name
     ```
   - Open a pull request on GitHub from your branch to the `main` branch of the original repository.

5. **Label Your PR**
   - Add appropriate labels like `feature`, `bugfix`, or `documentation`.

---

## Code Review Process

1. **Review Timeline**
   - PRs are reviewed within 3-5 business days. Larger changes may take longer.

2. **Address Feedback**
   - If reviewers request changes, update your branch accordingly and push the changes:
     ```bash
     git add .
     git commit -m "fix: Address review feedback"
     git push
     ```

3. **Collaborate**
   - Respond to comments and collaborate with reviewers to finalize your changes.

---

## Code of Conduct

By contributing, you agree to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful and constructive in all interactions.

---

## Thank You!

Thank you for taking the time to contribute to Omega Awesome A2A! Your efforts make this project a valuable resource for the multimodal AI community.

Feel free to open an issue if you have questions or suggestions. Happy coding!
