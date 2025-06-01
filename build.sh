#!/bin/bash

# Build script for production deployment to GitHub Pages
# This builds the site with the correct basepath for the GitHub repository

echo "Building site for production..."
python3 src/main.py "/static-site-generator/"
echo "Production build complete!"
