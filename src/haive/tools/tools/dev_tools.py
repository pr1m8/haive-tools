# Warning: This executes code locally, which can be unsafe when not sandboxed
from typing import Annotated

from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

repl = PythonREPL()

@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    """Use this to execute python code. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user.
    """
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {e!r}"
    result_str = f"Successfully executed:\n\\`\\`\\`python\n{code}\n\\`\\`\\`\nStdout: {result}"
    return (
        result_str + "\n\nIf you have completed all tasks, respond with FINAL ANSWER."
    )



from langchain_community.tools import ShellTool

shell_tool = ShellTool()
