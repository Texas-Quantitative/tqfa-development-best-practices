# Setup Best Practices Access Script
# Creates standardized access to TQFA best practices across all projects

param(
    [string]$TargetPath = "$env:USERPROFILE\.tqfa\best-practices",
    [switch]$Force
)

# Standard location for best practices
$BEST_PRACTICES_PATH = $TargetPath
$REPO_URL = "https://github.com/Texas-Quantitative/tqfa-development-best-practices.git"

Write-Host "🚀 Setting up TQFA Best Practices Access" -ForegroundColor Green
Write-Host "Target Path: $BEST_PRACTICES_PATH" -ForegroundColor Yellow

# Create directory structure
$parentDir = Split-Path $BEST_PRACTICES_PATH -Parent
if (!(Test-Path $parentDir)) {
    New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    Write-Host "✅ Created directory: $parentDir" -ForegroundColor Green
}

# Check if already exists
if (Test-Path $BEST_PRACTICES_PATH) {
    if ($Force) {
        Write-Host "🔄 Force flag set, removing existing..." -ForegroundColor Yellow
        Remove-Item $BEST_PRACTICES_PATH -Recurse -Force
    } else {
        Write-Host "📁 Best practices already exist at: $BEST_PRACTICES_PATH" -ForegroundColor Yellow
        Write-Host "🔄 Updating existing repository..." -ForegroundColor Yellow
        
        Push-Location $BEST_PRACTICES_PATH
        try {
            # Check git status
            $gitStatus = git status --porcelain 2>$null
            if ($gitStatus) {
                Write-Host "⚠️  Warning: Local changes detected:" -ForegroundColor Red
                git status --short
                Write-Host "❌ Cannot auto-update with local changes. Please commit or stash first." -ForegroundColor Red
                return 1
            }
            
            # Pull latest changes
            Write-Host "📥 Pulling latest changes..." -ForegroundColor Yellow
            git pull origin master
            Write-Host "✅ Best practices updated successfully!" -ForegroundColor Green
            
        } finally {
            Pop-Location
        }
        return 0
    }
}

# Clone fresh copy
Write-Host "📥 Cloning best practices repository..." -ForegroundColor Yellow
git clone $REPO_URL $BEST_PRACTICES_PATH

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Best practices cloned successfully!" -ForegroundColor Green
    Write-Host "📍 Location: $BEST_PRACTICES_PATH" -ForegroundColor Cyan
    
    # Add to environment for this session
    $env:TQFA_BEST_PRACTICES_PATH = $BEST_PRACTICES_PATH
    
    Write-Host ""
    Write-Host "🔧 Next Steps:" -ForegroundColor Yellow
    Write-Host "1. Add to your project's copilot-instructions.md:" -ForegroundColor White
    Write-Host "   📚 **BEST PRACTICES**: `$env:USERPROFILE\.tqfa\best-practices\README.md`" -ForegroundColor Cyan
    Write-Host "2. Use sync-best-practices.ps1 to keep updated" -ForegroundColor White
    Write-Host "3. Reference specific guides: $BEST_PRACTICES_PATH\docs\best-practices\" -ForegroundColor White
    
} else {
    Write-Host "❌ Failed to clone repository" -ForegroundColor Red
    return 1
}