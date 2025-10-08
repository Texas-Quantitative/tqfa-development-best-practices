#!/usr/bin/env python3
"""
Version Bump Script
Automatically increments the patch version number across all files
"""

import re
from pathlib import Path

def bump_version():
    """Bump the patch version in all relevant files."""
    
    files_to_update = [
        "app/main.py",
        "pyproject.toml",
        "setup.py"
    ]
    
    version_pattern = r'version\s*=\s*["\'](\d+)\.(\d+)\.(\d+)["\']'
    title_version_pattern = r'version="(\d+)\.(\d+)\.(\d+)"'
    
    current_version = None
    new_version = None
    
    print("🔢 Version Bump Utility")
    print("=" * 30)
    
    # First, find current version from main.py
    main_py = Path("app/main.py")
    if main_py.exists():
        content = main_py.read_text(encoding='utf-8')
        match = re.search(title_version_pattern, content)
        if match:
            major, minor, patch = map(int, match.groups())
            current_version = f"{major}.{minor}.{patch}"
            new_patch = patch + 1
            new_version = f"{major}.{minor}.{new_patch}"
            print(f"📋 Current version: {current_version}")
            print(f"🚀 New version: {new_version}")
        else:
            print("❌ Could not find version in app/main.py")
            return False
    
    if not new_version:
        print("❌ Failed to determine version")
        return False
    
    # Update all files
    updated_files = []
    
    for file_path in files_to_update:
        file_obj = Path(file_path)
        if not file_obj.exists():
            print(f"⚠️ File not found: {file_path}")
            continue
        
        content = file_obj.read_text(encoding='utf-8')
        
        # Update version= patterns
        updated_content, count1 = re.subn(
            version_pattern,
            f'version="{new_version}"',
            content
        )
        
        # Update title version patterns
        updated_content, count2 = re.subn(
            title_version_pattern,
            f'version="{new_version}"',
            updated_content
        )
        
        # Update return statement version patterns
        return_pattern = r'"version":\s*"(\d+)\.(\d+)\.(\d+)"'
        updated_content, count3 = re.subn(
            return_pattern,
            f'"version": "{new_version}"',
            updated_content
        )
        
        total_changes = count1 + count2 + count3
        
        if total_changes > 0:
            file_obj.write_text(updated_content, encoding='utf-8')
            updated_files.append(file_path)
            print(f"✅ Updated {file_path} ({total_changes} changes)")
        else:
            print(f"📋 No changes needed in {file_path}")
    
    if updated_files:
        print(f"\n🎯 Successfully bumped version from {current_version} to {new_version}")
        print(f"📁 Updated files: {', '.join(updated_files)}")
        return True, new_version
    else:
        print("❌ No files were updated")
        return False, None

if __name__ == "__main__":
    success, version = bump_version()
    if success:
        print(f"\n💡 Next steps:")
        print(f"   git add .")
        print(f'   git commit -m "Version bump to {version}"')
        print(f"   git push")
    else:
        print("\n❌ Version bump failed")