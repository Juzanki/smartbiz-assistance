# shadow_tester.py — Runs isolated test on a module
import sys, os

def run_shadow_test(module_name):
    print(f"🔍 Shadow Testing: {module_name}")
    # hapa unaweza kuweka test ya kweli — for now dummy
    if "fail" in module_name:
        raise Exception("Module contains invalid code.")
    print("✅ Passed Shadow Test.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: shadow_tester.py <module_name>")
        sys.exit(1)
    run_shadow_test(sys.argv[1])
