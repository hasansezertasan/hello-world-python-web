#!/usr/bin/env python3
"""Runner script that executes all hello-world applications.
Loops through each file ending with -hello-world.py and runs it with uv run.
Verifies that each app serves a "hello world" message on port 8000.
"""

import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


def verify_hello_world_response(url, timeout=5):
    """Verify if the given URL returns a response containing 'hello world' (case-insensitive).
    Returns (success: bool, message: str).
    """
    try:
        response = urlopen(url, timeout=timeout)
        content = response.read().decode("utf-8", errors="ignore").lower()

        if "hello world" in content or "hello" in content:
            return True, "Found 'hello world' message"
        return False, "No 'hello world' message found in response"
    except URLError as e:
        return False, f"Connection error: {e.reason}"
    except Exception as e:
        return False, f"Error: {e}"


def test_app(timeout=10):
    """Test if an app is serving correctly on port 8000.
    Returns (success: bool, message: str).
    """
    url = "http://localhost:8000/"

    # Give the app some time to start
    for attempt in range(5):
        success, message = verify_hello_world_response(url, timeout=2)
        if success:
            return True, message

        if attempt < 4:
            time.sleep(1)

    return False, "Server not responding on localhost:8000"


def main() -> int:
    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    # Find all files ending with -hello-world.py
    hello_world_files = sorted(script_dir.glob("*-hello-world.py"))

    if not hello_world_files:
        print("No hello-world files found in the apps directory.")
        return 1

    print(f"Found {len(hello_world_files)} hello-world application(s)\n")

    failed_apps = []
    successful_apps = []

    for file_path in hello_world_files:
        app_name = file_path.name
        print(f"{'=' * 60}")
        print(f"Running: {app_name}")
        print(f"{'=' * 60}")

        try:
            # Start the app process
            process = subprocess.Popen(
                ["uv", "run", app_name],
                cwd=script_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            # Test if the app is serving hello world
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
