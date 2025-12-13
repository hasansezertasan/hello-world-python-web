"""Runner script that executes all hello_world applications.

Loops through each file ending with _hello_world.py and runs it with uv run.
Verifies that each app serves a "Hello, World!" message on port 8000.
"""

import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


def verify_hello_world_response(url: str, timeout: int):
    """Verify if the given URL returns a response containing 'Hello, World!' (case-insensitive).
    Returns (success: bool, message: str).
    """
    try:
        response = urlopen(url, timeout=timeout)
        content = response.read().decode("utf-8", errors="ignore").lower()

        if "Hello, World!" in content or "hello" in content:
            return True, "Found 'Hello, World!' message"
        return False, "No 'Hello, World!' message found in response"
    except URLError as e:
        return False, f"Connection error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"


def test_app(timeout: int):
    """Test if an app is serving correctly on port 8000.
    Returns (success: bool, message: str).
    """
    url = "http://0.0.0.0:8000/"

    # Give the app some time to start
    for attempt in range(5):
        success, message = verify_hello_world_response(url, timeout=timeout)
        if success:
            return True, message

        if attempt < 4:
            time.sleep(1)

    return False, "Server not responding on 0.0.0.0:8000"


def main() -> int:
    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    # Find all files ending with _hello_world.py
    hello_world_files = sorted(script_dir.glob("*_hello_world.py"))

    if not hello_world_files:
        print("No hello_world files found in the apps directory.")
        return 1

    print(f"Found {len(hello_world_files)} hello_world application(s)\n")

    failed_apps: list[str] = []
    successful_apps: list[str] = []

    for file_path in hello_world_files:
        app_name = file_path.name
        print(f"{'=' * 60}")
        print(f"Running: {app_name}")
        print(f"{'=' * 60}")

        # Find any app that might be using port 8000 and terminate it
        port_process = subprocess.run(
            ["lsof", "-ti", ":8000"],
            check=False,
            capture_output=True,
            text=True,
        )
        for pid in port_process.stdout.splitlines():
            subprocess.run(["kill", "-9", pid], check=False)

        try:
            # Start the app process
            process = subprocess.Popen(
                ["uv", "run", app_name],
                cwd=script_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            # Test if the app is serving Hello, World!
            success, message = test_app(timeout=10)

            # Terminate the process
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()

            if success:
                successful_apps.append(app_name)
                print(f"✓ {app_name}: {message}\n")
            else:
                failed_apps.append(app_name)
                print(f"✗ {app_name}: {message}\n")

        except Exception as e:
            failed_apps.append(app_name)
            print(f"✗ {app_name} error: {e}\n")

    # Print summary
    print(f"{'=' * 60}")
    print("SUMMARY")
    print(f"{'=' * 60}")
    print(f"Successful: {len(successful_apps)}/{len(hello_world_files)}")
    print(f"Failed: {len(failed_apps)}/{len(hello_world_files)}")

    if failed_apps:
        print("\nFailed applications:")
        for app in failed_apps:
            print(f"  - {app}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
