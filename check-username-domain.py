#!/usr/bin/env python3
import subprocess



expectedName = "Jaii-Hardas"
name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip()


if name == expectedName:
    print("You are using username as per configuration, proceeding to commit")
    exit(0)
else:
    print(f"Configured username is not as per config. It should be {expectedName}")
    exit(1)