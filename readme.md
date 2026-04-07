# 🚫 Dark Reader Blacklist
 
Automatically extract all domains from [Catppuccin userstyles](https://github.com/catppuccin/userstyles) and update your `disabledFor` list (e.g., for Dark Reader or any other tool that needs to disable itself on themed sites).



## 📦 What it does

- Fetches the official `import.json` from Catppuccin releases  

  ➜ `https://github.com/catppuccin/userstyles/releases/download/all-userstyles-export/import.json`

- Parses every userstyle’s `@-moz-document` rules (`domain()`, `url-prefix()`, `regexp()`)

- Extracts all unique domain names (including subdomains and alternative instances)

- Writes them into a JSON file under the key `"disabledFor"`

  

## ❓ Why?  

I like to use the Stylus extension alongside Dark Reader. Catppuccin offers a whole `import.json` file of userstyles and recommends disabling Dark Reader for these websites. There are at least 130 *unique* websites. Manually doing it would take forever. So here is a script to automatically fetch the `import.json` and extract the websites to a clean list to be copied.


  

## 📄 How To Use

1. Open `disabled_sites.json` from within this repository or click here 🡓

- https://raw.githubusercontent.com/NakedTrashPanda/Dark-Reader-Blacklist/refs/heads/main/disabled_sites.json

1. Copy from the starting website or from `"disabledFor":` all the way to the last website

2. Open Dark Reader ➜ Settings ➜ Advanced ➜ Export Settings

3. Open `Dark-Reader-Settings.json` then find the line with `"disabledFor"` and paste the contents copied from step 2

- Make sure you are pasting it correctly and not overwriting any syntax. The indentation shouldn't matter.

5. Back in Dark Reader ➜ Settings ➜ Advanced ➜ go ahead and import `Dark-Reader-Settings.json`

6. Enjoy using both Stylus and Dark Reader without any conflicts!

  

## ❗ Requirements To Run Locally

- Python 3.8+

- `requests` library


Install the dependency:

  

```bash

pip install requests