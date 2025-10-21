# Web Analysis Toolkit - Repository Split Migration Plan

**Created**: October 21, 2025  
**Status**: Planning Phase  
**Current Version**: tqfa-development-best-practices v2.1.4  
**Target**: Create standalone `web-analysis-toolkit` repository  

---

## 🎯 **Migration Objective**

Split CSS extraction tools from `tqfa-development-best-practices` into standalone `web-analysis-toolkit` repository while maintaining cross-references and ensuring no functionality is lost.

---

## 📊 **Migration Tracking Matrix**

### **Phase 1: Inventory & Planning** ✅ COMPLETE

| Item | Current Location | New Location | Status |
|------|-----------------|--------------|---------|
| Migration Plan | MIGRATION_PLAN.md | Created | ✅ Done |
| File Inventory | Below | Documented | ✅ Done |
| Cross-References | Below | Identified | ✅ Done |

### **Phase 2: Create New Repository** ⏳ PENDING

| Item | Action Required | Status | Notes |
|------|----------------|---------|-------|
| GitHub Repo | Create `Texas-Quantitative/web-analysis-toolkit` | ⏳ Pending | Public repo |
| Initial Commit | Empty repo with README | ⏳ Pending | v1.0.0-alpha |
| Branch Strategy | Setup main/dev branches | ⏳ Pending | Match best-practices |

### **Phase 3: Move Tools** ⏳ PENDING

| Tool File | Source Path | Destination Path | Status |
|-----------|------------|------------------|---------|
| extract-media-queries.mjs | tools/extract-media-queries.mjs | src/extractors/media-queries.mjs | ⏳ Pending |
| scrape-styles.mjs | tools/scrape-styles.mjs | src/extractors/static-css.mjs | ⏳ Pending |
| audit-computed.mjs | tools/audit-computed.mjs | src/extractors/computed-styles.mjs | ⏳ Pending |
| responsive-analyzer.mjs | tools/responsive-analyzer.mjs | src/analyzers/responsive.mjs | ⏳ Pending |
| comprehensive-analyzer.mjs | tools/comprehensive-analyzer.mjs | src/analyzers/comprehensive.mjs | ⏳ Pending |
| analyze-specific-elements.mjs | tools/analyze-specific-elements.mjs | src/analyzers/elements.mjs | ⏳ Pending |

### **Phase 4: Move Documentation** ⏳ PENDING

| Documentation File | Source Path | Destination Path | Status |
|-------------------|------------|------------------|---------|
| css-extraction-toolkit.md | docs/best-practices/ | docs/guides/css-extraction.md | ⏳ Pending |
| media-query-extraction.md | docs/best-practices/ | docs/guides/media-queries.md | ⏳ Pending |
| responsive-analysis-methodology.md | docs/best-practices/ | docs/guides/responsive-analysis.md | ⏳ Pending |
| web-analysis-caching.md | docs/best-practices/ | docs/guides/caching.md | ⏳ Pending |
| text-element-analysis-enhancement.md | docs/best-practices/ | docs/guides/text-elements.md | ⏳ Pending |
| intelligent-responsive-analysis.md | docs/best-practices/ | docs/roadmap/v2.2.0.md | ⏳ Pending |
| declarative-site-extraction.md | docs/best-practices/ | docs/roadmap/v3.0.0.md | ⏳ Pending |

### **Phase 5: Create New Files** ⏳ PENDING

| New File | Purpose | Status | Priority |
|----------|---------|---------|----------|
| README.md | Main overview | ⏳ Pending | CRITICAL |
| INSTALLATION.md | Setup guide | ⏳ Pending | CRITICAL |
| QUICK_START.md | 5-minute guide | ⏳ Pending | HIGH |
| WORKFLOW.md | Complete workflow | ⏳ Pending | HIGH |
| CONTRIBUTING.md | Contribution guide | ⏳ Pending | MEDIUM |
| CHANGELOG.md | Version history | ⏳ Pending | HIGH |
| .gitignore | Ignore patterns | ⏳ Pending | CRITICAL |
| package.json | Dependencies/scripts | ⏳ Pending | CRITICAL |

### **Phase 6: Update Best Practices** ⏳ PENDING

| File | Action | Status | Notes |
|------|--------|---------|-------|
| Remove tools/ directory | Delete moved tools | ⏳ Pending | After verification |
| Remove CSS docs | Delete moved documentation | ⏳ Pending | After verification |
| Create web-recreation-workflow.md | Reference guide | ⏳ Pending | Links to new repo |
| Update copilot-instructions-template.md | Update references | ⏳ Pending | Point to new repo |
| Update VERSION_HISTORY.md | Document split | ⏳ Pending | Version 2.2.0 |
| Update package.json | Version bump | ⏳ Pending | 2.1.4 → 2.2.0 |

