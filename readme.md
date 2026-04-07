# 🚫 Dark Reader Blacklist

Automatically extract all domains from [Catppuccin userstyles](https://github.com/catppuccin/userstyles) and update your `disabledFor` list (e.g., for Dark Reader or any other tool that needs to disable itself on themed sites).

## 📦 What it does

- Fetches the official `import.json` from Catppuccin releases  
  👉 `https://github.com/catppuccin/userstyles/releases/download/all-userstyles-export/import.json`
- Parses every userstyle’s `@-moz-document` rules (`domain()`, `url-prefix()`, `regexp()`)
- Extracts all unique domain names (including subdomains and alternative instances)
- Writes them into a JSON file under the key `"disabledFor"`

## ❓ Why?

I like to use the Stylus extension alongside Dark Reader. Catppuccin offers a whole `import.json` file of userstyles and recommends disabling Dark Reader for these websites. There are at least 130 unique websites. Manually doing it would take forever, so here is a script to automatically fetch the `import.json` and extract the websites to a clean list.

## 🧰 Requirements

- Python 3.8+
- `requests` library

Install the dependency:

```bash
pip install requests