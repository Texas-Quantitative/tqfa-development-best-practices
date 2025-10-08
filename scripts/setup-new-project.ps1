# TQFA Best Practices Setup Script for Windows
# PowerShell version of the project setup automation

param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectName,
    
    [string]$Path = ".",
    
    [switch]$NoDownload
)

function Write-Success { param($Message) Write-Host "✅ $Message" -ForegroundColor Green }
function Write-Info { param($Message) Write-Host "📁 $Message" -ForegroundColor Cyan }
function Write-Error { param($Message) Write-Host "❌ $Message" -ForegroundColor Red }

$ProjectPath = Join-Path $Path $ProjectName

if (Test-Path $ProjectPath) {
    Write-Error "Project directory '$ProjectPath' already exists"
    exit 1
}

Write-Host "🚀 Setting up new FastAPI project: $ProjectName" -ForegroundColor Yellow
Write-Info "Location: $ProjectPath"

try {
    # Create project directory structure
    $Structure = @{
        "app" = @("__init__.py", "main.py")
        "app/api" = @("__init__.py", "routes.py") 
        "app/schemas" = @("__init__.py")
        "app/services" = @("__init__.py")
        "app/models" = @("__init__.py")
        "docs" = @()
        "docs/best-practices" = @()
        "scripts" = @()
        "tests" = @("__init__.py", "test_main.py")
        ".github" = @()
        ".github/workflows" = @()
    }
    
    Write-Info "Creating project structure..."
    
    foreach ($dir in $Structure.Keys) {
        $DirPath = Join-Path $ProjectPath $dir
        New-Item -ItemType Directory -Path $DirPath -Force | Out-Null
        
        foreach ($file in $Structure[$dir]) {
            $FilePath = Join-Path $DirPath $file
            New-Item -ItemType File -Path $FilePath -Force | Out-Null
        }
    }
    
    Write-Success "Project structure created"
    
    # Download best practices if not skipped
    if (-not $NoDownload) {
        Write-Info "Downloading best practices documentation..."
        
        $BaseUrl = "https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/main"
        
        $FilesToDownload = @{
            "docs/best-practices/docker-deployment.md" = "$BaseUrl/docs/best-practices/docker-deployment.md"
            "docs/best-practices/scripts-and-tools.md" = "$BaseUrl/docs/best-practices/scripts-and-tools.md"
            "docs/best-practices/troubleshooting.md" = "$BaseUrl/docs/best-practices/troubleshooting.md"
            "docs/best-practices/README.md" = "$BaseUrl/docs/best-practices/README.md"
            "scripts/bump_version.py" = "$BaseUrl/scripts/bump_version.py"
            "scripts/check_deployment.py" = "$BaseUrl/scripts/check_deployment.py"
            "scripts/promote_healthy_revision.py" = "$BaseUrl/scripts/promote_healthy_revision.py"
            ".github/copilot-instructions.md" = "$BaseUrl/docs/templates/copilot-instructions-template.md"
        }
        
        foreach ($LocalPath in $FilesToDownload.Keys) {
            $Url = $FilesToDownload[$LocalPath]
            $FullPath = Join-Path $ProjectPath $LocalPath
            
            try {
                $Dir = Split-Path $FullPath -Parent
                if (-not (Test-Path $Dir)) {
                    New-Item -ItemType Directory -Path $Dir -Force | Out-Null
                }
                
                Invoke-WebRequest -Uri $Url -OutFile $FullPath
                Write-Host "  ✅ Downloaded $LocalPath" -ForegroundColor Gray
            }
            catch {
                Write-Host "  ❌ Failed to download $LocalPath`: $($_.Exception.Message)" -ForegroundColor Red
            }
        }
        
        Write-Success "Best practices documentation installed"
    }
    
    # Create requirements.txt
    Write-Info "Creating requirements.txt..."
    
    $RequirementsContent = @"
# Core FastAPI dependencies
fastapi[all]==0.104.1
uvicorn[standard]==0.24.0
gunicorn==21.2.0

# Data validation and serialization
pydantic==2.5.0
email-validator==2.1.0

# Azure dependencies (if using Azure)
azure-storage-blob==12.19.0
azure-identity==1.15.0

# Development dependencies
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2

# Optional: Database (uncomment if needed)
# sqlalchemy==2.0.23
# asyncpg==0.29.0

# Optional: Authentication (uncomment if needed)
# python-jose[cryptography]==3.3.0
# python-multipart==0.0.6
"@
    
    $RequirementsPath = Join-Path $ProjectPath "requirements.txt"
    Set-Content -Path $RequirementsPath -Value $RequirementsContent
    Write-Success "Created requirements.txt with recommended dependencies"
    
    # Create Dockerfile
    Write-Info "Creating production-ready Dockerfile..."
    
    $DockerfileContent = @'
# Production-ready FastAPI Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv .venv

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check (critical for Azure Container Apps)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Production command with proper workers and timeout
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "--timeout", "120"]
'@
    
    $DockerfilePath = Join-Path $ProjectPath "Dockerfile"
    Set-Content -Path $DockerfilePath -Value $DockerfileContent
    Write-Success "Created production-ready Dockerfile"
    
    # Create main FastAPI app
    Write-Info "Creating main FastAPI application..."
    
    $MainContent = @"
