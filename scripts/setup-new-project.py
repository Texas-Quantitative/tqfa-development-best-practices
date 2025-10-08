#!/usr/bin/env python3
"""
TQFA Best Practices Installation Script

Automatically sets up a new project with proven best practices.
Saves hours of manual setup and ensures nothing is missed.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
import subprocess
import urllib.request


def create_project_structure(project_name, project_path):
    """Create the recommended FastAPI project structure."""
    
    structure = {
        'app': ['__init__.py', 'main.py'],
        'app/api': ['__init__.py', 'routes.py'],
        'app/schemas': ['__init__.py'],
        'app/services': ['__init__.py'],
        'app/models': ['__init__.py'],
        'docs': [],
        'docs/best-practices': [],
        'scripts': [],
        'tests': ['__init__.py', 'test_main.py'],
        '.github': [],
        '.github/workflows': []
    }
    
    print(f"📁 Creating project structure for {project_name}...")
    
    for directory, files in structure.items():
        dir_path = project_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        
        for file in files:
            file_path = dir_path / file
            if not file_path.exists():
                file_path.touch()
                
    print("✅ Project structure created")


def download_best_practices(project_path):
    """Download the latest best practices documentation."""
    
    base_url = "https://raw.githubusercontent.com/Texas-Quantitative/tqfa-development-best-practices/main"
    
    files_to_download = {
        'docs/best-practices/docker-deployment.md': f'{base_url}/docs/best-practices/docker-deployment.md',
        'docs/best-practices/scripts-and-tools.md': f'{base_url}/docs/best-practices/scripts-and-tools.md',
        'docs/best-practices/troubleshooting.md': f'{base_url}/docs/best-practices/troubleshooting.md',
        'docs/best-practices/README.md': f'{base_url}/docs/best-practices/README.md',
        'scripts/bump_version.py': f'{base_url}/scripts/bump_version.py',
        'scripts/check_deployment.py': f'{base_url}/scripts/check_deployment.py',
        'scripts/promote_healthy_revision.py': f'{base_url}/scripts/promote_healthy_revision.py',
        '.github/copilot-instructions.md': f'{base_url}/docs/templates/copilot-instructions-template.md'
    }
    
    print("📥 Downloading best practices documentation...")
    
    for local_path, url in files_to_download.items():
        file_path = project_path / local_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            urllib.request.urlretrieve(url, file_path)
            print(f"  ✅ Downloaded {local_path}")
        except Exception as e:
            print(f"  ❌ Failed to download {local_path}: {e}")
    
    print("✅ Best practices documentation installed")


def create_requirements_file(project_path):
    """Create a requirements.txt with recommended dependencies."""
    
    requirements = """# Core FastAPI dependencies
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
"""
    
    requirements_path = project_path / "requirements.txt"
    requirements_path.write_text(requirements)
    print("✅ Created requirements.txt with recommended dependencies")


def create_dockerfile(project_path):
    """Create a production-ready Dockerfile with best practices."""
    
    dockerfile_content = '''# Production-ready FastAPI Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PATH="/app/.venv/bin:$PATH"

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    curl \\
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv .venv

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \\
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser \\
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check (critical for Azure Container Apps)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health/ || exit 1

# Production command with proper workers and timeout
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "--timeout", "120"]
'''
    
    dockerfile_path = project_path / "Dockerfile"
    dockerfile_path.write_text(dockerfile_content)
    print("✅ Created production-ready Dockerfile")


def create_main_app(project_path, project_name):
    """Create a basic FastAPI main.py with best practices."""
    
    main_content = f'''"""
{project_name} - FastAPI Application

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
    title="{project_name} API",
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
    return {{
        "message": "{project_name} API",
        "version": "1.0.0",
        "status": "healthy"
    }}


@app.get("/health/")
async def health_check():
    """Health check endpoint for load balancers and container orchestrators."""
    return {{
        "status": "healthy",
        "service": "{project_name}",
        "version": "1.0.0"
    }}


# Include your API routes here
# app.include_router(routes.router, prefix="/api/v1", tags=["api"])


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors."""
    return JSONResponse(
        status_code=500,
        content={{"message": "Internal server error", "detail": str(exc)}}
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
'''
    
    main_path = project_path / "app" / "main.py"
    main_path.write_text(main_content)
    print("✅ Created main FastAPI application")


def customize_for_project(project_path, project_name):
    """Customize template files with project-specific details."""
    
    print(f"🔧 Customizing files for project '{project_name}'...")
    
    # Update copilot instructions with project name
    copilot_file = project_path / ".github" / "copilot-instructions.md"
    if copilot_file.exists():
        content = copilot_file.read_text()
        content = content.replace("tqfaAPI", project_name)
        content = content.replace("TQFA API", f"{project_name} API")
        copilot_file.write_text(content)
        
    # Update version scripts with project name (if needed)
    # Add more customization as needed
    
    print("✅ Project customization complete")


def main():
    parser = argparse.ArgumentParser(
        description="Setup a new FastAPI project with TQFA best practices"
    )
    parser.add_argument("project_name", help="Name of the new project")
    parser.add_argument("--path", default=".", help="Path where to create the project")
    parser.add_argument("--no-download", action="store_true", 
                       help="Skip downloading latest best practices (use local)")
    
    args = parser.parse_args()
    
    project_path = Path(args.path) / args.project_name
    
    if project_path.exists():
        print(f"❌ Project directory '{project_path}' already exists")
        sys.exit(1)
    
    print(f"🚀 Setting up new FastAPI project: {args.project_name}")
    print(f"📁 Location: {project_path}")
    
    try:
        # Create project directory
        project_path.mkdir(parents=True)
        
        # Setup project structure and files
        create_project_structure(args.project_name, project_path)
        
        # Download or copy best practices
        if not args.no_download:
            download_best_practices(project_path)
        
        # Create essential files
        create_requirements_file(project_path)
        create_dockerfile(project_path)
        create_main_app(project_path, args.project_name)
        
        # Customize for this project
        customize_for_project(project_path, args.project_name)
        
        print(f"\\n🎉 Successfully created project '{args.project_name}'!")
        print(f"\\n📋 Next steps:")
        print(f"   cd {args.project_name}")
        print(f"   python -m venv .venv")
        print(f"   source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows")
        print(f"   pip install -r requirements.txt")
        print(f"   python -m app.main")
        print(f"\\n📚 Documentation:")
        print(f"   - Best practices: {project_path}/docs/best-practices/")
        print(f"   - Deployment guide: {project_path}/docs/best-practices/docker-deployment.md")
        print(f"   - Troubleshooting: {project_path}/docs/best-practices/troubleshooting.md")
        
    except Exception as e:
        print(f"❌ Error setting up project: {e}")
        if project_path.exists():
            shutil.rmtree(project_path)
        sys.exit(1)


if __name__ == "__main__":
    main()