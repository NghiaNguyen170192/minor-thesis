# Setup script for graph environment dependencies
# This handles torch-scatter and torch-sparse which require wheel URLs

Write-Host "Setting up graph environment dependencies..." -ForegroundColor Green

# Detect Python executable in graph environment
$pythonExe = ".\graph\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    Write-Host "Error: Python executable not found at $pythonExe" -ForegroundColor Red
    exit 1
}

Write-Host "Using Python: $pythonExe"
Write-Host ""

# Install basic requirements from requirements file
Write-Host "Installing base requirements..." -ForegroundColor Yellow
& $pythonExe -m pip install -q numpy pandas scikit-learn scipy matplotlib networkx tqdm ipython pyarrow fastparquet altair

# Install PyG sparse operations with proper wheel URLs
Write-Host "Installing torch-scatter..." -ForegroundColor Yellow
& $pythonExe -m pip install -q torch-scatter -f https://data.pyg.org/whl/torch-2.7.0+cu118.html

Write-Host "Installing torch-sparse..." -ForegroundColor Yellow
& $pythonExe -m pip install -q torch-sparse -f https://data.pyg.org/whl/torch-2.7.0+cu118.html

Write-Host ""
Write-Host "✓ Graph environment setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Installed packages:" -ForegroundColor Cyan
& $pythonExe -m pip list | Select-String -Pattern "torch|pyg|geometric"
