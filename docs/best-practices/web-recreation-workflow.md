# Web Recreation Workflow

**Integration Guide**: Using the [Web Analysis Toolkit](https://github.com/Texas-Quantitative/web-analysis-toolkit) with TQFA Development Best Practices

---

## Overview

The **Web Analysis Toolkit** is now a standalone repository providing comprehensive CSS extraction, responsive analysis, and media query extraction capabilities. This guide shows how to integrate it with your TQFA projects for pixel-perfect website recreation.

## Quick Start

### 1. Install the Toolkit

```bash
# Clone the toolkit repository
git clone https://github.com/Texas-Quantitative/web-analysis-toolkit.git
cd web-analysis-toolkit
npm install
```

**Detailed Setup**: See [Installation Guide](https://github.com/Texas-Quantitative/web-analysis-toolkit/blob/main/INSTALLATION.md)

### 2. Run Complete Analysis

```bash
# Analyze target website
npm run analyze:complete -- https://target-site.com

# Output locations:
# - analysis/media-queries/     → Media query breakpoints
# - orig/_responsive-analysis.json → Responsive behavior
# - orig/_comprehensive-analysis.json → Site structure
# - orig/_computed-style-inventory.json → Applied styles
```

### 3. Apply to Your Project

Use the extracted data to recreate the site with pixel-perfect accuracy in your TQFA FastAPI or frontend project.

---

## Complete Workflow

### Phase 1: Analysis

**Run the complete toolkit analysis:**

```bash
cd web-analysis-toolkit

# 1. Responsive analysis across 7 breakpoints
npm run analyze:responsive -- https://target-site.com

# 2. Comprehensive element detection
npm run analyze:comprehensive -- https://target-site.com

# 3. Extract media query breakpoints
npm run extract:media-queries -- https://target-site.com

# 4. Get computed styles
npm run extract:computed -- https://target-site.com

# Or run everything at once:
npm run analyze:complete -- https://target-site.com
```

**Output Files:**
- `analysis/media-queries/YYYY-MM-DD/site-media-queries.json` - Actual breakpoints
- `orig/_responsive-analysis.json` - Viewport-by-viewport data
- `orig/_responsive-report.md` - Human-readable responsive patterns
- `orig/_comprehensive-analysis.json` - Complete site structure
- `orig/_comprehensive-report.md` - Section breakdown
- `orig/_computed-style-inventory.json` - All applied styles
- `orig/_comprehensive-analysis-screenshot.png` - Visual reference

### Phase 2: Recreation

**Set up your project structure:**

```bash
# In your TQFA project
mkdir -p frontend/src/pages
mkdir -p frontend/src/components
mkdir -p frontend/src/styles
```

**Copy analysis data:**

```bash
# Copy toolkit results to your project for reference
cp -r ../web-analysis-toolkit/analysis ./docs/site-analysis/
cp -r ../web-analysis-toolkit/orig ./docs/site-analysis/
```

**Extract key information:**

1. **Colors** - From `orig/_computed-style-inventory.json`:
   ```json
   {
     "inventory": {
       "colors": ["rgb(51, 51, 51)", "rgb(255, 255, 255)", ...],
       "backgroundColors": ["rgb(245, 245, 245)", ...],
       "borderColors": [...]
     }
   }
   ```

2. **Typography** - From `orig/_comprehensive-analysis.json`:
   ```json
   {
     "typography": {
       "hierarchy": [
         {
           "fontSize": "48px",
           "fontWeight": "700",
           "fontFamily": "Montserrat, sans-serif",
           "examples": ["Main Headline", ...]
         }
       ]
     }
   }
   ```

3. **Breakpoints** - From `analysis/media-queries/.../site-media-queries.json`:
   ```json
   {
     "summary": {
       "uniqueBreakpoints": [768, 992, 1200]
     }
   }
   ```

4. **Layout** - From `orig/_comprehensive-analysis.json`:
   ```json
   {
     "sections": [
       {
         "type": "Hero Section",
         "selector": ".hero",
         "position": { "width": 1440, "height": 600 }
       }
     ]
   }
   ```

### Phase 3: Implementation

**Create Tailwind config with extracted colors:**

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // From _computed-style-inventory.json
        'primary': 'rgb(51, 51, 51)',
        'secondary': 'rgb(245, 245, 245)',
        // ... extracted colors
      },
      fontFamily: {
        // From comprehensive analysis
        'heading': ['Montserrat', 'sans-serif'],
        'body': ['Open Sans', 'sans-serif'],
      }
    }
  }
}
```

**Implement components with extracted class names:**

```html
<!-- ✅ CORRECT: Preserve original class names -->
<nav class="navbar navbar-expand-lg">
  <div class="container-fluid px-4">
    <a class="navbar-brand" href="/">
      <!-- ... -->
    </a>
  </div>
</nav>

<!-- ❌ WRONG: Generic class names -->
<nav class="main-nav">
  <div class="container">
    <!-- Lost the connection to original analysis -->
  </div>
</nav>
```

**Apply responsive breakpoints from media queries:**

```css
/* From media-queries.json: breakpoints at 768, 992, 1200 */

@media (max-width: 1200px) {
  /* Extracted rules for .hero-section at 1200px */
  .hero-section {
    margin-left: auto; /* Changed from 325px at larger screens */
  }
}

