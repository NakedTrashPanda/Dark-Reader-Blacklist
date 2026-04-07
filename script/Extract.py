#!/usr/bin/env python3
"""
Extract domains from Catppuccin userstyles import.json and export them to a clean list ready for Dark Readers blacklist.
Usage: python extract_domains.py [output_file.json]
"""

import json
import re
import sys
import requests
from urllib.parse import urlparse

IMPORT_JSON_URL = "https://github.com/catppuccin/userstyles/releases/download/all-userstyles-export/import.json"
DEFAULT_OUTPUT = "disabled_sites.json"

def fetch_import_json():
    resp = requests.get(IMPORT_JSON_URL)
    resp.raise_for_status()
    return resp.json()

def extract_domains_from_source(source_code):
    domains = set()
    # domain("example.com")
    domain_pattern = re.compile(r'domain\("([^"]+)"\)')
    for match in domain_pattern.finditer(source_code):
        domains.add(match.group(1))
    
    # url-prefix("https://example.com/")
    url_prefix_pattern = re.compile(r'url-prefix\("([^"]+)"\)')
    for match in url_prefix_pattern.finditer(source_code):
        url = match.group(1)
        parsed = urlparse(url)
        if parsed.netloc:
            domains.add(parsed.netloc)
    
    # regexp("...") – simple heuristic
    regexp_pattern = re.compile(r'regexp\("([^"]+)"\)')
    for match in regexp_pattern.finditer(source_code):
        regex = match.group(1)
        host_match = re.search(r'([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)', regex)
        if host_match:
            domains.add(host_match.group(1))
        else:
            literal = re.search(r'(?<!\\)(?:\\\.)*([a-zA-Z0-9-]+)\\\.', regex)
            if literal:
                domains.add(literal.group(1) + ".com")
    return domains

def main():
    output_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    
    try:
        print(f"Fetching {IMPORT_JSON_URL}...")
        data = fetch_import_json()
        print("Parsing userstyles...")
        all_domains = set()
        for entry in data:
            if "sourceCode" in entry:
                domains = extract_domains_from_source(entry["sourceCode"])
                all_domains.update(domains)
        
        sorted_domains = sorted(all_domains)
        output = {"disabledFor": sorted_domains}
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)   # <-- clean indentation
        print(f"Saved {len(sorted_domains)} unique domains to {output_file}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()