### **Phase 7: Cross-References** ⏳ PENDING

| Reference Type | From | To | Status |
|----------------|------|-----|---------|
| Tool Installation | best-practices README | web-analysis-toolkit | ⏳ Pending |
| Workflow Guide | web-analysis-toolkit | best-practices deployment | ⏳ Pending |
| Agent Instructions | copilot template | web-analysis-toolkit docs | ⏳ Pending |
| GitHub Links | Both repos | Cross-reference | ⏳ Pending |

### **Phase 8: Testing & Verification** ⏳ PENDING

| Test | Description | Status | Notes |
|------|-------------|---------|-------|
| Tool Execution | Run all tools in new repo | ⏳ Pending | Test each tool |
| Cache Functionality | Verify caching works | ⏳ Pending | Test .cache/ directory |
| npm Scripts | Test all package.json scripts | ⏳ Pending | Ensure all work |
| Documentation Links | Verify all cross-links | ⏳ Pending | No 404s |
| Installation | Fresh install test | ⏳ Pending | Clean environment |

### **Phase 9: Release & Communication** ⏳ PENDING

| Task | Description | Status | Notes |
|------|-------------|---------|-------|
| Tag Releases | v2.2.0 (best-practices), v1.0.0 (toolkit) | ⏳ Pending | Git tags |
| GitHub Release Notes | Document split | ⏳ Pending | Explain migration |
| Update Organization README | Link both repos | ⏳ Pending | If applicable |
| Announcement | Notify users | ⏳ Pending | If applicable |

---

## 📂 **Complete File Inventory**

### **Files Moving to web-analysis-toolkit**

#### **Tools (tools/ → src/)**
```
✅ IDENTIFIED - READY TO MOVE:

tools/extract-media-queries.mjs              → src/extractors/media-queries.mjs
tools/scrape-styles.mjs                      → src/extractors/static-css.mjs
tools/audit-computed.mjs                     → src/extractors/computed-styles.mjs
tools/responsive-analyzer.mjs                → src/analyzers/responsive.mjs
tools/comprehensive-analyzer.mjs             → src/analyzers/comprehensive.mjs
tools/analyze-specific-elements.mjs          → src/analyzers/elements.mjs

NOTE: Check if all tools exist in current repo
```

#### **Documentation (docs/best-practices/ → docs/guides/)**
```
✅ IDENTIFIED - READY TO MOVE:

docs/best-practices/css-extraction-toolkit.md              → docs/guides/css-extraction.md
docs/best-practices/media-query-extraction.md              → docs/guides/media-queries.md
docs/best-practices/responsive-analysis-methodology.md     → docs/guides/responsive-analysis.md
docs/best-practices/web-analysis-caching.md                → docs/guides/caching.md
docs/best-practices/text-element-analysis-enhancement.md   → docs/guides/text-elements.md
docs/best-practices/intelligent-responsive-analysis.md     → docs/roadmap/v2.2.0.md
docs/best-practices/declarative-site-extraction.md         → docs/roadmap/v3.0.0.md
```

### **Files Staying in tqfa-development-best-practices**

```
✅ KEEPING (Core Best Practices):

docs/best-practices/docker-deployment.md
docs/best-practices/troubleshooting.md
docs/best-practices/scripts-and-tools.md
docs/best-practices/project-organization.md
docs/templates/copilot-instructions-template.md
scripts/bump_version.py
scripts/check_deployment.py
scripts/promote_healthy_revision.py
scripts/setup-new-project.ps1
scripts/setup-new-project.py
VERSION_HISTORY.md
ROADMAP.md (will be updated)
README.md (will be updated)
package.json (will be updated)
```

### **Files to Create in web-analysis-toolkit**