@media (max-width: 992px) {
  .navbar-expand-lg {
    /* Responsive behavior from analysis */
  }
}
```

### Phase 4: Deployment

**Follow TQFA deployment best practices:**

1. **Local testing** (always test in `dev` branch first):
   ```bash
   # Start local server
   python main.py  # For FastAPI backend
   npm run dev     # For frontend
   ```

2. **Version management**:
   ```bash
   # Bump version before deployment
   python scripts/bump_version.py
   git add .
   git commit -m "Version bump to X.Y.Z - Implement [feature] recreation"
   ```

3. **Deploy to UAT**:
   ```bash
   git push origin uat
   # Automatic CI/CD deployment
   ```

4. **Validate deployment**:
   ```bash
   python scripts/check_deployment.py
   ```

**See Also:**
- [docker-deployment.md](./docker-deployment.md) - Azure Container Apps deployment
- [scripts-and-tools.md](./scripts-and-tools.md) - Automation scripts
- [troubleshooting.md](./troubleshooting.md) - Common issues

---

## Best Practices

### ✅ DO

- **Run complete analysis** before starting recreation
- **Preserve original class names** for maintainability
- **Use extracted breakpoints** instead of guessing
- **Reference analysis files** throughout development
- **Test locally first** (dev branch) before deploying
- **Use smart caching** (--force only when needed)

### ❌ DON'T

- **Guess CSS values** when you can extract them
- **Skip responsive analysis** for modern sites
- **Use generic class names** that lose context
- **Deploy without local testing**
- **Ignore actual breakpoints** from media queries
- **Approximate colors/fonts** when exact values available

---

## Tool Reference

### Toolkit Commands

All commands run from the `web-analysis-toolkit` directory:

```bash
# Extract media queries
npm run extract:media-queries -- <url>

# Analyze responsive behavior
npm run analyze:responsive -- <url>

# Get comprehensive site analysis
npm run analyze:comprehensive -- <url>

# Analyze specific elements
npm run analyze:elements -- <url> ".selector"

# Extract static CSS
npm run extract:static-css -- <url>

# Get computed styles
npm run extract:computed -- <url>

# Complete analysis
npm run analyze:complete -- <url>
```

**Options:**
- `--force` - Bypass cache, fetch fresh data
- `--property <prop>` - Filter media queries by CSS property
- `--selector <sel>` - Filter media queries by selector
- `--output <file>` - Custom output location

### TQFA Scripts

All commands run from your TQFA project directory:

```bash
# Version management
python scripts/bump_version.py

# Deployment validation
python scripts/check_deployment.py

# Traffic management
python scripts/promote_healthy_revision.py
```

---

## Troubleshooting

### Issue: Analysis Results Empty

**Problem**: Toolkit runs but output files are empty or incomplete

**Solution**:
1. Check if site blocks automation (some sites detect Puppeteer)
2. Try with `--force` to bypass cache
3. Check network connectivity
4. Review toolkit logs for CORS errors

### Issue: Breakpoints Don't Match Visual Changes

**Problem**: Media query extraction shows breakpoints that don't seem to affect layout

**Solution**:
1. Run `analyze:responsive` to see actual layout changes
2. Check if site uses JavaScript for responsive behavior
3. Some breakpoints may be for minor adjustments (colors, spacing)
4. Cross-reference with comprehensive analysis

### Issue: Class Names Not Found in Analysis

**Problem**: Can't find specific class names in analysis output

**Solution**:
1. Use `analyze:elements` with specific selector: `npm run analyze:elements -- <url> ".your-class"`
2. Check comprehensive analysis report for section detection
3. Class may be dynamically generated (check HTML source)
4. Use browser DevTools to verify class name spelling

### Issue: Colors Don't Match Exactly

**Problem**: Extracted colors slightly different from visual appearance

**Solution**:
1. Use computed styles (`extract:computed`) not static CSS
2. Check for opacity/transparency in rgba values
3. Some colors may be from images (not CSS)
4. Cross-reference multiple analysis outputs

---

## Resources

### Web Analysis Toolkit

- **[Main Repository](https://github.com/Texas-Quantitative/web-analysis-toolkit)** - Source code and releases
- **[Installation Guide](https://github.com/Texas-Quantitative/web-analysis-toolkit/blob/main/INSTALLATION.md)** - Setup instructions
- **[Quick Start](https://github.com/Texas-Quantitative/web-analysis-toolkit/blob/main/QUICK_START.md)** - 5-minute getting started
- **[Tool Documentation](https://github.com/Texas-Quantitative/web-analysis-toolkit/blob/main/docs/guides/)** - Complete guides

### TQFA Best Practices

- **[Docker Deployment](./docker-deployment.md)** - Azure Container Apps
- **[Scripts & Tools](./scripts-and-tools.md)** - Automation scripts
- **[Troubleshooting](./troubleshooting.md)** - Common issues
- **[Project Organization](./project-organization.md)** - File structure

---

## Example: Complete Recreation Flow

```bash
# 1. Clone toolkit (one-time setup)
git clone https://github.com/Texas-Quantitative/web-analysis-toolkit.git
cd web-analysis-toolkit
npm install

# 2. Analyze target site
npm run analyze:complete -- https://careington1.com

# 3. Review results
cat orig/_responsive-report.md
cat orig/_comprehensive-report.md
cat analysis/media-queries/*/careington1-com-media-queries.json

# 4. Copy to project for reference
cd ../your-tqfa-project
mkdir -p docs/site-analysis
cp -r ../web-analysis-toolkit/analysis docs/site-analysis/
cp -r ../web-analysis-toolkit/orig docs/site-analysis/

# 5. Implement recreation
# (Use extracted data throughout development)

# 6. Test locally
git checkout dev
python main.py  # Test endpoints

# 7. Deploy
python scripts/bump_version.py
git add .
git commit -m "feat: Recreate careington1.com homepage"
git push origin uat

# 8. Validate
python scripts/check_deployment.py
```

---

**Questions?** 
- Toolkit issues: [Open an issue](https://github.com/Texas-Quantitative/web-analysis-toolkit/issues)
- TQFA practices: [Open an issue](https://github.com/Texas-Quantitative/tqfa-development-best-practices/issues)
