"""
install.py - Cross-IDE installer for the Lecture Notes Compiler skill.
Supports Antigravity, Claude Code, Cursor, Windsurf, Cline, and Roo Code.

Usage:
    python install.py [--global] [--ide=antigravity|claude|cursor|windsurf|all]
"""

import os
import sys
import shutil
import argparse

def get_home_dir():
    return os.path.expanduser("~")

def copy_folder_contents(src, dest):
    os.makedirs(dest, exist_ok=True)
    if os.path.abspath(src) == os.path.abspath(dest):
        return
    for item in os.listdir(src):
        s_item = os.path.join(src, item)
        d_item = os.path.join(dest, item)
        if os.path.isdir(s_item):
            if os.path.exists(d_item):
                shutil.rmtree(d_item)
            shutil.copytree(s_item, d_item)
        else:
            if os.path.abspath(s_item) != os.path.abspath(d_item):
                shutil.copy2(s_item, d_item)

def install_for_antigravity(target_dir, is_global=False):
    src = os.path.dirname(os.path.abspath(__file__))
    locations = []
    if is_global:
        locations.append(os.path.join(get_home_dir(), ".gemini", "config", "skills", "lecture-notes-compiler"))
        locations.append(os.path.join(get_home_dir(), ".agents", "skills", "lecture-notes-compiler"))
    else:
        locations.append(os.path.join(target_dir, ".agents", "skills", "lecture-notes-compiler"))

    for dest in locations:
        if os.path.abspath(src) == os.path.abspath(dest):
            continue
        print(f"Installing for Antigravity at: {dest}")
        os.makedirs(dest, exist_ok=True)
        shutil.copy2(os.path.join(src, "SKILL.md"), os.path.join(dest, "SKILL.md"))
        for folder in ["resources", "scripts"]:
            s_folder = os.path.join(src, folder)
            d_folder = os.path.join(dest, folder)
            if os.path.exists(s_folder):
                copy_folder_contents(s_folder, d_folder)
        print("  Antigravity skill installed successfully.")

def install_for_claude(target_dir, is_global=False):
    src = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(get_home_dir(), ".claude", "skills", "lecture-notes-compiler") if is_global else os.path.join(target_dir, ".agents", "skills", "lecture-notes-compiler")
    if os.path.abspath(src) == os.path.abspath(dest):
        return
    print(f"Installing for Claude Code at: {dest}")
    os.makedirs(dest, exist_ok=True)
    shutil.copy2(os.path.join(src, "SKILL.md"), os.path.join(dest, "SKILL.md"))
    for folder in ["resources", "scripts"]:
        s_folder = os.path.join(src, folder)
        d_folder = os.path.join(dest, folder)
        if os.path.exists(s_folder):
            copy_folder_contents(s_folder, d_folder)
    print("  Claude Code skill installed successfully.")

def install_for_cursor(target_dir):
    dest_dir = os.path.join(target_dir, ".cursor", "rules")
    os.makedirs(dest_dir, exist_ok=True)
    src = os.path.dirname(os.path.abspath(__file__))
    rule_src = os.path.join(src, ".cursor", "rules", "lecture-notes-compiler.mdc")
    rule_dst = os.path.join(dest_dir, "lecture-notes-compiler.mdc")
    if os.path.exists(rule_src) and os.path.abspath(rule_src) != os.path.abspath(rule_dst):
        shutil.copy2(rule_src, rule_dst)
        print(f"Installing Cursor rule at: {rule_dst}")
        print("  Cursor rule installed successfully.")

def install_for_windsurf(target_dir):
    dest_dir = os.path.join(target_dir, ".windsurf", "rules")
    os.makedirs(dest_dir, exist_ok=True)
    src = os.path.dirname(os.path.abspath(__file__))
    rule_src = os.path.join(src, ".windsurf", "rules", "lecture-notes-compiler.md")
    rule_dst = os.path.join(dest_dir, "lecture-notes-compiler.md")
    if os.path.exists(rule_src) and os.path.abspath(rule_src) != os.path.abspath(rule_dst):
        shutil.copy2(rule_src, rule_dst)
        print(f"Installing Windsurf rule at: {rule_dst}")
        print("  Windsurf rule installed successfully.")

def main():
    parser = argparse.ArgumentParser(description="Install Lecture Notes Compiler skill across AI IDEs.")
    parser.add_argument("--global", dest="is_global", action="store_true", help="Install globally in user profile")
    parser.add_argument("--ide", choices=["antigravity", "claude", "cursor", "windsurf", "all"], default="all", help="Target AI IDE")
    parser.add_argument("--target-dir", default=os.getcwd(), help="Target workspace directory")
    args = parser.parse_args()

    target = os.path.abspath(args.target_dir)
    print(f"Target directory: {target}")

    if args.ide in ["antigravity", "all"]:
        install_for_antigravity(target, args.is_global)
    if args.ide in ["claude", "all"]:
        install_for_claude(target, args.is_global)
    if args.ide in ["cursor", "all"]:
        install_for_cursor(target)
    if args.ide in ["windsurf", "all"]:
        install_for_windsurf(target)

    print("\nInstallation complete.")

if __name__ == "__main__":
    main()
