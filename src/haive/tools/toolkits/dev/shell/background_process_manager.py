"""
Background Process Manager Module

This module provides a utility for managing long-running background processes
in a shell environment. It handles process spawning, monitoring, and termination,
allowing for safer and more controlled execution of background tasks.

The module is particularly useful for managing persistent services, daemons,
or any long-running commands that need to be started, monitored, and cleanly
terminated programmatically.

Examples:
    >>> from haive.tools.toolkits.dev.shell.background_process_manager import BackgroundProcessManager
    >>> bg_manager = BackgroundProcessManager()
    >>> bg_manager.run_background("npm run dev")
    {'success': True, 'pid': 12345, 'message': '✅ npm run dev is running in the background'}
    >>> bg_manager.list_running()
    [{'pid': 12345, 'command': 'npm run dev', 'status': 'running'}]
    >>> bg_manager.stop_process(12345)
    {'success': True, 'message': '✅ Process 12345 stopped'}
"""

import os
import shlex
import signal
import subprocess
from typing import Any, Dict, List, Optional, Union

import psutil


class BackgroundProcessManager:
    """Manages long-running background processes.

    This class provides methods to start, monitor, and stop background processes,
    as well as utilities to inspect network listeners and track resource usage.

    Attributes:
        processes: Dictionary mapping process IDs to subprocess.Popen objects.
    """

    def __init__(self):
        """Initialize the background process manager.

        Sets up an empty processes dictionary to track spawned processes.
        """
        self.processes = {}

    def run_background(
        self,
        command: str,
        cwd: Optional[str] = None,
        env: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Start a long-running command in the background.

        Args:
            command: The shell command to run in the background.
            cwd: Optional working directory for the process.
            env: Optional environment variables for the process.

        Returns:
            Dictionary containing:
                - success: Boolean indicating whether the process started successfully.
                - pid: Process ID of the spawned process if successful.
                - message: Success or error message.
                - error: Error details if the process failed to start.

        Raises:
            OSError: If there's an issue with the system call to create the process.
        """
        try:
            # Split command into arguments
            cmd_args = shlex.split(command)

            # Start the process
            process = subprocess.Popen(
                cmd_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=cwd,
                env=env,
            )

            # Store the process
            self.processes[process.pid] = process

            return {
                "success": True,
                "pid": process.pid,
                "message": f"✅ {command} is running in the background",
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def list_running(self) -> List[Dict[str, Any]]:
        """List currently running background processes.

        Returns:
            List of dictionaries containing information about each running process:
                - pid: Process ID.
                - command: The command that started the process.
                - status: Current status of the process.
                - memory: Memory usage in MB (if available).
                - cpu: CPU usage percentage (if available).
        """
        active_processes = []

        for pid, process in list(self.processes.items()):
            try:
                if psutil.pid_exists(pid):
                    # Get process info
                    ps_process = psutil.Process(pid)
                    proc_info = {
                        "pid": pid,
                        "command": " ".join(process.args),
                        "status": "running",
                    }

                    # Try to get resource usage
                    try:
                        proc_info["memory"] = (
                            f"{ps_process.memory_info().rss / (1024 * 1024):.2f} MB"
                        )
                        proc_info["cpu"] = f"{ps_process.cpu_percent()}%"
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        # Skip resource info if not available
                        pass

                    active_processes.append(proc_info)
                else:
                    # Process no longer exists, remove from tracking
                    del self.processes[pid]
            except psutil.NoSuchProcess:
                # Process no longer exists, remove from tracking
                del self.processes[pid]

        return active_processes

    def stop_process(self, pid: int, force: bool = False) -> Dict[str, Any]:
        """Stop a specific background process.

        Args:
            pid: The process ID to stop.
            force: Whether to forcefully kill the process (SIGKILL) rather than
                   gracefully terminate it (SIGTERM).

        Returns:
            Dictionary containing:
                - success: Boolean indicating whether the process was stopped successfully.
                - message: Success or error message.
                - error: Error details if the process could not be stopped.
        """
        try:
            if pid in self.processes:
                process = self.processes[pid]

                if force:
                    # Force kill with SIGKILL
                    process.kill()
                else:
                    # Graceful termination with SIGTERM
                    process.terminate()

                # Wait for process to terminate (with timeout)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # If it doesn't terminate in time, force kill
                    process.kill()
                    process.wait()

                # Remove from tracked processes
                del self.processes[pid]
                return {"success": True, "message": f"✅ Process {pid} stopped"}
            else:
                return {
                    "success": False,
                    "error": f"❌ Process {pid} not found in managed processes",
                }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def list_network_listeners(self) -> List[Dict[str, Any]]:
        """List all processes listening on network ports.

        Returns:
            List of dictionaries containing information about each listening process:
                - port: The port number being listened on.
                - process: The process name.
                - pid: The process ID.
                - address: The binding address.
                - protocol: The protocol (TCP/UDP).
        """
        listeners = []

        try:
            for conn in psutil.net_connections(kind="inet"):
                if conn.status == "LISTEN":
                    try:
                        process = psutil.Process(conn.pid) if conn.pid else None
                        listeners.append(
                            {
                                "port": conn.laddr.port,
                                "process": process.name() if process else "Unknown",
                                "pid": conn.pid,
                                "address": conn.laddr.ip,
                                "protocol": "TCP",  # psutil currently only supports TCP
                            }
                        )
                    except psutil.NoSuchProcess:
                        # Process no longer exists
                        pass
        except (psutil.AccessDenied, PermissionError):
            # Return limited information if access is denied
            return [{"error": "Access denied to network connection information"}]

        return listeners

    def get_process_logs(self, pid: int, max_lines: int = 100) -> Dict[str, Any]:
        """Get stdout and stderr output from a running process.

        Args:
            pid: The process ID to get logs for.
            max_lines: Maximum number of lines to return.

        Returns:
            Dictionary containing:
                - success: Boolean indicating whether logs were retrieved successfully.
                - stdout: Standard output from the process.
                - stderr: Standard error from the process.
                - error: Error details if logs could not be retrieved.
        """
        if pid not in self.processes:
            return {
                "success": False,
                "error": f"❌ Process {pid} not found in managed processes",
            }

        process = self.processes[pid]

        try:
            # Get output without blocking
            stdout, stderr = [], []

            # Read from stdout
            while process.stdout and len(stdout) < max_lines:
                line = process.stdout.readline()
                if not line:
                    break
                stdout.append(line.strip())

            # Read from stderr
            while process.stderr and len(stderr) < max_lines:
                line = process.stderr.readline()
                if not line:
                    break
                stderr.append(line.strip())

            return {
                "success": True,
                "stdout": "\n".join(stdout) if stdout else "",
                "stderr": "\n".join(stderr) if stderr else "",
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def cleanup(self) -> Dict[str, Any]:
        """Stop all managed processes and clean up resources.

        Returns:
            Dictionary containing:
                - success: Boolean indicating whether cleanup was successful.
                - stopped: Number of processes stopped.
                - errors: List of errors encountered during cleanup.
        """
        errors = []
        stopped_count = 0

        for pid in list(self.processes.keys()):
            try:
                result = self.stop_process(pid)
                if result["success"]:
                    stopped_count += 1
                else:
                    errors.append(
                        f"Failed to stop PID {pid}: {result.get('error', 'Unknown error')}"
                    )
            except Exception as e:
                errors.append(f"Error stopping PID {pid}: {str(e)}")

        return {"success": len(errors) == 0, "stopped": stopped_count, "errors": errors}
