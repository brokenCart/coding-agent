# Coding Agent

A lightweight, terminal-based AI coding assistant that uses LLMs via OpenRouter to autonomously explore, read, write, and execute Python code within a sandboxed working directory.

## Description

Coding Agent is a command-line interface (CLI) tool designed for automated code exploration and editing. It leverages large language models (LLMs) equipped with tool-calling capabilities to perform routine developer tasks autonomously. Given a natural language prompt, the agent iterates through tool calls—inspecting directory structures, reading source files, modifying code, and executing Python scripts within a strictly isolated sandbox directory until the task is completed or the maximum iteration limit is reached.

> **Disclaimer:** This is an experimental project with basic guardrails. Do not use it on production workloads or untrusted codebases.

## Key Features

- **Conversational Code Assistance**: Formulate tasks in natural language and let the agent plan and execute file modifications.
- **Autonomous Tool Selection**: Uses LLM function calling to list files, inspect contents, write changes, and execute scripts dynamically.
- **Path Sandboxing**: Enforces strict filesystem boundaries on all operations, preventing path traversal outside the working directory.
- **Subprocess Execution Controls**: Runs Python scripts in an isolated subprocess with configurable timeout limits to prevent runaway execution.
- **Iterative Reasoning Loop**: Automatically chains multiple tool calls in a loop before returning a final answer.
- **Verbose Inspection**: Optional verbose mode exposes detailed tool calls, arguments, outputs, and token usage for debugging.

## Installation

### Prerequisites

- Python 3.14 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`
- An [OpenRouter API Key](https://openrouter.ai/)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coding-agent.git
   cd coding-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Configuration

Custom options can be configured in [`config.py`](config.py):

| Variable | Default | Description |
| --- | --- | --- |
| `MAX_CHARS` | `10000` | Maximum characters to read from a single file |
| `EXECUTION_TIMEOUT` | `30` | Timeout in seconds for script execution |
| `WORKING_DIR` | `./calculator` | Sandboxed target directory |
| `MAX_AGENT_ITERATIONS` | `20` | Maximum tool-call iterations per run |

## Usage

```bash
# Basic usage
python main.py "List all files in the project"

# Verbose output showing tool execution & token usage
python main.py --verbose "Read main.py and explain what it does"

# Requesting code modifications
python main.py "Add a modulo operation to the calculator"

# Running tests and fixing failures
python main.py "Run the tests and fix any failures"
```

## Architecture

```mermaid
flowchart TD
    A["User Prompt (CLI)"] --> B["main.py - Agent Loop"]
    B --> C["OpenRouter API (LLM)"]
    C -->|text reply| D["Print & Exit"]
    C -->|tool_calls| E["call_function.py - Dispatcher"]
    E --> F["get_files_info"]
    E --> G["get_file_content"]
    E --> H["write_file"]
    E --> I["run_python_file"]
    F & G & H & I --> J["Sandboxed WORKING_DIR"]
    E -->|results| B
```

## Available Tools

| Tool | Source | Description |
| --- | --- | --- |
| `get_files_info` | [`functions/get_files_info.py`](functions/get_files_info.py) | Lists directory contents with sizes and file types |
| `get_file_content` | [`functions/get_file_content.py`](functions/get_file_content.py) | Reads file text up to `MAX_CHARS` limit |
| `write_file` | [`functions/write_file.py`](functions/write_file.py) | Creates or overwrites files, auto-creating directories |
| `run_python_file` | [`functions/run_python_file.py`](functions/run_python_file.py) | Executes Python scripts safely with arguments |

## Testing

Run tests for individual tools using Python:

```bash
python test_get_files_info.py
python test_get_file_content.py
python test_run_python_file.py
python test_write_file.py
```

## Security Considerations

- **Path Sandboxing**: Validates normalized absolute paths against `WORKING_DIR` to prevent unauthorized filesystem access.
- **Server-Side Context**: Sandboxing parameters are enforced by `call_function.py` and cannot be altered by LLM outputs.
- **No Direct Shell Execution**: Script execution uses explicit `subprocess.run` calls without `shell=True`.
- **Resource Constraints**: Limits output sizes (`MAX_CHARS`), execution duration (`EXECUTION_TIMEOUT`), and loop counts (`MAX_AGENT_ITERATIONS`).
