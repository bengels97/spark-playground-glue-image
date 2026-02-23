# spark-playground-glue-image
Repository that includes a .devcontainer referencing a Glue Image. Allowing for trying out spark. 
## Prerequisites

### macOS
- **Docker Desktop**: [Download here](https://www.docker.com/products/docker-desktop)
- **Visual Studio Code**: [Download here](https://code.visualstudio.com/)
- **Dev Containers Extension**: Install from VSCode Extensions marketplace (`ms-vscode-remote.remote-containers`)

### Windows
- **Docker Desktop**: [Download here](https://www.docker.com/products/docker-desktop)
- **Visual Studio Code**: [Download here](https://code.visualstudio.com/)
- **Dev Containers Extension**: Install from VSCode Extensions marketplace (`ms-vscode-remote.remote-containers`)
- **WSL 2** (recommended, optional): [Installation guide](https://learn.microsoft.com/en-us/windows/wsl/install) - Provides better performance and is the default backend, but Docker Desktop can also run with Hyper-V

## Setting Up the Dev Container

1. **Clone this repository** and open it in VSCode
2. When prompted, click **"Reopen in Container"** (or press `Cmd+Shift+P` / `Ctrl+Shift+P` and select "Dev Containers: Reopen in Container")
3. VSCode will build the container using the Glue image - this may take several minutes on first run
4. Once complete, you'll have a fully configured Spark environment

## Debugging PySpark in VSCode

To inspect Spark DataFrames and objects during runtime:

1. **Open** `main.py` in VSCode
2. **Set a breakpoint** by clicking in the left gutter next to the line number where you want to pause (e.g., after `df = spark.read.csv(...)`)
3. **Start debugging**:
   - Press `F5` or go to Run → Start Debugging
   - Or click the Run and Debug icon in the sidebar and click "Python: Current File"
4. **Inspect variables** in the Debug sidebar:
   - View DataFrame schema, row count, and data
   - Use the Debug Console to run commands like `df.show()`, `df.printSchema()`, or `df.columns`
   - Hover over variables to see their values

### Debug Console Tips
While paused at a breakpoint, try these commands in the Debug Console:
```python
df.show(5)                    # Show first 5 rows
df.count()                    # Get row count
df.columns                    # List all columns
df.select("Horse_Name").show() # Show specific column
```

This interactive debugging makes it easy to experiment with Spark transformations and explore your data!