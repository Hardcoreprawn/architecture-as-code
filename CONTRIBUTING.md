# Contributing to Architecture Visibility Platform

Thank you for your interest in contributing! This is an open source project to help enterprise architects automate boring chores.

## How to Contribute

### 1. Understand the Vision

Read these docs first:

- [README.md](README.md) - Project overview
- [docs/MVP-ARCHITECTURE-FOCUSED.md](docs/MVP-ARCHITECTURE-FOCUSED.md) - What we're building
- [docs/ROADMAP.md](docs/ROADMAP.md) - Implementation timeline

### 2. Find Something to Work On

- Check [Issues](https://github.com/YOUR_USERNAME/architecture-visibility-platform/issues) for open tasks
- Look for `good-first-issue` or `help-wanted` labels
- Start discussions in [Discussions](https://github.com/YOUR_USERNAME/architecture-visibility-platform/discussions) for new ideas

### 3. Development Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/architecture-visibility-platform.git
cd architecture-visibility-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (once we have them)
pip install -r requirements.txt

# Run tests
pytest
```

### 4. Make Changes

1. Create a branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Write tests if applicable
4. Update documentation
5. Commit with clear message: `git commit -m "Add feature: ..."`

### 5. Submit Pull Request

1. Push to your fork: `git push origin feature/your-feature-name`
2. Open PR against `main` branch
3. Describe what you changed and why
4. Link to related issues
5. Wait for review (we'll respond within 48 hours)

## Code Style

- **Python:** Follow PEP 8, use type hints
- **Markdown:** Keep docs clear and concise
- **Commits:** Use conventional commits (feat:, fix:, docs:, etc.)

## Areas We Need Help

### Immediate (Week 1-2)

- [ ] Python CLI scaffold
- [ ] Azure Resource Graph query builder
- [ ] Markdown report generator
- [ ] Unit tests

### Near-term (Week 3-6)

- [ ] Hugo theme customization
- [ ] Chart.js visualizations
- [ ] Azure Static Web Apps deployment
- [ ] Documentation improvements

### Later (Month 2+)

- [ ] Azure DevOps API integration
- [ ] Teams webhook integration
- [ ] Advanced grouping heuristics
- [ ] Multi-cloud support (AWS, GCP)

## Questions?

- Open a [Discussion](https://github.com/YOUR_USERNAME/architecture-visibility-platform/discussions)
- Comment on relevant [Issues](https://github.com/YOUR_USERNAME/architecture-visibility-platform/issues)
- Read the [docs/](docs/) folder

## Code of Conduct

Be respectful, constructive, and collaborative. We're all learning together.

---

**Thank you for contributing!** 🎉
