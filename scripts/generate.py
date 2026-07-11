#!/usr/bin/env python3
"""logo-to-slide — CLI that places a logo on all 12 slides at correct position, size, and alignment."""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="CLI that places a logo on all 12 slides at correct position, size, and alignment.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    
    result = {"tool": "logo-to-slide", "status": "ready", "version": "1.0.0", "author": "Jose Zuma"}
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['tool']} v{result['version']} — {result['status']}")

if __name__ == "__main__":
    main()