```
⏳ NEW FILES TO CREATE:

README.md                    # Main overview with quick start
INSTALLATION.md              # Detailed setup guide
QUICK_START.md               # 5-minute getting started
WORKFLOW.md                  # Complete analysis workflow
CONTRIBUTING.md              # How to contribute
CHANGELOG.md                 # Version history
LICENSE                      # MIT license
.gitignore                   # Node modules, cache, analysis outputs
.npmignore                   # If publishing to npm
package.json                 # Dependencies and scripts
package-lock.json            # Locked dependencies (generated)

docs/
  guides/                    # Moved from best-practices
  examples/                  # NEW: Usage examples
    basic-extraction.md
    complete-recreation.md
    component-analysis.md
  api/                       # NEW: API documentation
    programmatic-usage.md
    tool-options.md
  roadmap/                   # Moved planning docs
    v2.2.0.md
    v3.0.0.md

src/
  extractors/                # Moved tool files
  analyzers/                 # Moved tool files
  utils/                     # NEW: Shared utilities
    cache.mjs
    output.mjs
  
examples/                    # NEW: Code examples
  basic-usage.mjs
  advanced-workflow.mjs

tests/                       # NEW: Unit tests
  extractors/
  analyzers/
```

---

## 🔗 **Cross-Reference Updates**

### **In web-analysis-toolkit (Point to best-practices)**

#### **README.md**
```markdown
## 🚀 Related Projects

- **[TQFA Development Best Practices](https://github.com/Texas-Quantitative/tqfa-development-best-practices)** - 
  Production deployment patterns, Azure Container Apps, FastAPI architecture

**Using this toolkit with FastAPI/Azure?** See the [deployment best practices](link) for production-ready patterns.
```

#### **WORKFLOW.md**
```markdown
## Production Deployment

After recreating a website using this toolkit, see:
- [Docker Deployment Guide](link) - Containerization and Azure deployment
- [CI/CD Pipeline](link) - Automated deployment workflows
```

### **In tqfa-development-best-practices (Point to toolkit)**

#### **README.md - Update Main Overview**
```markdown
## 🎨 Web Analysis & Site Recreation

For pixel-perfect website recreation, use our dedicated toolkit:

**[Web Analysis Toolkit](https://github.com/Texas-Quantitative/web-analysis-toolkit)** - 
Comprehensive CSS extraction, responsive analysis, and media query extraction tools

**Capabilities**:
- Extract actual CSS media query breakpoints
- Multi-viewport responsive analysis
- Typography and layout extraction
- Smart caching for 30-60x performance

**See**: [Web Recreation Workflow](docs/best-practices/web-recreation-workflow.md) for integration guide
```

#### **docs/best-practices/web-recreation-workflow.md (NEW FILE)**
```markdown
# Web Recreation Workflow

**Reference**: [Web Analysis Toolkit](https://github.com/Texas-Quantitative/web-analysis-toolkit)

## Quick Start

1. **Install the toolkit**:
   ```bash
   git clone https://github.com/Texas-Quantitative/web-analysis-toolkit.git
   cd web-analysis-toolkit
   npm install
   ```

2. **Run complete analysis**:
   ```bash
   npm run analyze:complete -- https://target-site.com
   ```

3. **Use extracted data for recreation**

## Complete Guide

See the [Web Analysis Toolkit Documentation](link) for:
- Installation guide
- Complete workflow
- Tool reference
- Examples

## Integration with Best Practices

After recreation:
- [Docker Deployment](./docker-deployment.md) - Containerize your recreation
- [CI/CD Pipeline](./cicd-pipeline.md) - Automate deployments
- [Project Organization](./project-organization.md) - Organize analysis outputs
```

#### **docs/templates/copilot-instructions-template.md - Update CSS Section**
```markdown
## 🎨 **WEB ANALYSIS TOOLKIT - EXTERNAL TOOL**

**🚨 CRITICAL: Never guess CSS values - extract exact specifications**

This project can use the **Web Analysis Toolkit** for pixel-perfect website recreation:

**🌐 Toolkit Repository**: `https://github.com/Texas-Quantitative/web-analysis-toolkit`

### **Installation**
```bash
# Clone toolkit to project directory
git clone https://github.com/Texas-Quantitative/web-analysis-toolkit.git tools/web-analysis

# Install dependencies
cd tools/web-analysis
npm install
```

### **Available Tools**
```bash
# See toolkit documentation for complete command reference
cd tools/web-analysis

# Extract media queries (find exact breakpoints)
npm run analyze:media-queries -- https://target-site.com

# Analyze responsive behavior
npm run styles:responsive -- https://target-site.com

# Complete analysis
npm run analyze:complete -- https://target-site.com
```

