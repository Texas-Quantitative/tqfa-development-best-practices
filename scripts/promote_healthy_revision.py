#!/usr/bin/env python3
"""
Azure Container Apps Traffic Promotion Script

This script fixes Azure's idiotic default behavior of keeping healthy 
revisions at 0% traffic. It automatically promotes the latest healthy 
revision to receive 100% traffic.

Why this script exists:
- Azure Container Apps doesn't automatically route traffic to healthy revisions
- Microsoft's "safety" feature creates deployment confusion
- Manual traffic promotion is required for every deployment
- This is INSANE default behavior that wastes hours of debugging
"""

import subprocess
import json
import sys
from datetime import datetime

def run_command(command):
    """Run Azure CLI command and return JSON result."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {command}")
        print(f"Error: {e.stderr}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON response from: {command}")
        print(f"Raw output: {e}")
        return None

def get_revisions(app_name, resource_group):
    """Get all revisions for the container app."""
    command = f"az containerapp revision list --name {app_name} --resource-group {resource_group}"
    return run_command(command)

def promote_latest_healthy_revision(app_name, resource_group):
    """Find the latest healthy revision and promote it to 100% traffic."""
    print(f"🔍 Checking revisions for {app_name}...")
    
    revisions = get_revisions(app_name, resource_group)
    if not revisions:
        print("❌ Failed to get revisions")
        return False
    
    # Find healthy revisions sorted by creation time (latest first)
    healthy_revisions = [
        r for r in revisions 
        if r.get('properties', {}).get('healthState') == 'Healthy'
    ]
    
    if not healthy_revisions:
        print("❌ No healthy revisions found!")
        return False
    
    # Sort by creation time (latest first)  
    healthy_revisions.sort(
        key=lambda x: x.get('properties', {}).get('createdTime', ''), 
        reverse=True
    )
    
    latest_healthy = healthy_revisions[0]
    revision_name = latest_healthy['name']
    current_traffic = latest_healthy.get('properties', {}).get('trafficWeight', 0)
    
    print(f"📊 Latest healthy revision: {revision_name}")
    print(f"📊 Current traffic weight: {current_traffic}%")
    
    if current_traffic == 100:
        print("✅ Latest healthy revision already has 100% traffic - no action needed")
        return True
    
    print(f"🚀 Promoting {revision_name} to 100% traffic...")
    
    # Set traffic to 100% for the latest healthy revision
    command = f"az containerapp ingress traffic set --name {app_name} --resource-group {resource_group} --revision-weight {revision_name}=100"
    
    result = run_command(command)
    if result:
        print(f"✅ Successfully promoted {revision_name} to 100% traffic!")
        print(f"🎉 Deployment complete - users are now getting the latest version")
        return True
    else:
        print(f"❌ Failed to promote {revision_name}")
        return False

def main():
    """Main function."""
    app_name = "tqfaapi-uat"
    resource_group = "tqfa-uat-rg"
    
    print("🚀 Azure Container Apps Traffic Promotion Tool")
    print("=" * 50)
    print(f"App: {app_name}")
    print(f"Resource Group: {resource_group}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    success = promote_latest_healthy_revision(app_name, resource_group)
    
    if success:
        print("\n🎉 Traffic promotion completed successfully!")
        print("💡 Tip: Add this script to your deployment pipeline to automate traffic promotion")
        sys.exit(0)
    else:
        print("\n❌ Traffic promotion failed")
        print("🔧 Check the Azure portal or run 'az containerapp revision list' manually")
        sys.exit(1)

if __name__ == "__main__":
    main()