"""
$ProjectName - FastAPI Application

Production-ready FastAPI application with health checks and proper error handling.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Import your route modules here
# from app.api import routes

# Application metadata
app = FastAPI(
    title="$ProjectName API",
    description="Production-ready FastAPI application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware (configure for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - shows API status and version."""
    return {
        "message": "$ProjectName API",
        "version": "1.0.0",
        "status": "healthy"
    }


@app.get("/health/")
async def health_check():
    """Health check endpoint for load balancers and container orchestrators."""
    return {
        "status": "healthy",
        "service": "$ProjectName",
        "version": "1.0.0"
    }


# Include your API routes here
# app.include_router(routes.router, prefix="/api/v1", tags=["api"])


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors."""
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "detail": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    
    # Development server configuration
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
"@
    
    $MainPath = Join-Path $ProjectPath "app/main.py"
    Set-Content -Path $MainPath -Value $MainContent
    Write-Success "Created main FastAPI application"
    
    # Customize copilot instructions
    $CopilotPath = Join-Path $ProjectPath ".github/copilot-instructions.md"
    if (Test-Path $CopilotPath) {
        Write-Info "Customizing Copilot instructions..."
        $Content = Get-Content $CopilotPath -Raw
        $Content = $Content -replace "tqfaAPI", $ProjectName
        $Content = $Content -replace "TQFA API", "$ProjectName API"
        Set-Content -Path $CopilotPath -Value $Content
        Write-Success "Project customization complete"
    }
    
    Write-Host "`n🎉 Successfully created project '$ProjectName'!" -ForegroundColor Green
    Write-Host "`n📋 Next steps:" -ForegroundColor Yellow
    Write-Host "   cd $ProjectName"
    Write-Host "   python -m venv .venv"
    Write-Host "   .venv\Scripts\activate"
    Write-Host "   pip install -r requirements.txt"
    Write-Host "   python -m app.main"
    Write-Host "`n📚 Documentation:" -ForegroundColor Yellow
    Write-Host "   - Best practices: $ProjectPath\docs\best-practices\"
    Write-Host "   - Deployment guide: $ProjectPath\docs\best-practices\docker-deployment.md"
    Write-Host "   - Troubleshooting: $ProjectPath\docs\best-practices\troubleshooting.md"
    
}
catch {
    Write-Error "Error setting up project: $($_.Exception.Message)"
    if (Test-Path $ProjectPath) {
        Remove-Item $ProjectPath -Recurse -Force
    }
    exit 1
}