### **Reference Documentation**
- **[Toolkit README](https://github.com/Texas-Quantitative/web-analysis-toolkit)** - Main overview
- **[Installation Guide](link)** - Detailed setup
- **[Workflow Guide](link)** - Complete analysis workflow
- **[Best Practices Integration](./docs/best-practices/web-recreation-workflow.md)** - Using with this project

**Remember**: Always extract exact specifications rather than approximating.
```

---

## 📝 **Version Strategy**

### **web-analysis-toolkit Versioning**
```
v1.0.0-alpha    Initial repository creation (empty)
v1.0.0-beta     All tools moved, documentation complete, testing phase
v1.0.0          First stable release, production-ready
v1.1.0          Minor improvements post-release
v2.0.0          Express/Detailed analysis modes (v2.2.0 in roadmap)
v3.0.0          Declarative extraction (v3.0.0 in roadmap)
```

### **tqfa-development-best-practices Versioning**
```
v2.1.4          Current version (media query extraction added)
v2.2.0          Repository split, toolkit moved to standalone
v2.2.1+         Continue best practices updates independently
```

---

## ⚠️ **Risk Mitigation**

### **Identified Risks**

| Risk | Impact | Mitigation | Status |
|------|--------|------------|---------|
| Broken links after split | HIGH | Update all cross-references before deletion | ⏳ Planned |
| Lost functionality | HIGH | Comprehensive testing phase | ⏳ Planned |
| Users can't find tools | MEDIUM | Clear migration documentation | ⏳ Planned |
| Cache directory mismatch | LOW | Document new cache location | ⏳ Planned |
| Import path changes | LOW | Test all tool executions | ⏳ Planned |

### **Rollback Plan**

If migration fails:
1. Keep both repositories (don't delete from best-practices)
2. Add "DEPRECATED" notice to tools in best-practices
3. Fix issues in web-analysis-toolkit
4. Retry migration when stable
5. Only delete from best-practices after 100% verification

---

## ✅ **Success Criteria**

### **Phase Completion Checklist**

- [ ] **Repository Created**: web-analysis-toolkit exists and is accessible
- [ ] **All Tools Moved**: Every tool file copied and working in new repo
- [ ] **All Docs Moved**: Every documentation file migrated
- [ ] **New Docs Created**: README, INSTALLATION, QUICK_START complete
- [ ] **Cross-References Updated**: All links point to correct locations
- [ ] **Testing Complete**: All tools tested and working
- [ ] **npm Scripts Work**: All package.json scripts execute successfully
- [ ] **Cache Works**: Caching functionality verified
- [ ] **Best Practices Updated**: Old references removed/updated
- [ ] **Version Tags Created**: Both repos tagged appropriately
- [ ] **No Broken Links**: All documentation links verified
- [ ] **Migration Documented**: VERSION_HISTORY entries in both repos

### **Final Verification**

Before marking complete:
1. ✅ Fresh install of toolkit works
2. ✅ All tools execute without errors
3. ✅ Documentation has no 404 links
4. ✅ Best practices references new repo correctly
5. ✅ Both repos have clear README files
6. ✅ GitHub release notes published
7. ✅ Old tools deleted from best-practices

---

## 📅 **Execution Timeline**

### **Estimated Duration: 3-4 hours**

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: Inventory | ✅ COMPLETE | None |
| Phase 2: Create Repo | 15 min | GitHub access |
| Phase 3: Move Tools | 30 min | Phase 2 |
| Phase 4: Move Docs | 30 min | Phase 2 |
| Phase 5: Create New Files | 60 min | Phase 3, 4 |
| Phase 6: Update Best Practices | 30 min | Phase 5 |
| Phase 7: Cross-References | 20 min | Phase 6 |
| Phase 8: Testing | 45 min | Phase 7 |
| Phase 9: Release | 20 min | Phase 8 |

---

## 🚀 **Ready to Begin**

**Current Status**: Planning Complete, Ready for Phase 2

**Next Step**: Create `Texas-Quantitative/web-analysis-toolkit` repository on GitHub

**Command to Start Phase 2**:
```bash
# Manual step: Create repository on GitHub
# Then clone to local:
cd D:\Users\dstac\TQSource
git clone https://github.com/Texas-Quantitative/web-analysis-toolkit.git
cd web-analysis-toolkit
```

---

## 📊 **Progress Tracking**

**Overall Progress**: 11% (Phase 1 complete)

- [x] Phase 1: Inventory & Planning (100%)
- [ ] Phase 2: Create Repository (0%)
- [ ] Phase 3: Move Tools (0%)
- [ ] Phase 4: Move Documentation (0%)
- [ ] Phase 5: Create New Files (0%)
- [ ] Phase 6: Update Best Practices (0%)
- [ ] Phase 7: Cross-References (0%)
- [ ] Phase 8: Testing (0%)
- [ ] Phase 9: Release (0%)

**Last Updated**: October 21, 2025  
**Status**: READY TO PROCEED
