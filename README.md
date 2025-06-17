# Python Behave Playwright Demo

This is a Behave Playwright demo designed to test against the [Sauce Demo](https://www.saucedemo.com/) site. The framework allows you to automate and validate various elements and functionalities of the site.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Behave Tests](#running-the-behave-tests)
  - [Running the Quality Tools](#running-the-quality-tools)
  - [Using Playwright Codegen](#using-playwright-codegen)
- [Available Elements to Test](#available-elements-to-test)

## Getting Started

Follow these steps to set up the project and start using the framework:

### Prerequisites

Ensure you have the following installed:
- **Python**
    - A current version of Python

### Installation

1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```sh
   git clone <repo-url>
   cd <repo-name>
   ```

2. **Create a Virtual Environment**  
   Create and activate a virtual environment to isolate project dependencies:
   - On Windows:
     ```sh
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Upgrade Pip and Install Dependencies**  
   Install the project dependencies using `pip`:
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**  
   After installing the dependencies, install the required Playwright browsers:
   ```sh
   playwright install
   ```

You are now ready to use the Python Behave Playwright Demo!

## Usage

### Running the Behave Tests
To execute the Behave tests, use the following command:
```sh
behave
```
This will run all the feature files in the `features` directory.

To execute work in progress tests, add the `@wip` tag to the scenarios or features and use the following command:
```sh
behave --wip
```
The `@wip` tag is used to mark scenarios or features that are a work in progress. These tests can be run separately to focus on incomplete or experimental functionality.

You can also run specific tests by specifying the feature file or scenario tags:
- Run a specific feature file:
  ```sh
  behave features/<feature-file>.feature
  ```
- Run tests with specific tags:
  ```sh
  behave --tags=@<tag>
  ```

### Running the Quality Tools
To ensure code quality, you can run tools like `ruff`, `ruff formatter`, `mypy`, and `reformat-gherkin`:

- **Check code style with `ruff`**:
  ```sh
  ruff check
  ```

- **Check code formatting with `ruff formatter`**:
  ```sh
  ruff format --check --diff
  ```

- **Check type annotations with `mypy`**:
  To verify type correctness in your code, run:
  ```sh
  mypy .
  ```
  This will check all Python files in the current directory and its subdirectories for type errors.

- **Reformat Gherkin feature files with `reformat-gherkin`**:
  To ensure consistent formatting of your Gherkin feature files, use the following command:
  ```sh
  reformat-gherkin features/
  ```
  This will reformat all `.feature` files in the `features` directory to follow a consistent style.

### Using Playwright Codegen
You can use Playwright's `codegen` tool to generate scripts or debug interactions with the browser. For example:
```sh
playwright codegen https://www.saucedemo.com/ --save-storage auth.json --load-storage auth.json
```
This will open a browser window and allow you to record actions. The storage state will be saved to `auth.json` for reuse over multiple codegen sessions.

## Available Elements to Test
The following elements are available for testing:
- **Login Page**:
  - Username and password fields
  - Login button
  - Error messages for invalid credentials
- **Product Page**:
  - Product listings
  - Add to and remove from cart buttons
  - Sorting functionality
- **Cart Page**:
  - Cart items
  - Remove item buttons
  - Checkout button
- **Checkout Page**:
  - Form fields for user information
  - Overview of selected items
  - Finish button