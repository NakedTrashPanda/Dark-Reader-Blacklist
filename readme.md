# 🚫 Dark Reader Blacklist

Automatically extract all domains from [Catppuccin's Stylus userstyles](https://github.com/catppuccin/userstyles) so you can update your disabledFor list within Dark Reader.

## 📦 What it does

- Fetches the official import.json from Catppuccin releases
  -> https://github.com/catppuccin/userstyles/releases/download/all-userstyles-export/import.json
- Parses every userstyle's @-moz-document rules (domain(), url-prefix(), regexp())
- Extracts all unique domain names (including subdomains and alternative instances)
- Writes them into a JSON file under the key "disabledFor"

## ❓ Why?

I like to use the Stylus extension alongside Dark Reader. Catppuccin offers a whole import.json file of userstyles and recommends disabling Dark Reader for these websites. There are at least 130 unique websites. Manually doing it would take forever. So here is a script to automatically fetch the import.json and extract the websites to a clean list to be copied.

## 📄 How To Use

1. Open `disabled_sites.json` from within this repository or click here
   https://raw.githubusercontent.com/NakedTrashPanda/Dark-Reader-Blacklist/refs/heads/main/disabled_sites.json

2. Copy from the starting website or from `"disabledFor":` all the way to the last website

3. Open Dark Reader -> Settings -> Advanced -> Export Settings

4. Open `Dark-Reader-Settings.json` then find the line with `"disabledFor"` and paste the contents copied from step 2
   - Make sure you are pasting it correctly and not overwriting any syntax. The indentation shouldn't matter.

5. Back in Dark Reader -> Settings -> Advanced -> import Dark-Reader-Settings.json

6. Enjoy using both Stylus and Dark Reader without any conflicts!

## 🛠️ Manual Installation & Local Execution

If you prefer to run the script yourself (instead of using the pre-generated disabled_sites.json), follow these steps:

1. Clone the repository
   `git clone https://github.com/NakedTrashPanda/Dark-Reader-Blacklist.git`
   `cd Dark-Reader-Blacklist`

2. Install the required dependency
   `pip install requests`

3. Run the extraction script
   `python script/Extract.py`

   The script will download the latest Catppuccin import.json, parse all domains, and save the result to `disabled_sites.json` in the repository root folder.

4. Follow the steps in the "[[#📄 How To Use]]" section above, using your freshly generated disabled_sites.json instead of the hosted one.