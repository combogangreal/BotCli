# Remove previous builds
Remove-Item -Recurse -Force build, dist

# Build the distribution
python -m build

# Upload the package to PyPI using twine
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

# Clean up the build artifacts
Remove-Item -Recurse -Force build, dist
