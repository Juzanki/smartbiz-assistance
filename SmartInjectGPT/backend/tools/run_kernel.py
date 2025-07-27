# run_kernel.py — Secure Runner for SmartInjectGPT Kernel

from backend.firewall.prompt_firewall import scan_prompt_file
from backend.kernel.smartinject_kernel import SmartInjectKernel
from backend.notifications.telegram_alert import send_telegram_alert
from backend.identity.soul_signature import verify_identity
from backend.prophecy.prophetic_guard import verify_kernel_signature
from backend.prophecy.dream_memory_log import log_dream




def main():
    print("\n🚀 SmartInjectGPT Kernel Execution Started")

    scan = scan_prompt_file("input_dream.txt")

    if scan["status"] != "allowed":
        print("❌ BLOCKED by Prompt Firewall:", scan["reason"])
        send_telegram_alert(f"❌ Prompt Blocked:\nReason: {scan['reason']}")
        return

    prompt = scan["prompt"]
    print("🧠 Prompt accepted. Running kernel...\n")

    try:
        SmartInjectKernel().run(prompt)
        print("\n✅ Kernel execution completed.")
    except Exception as e:
        print(f"\n❌ Kernel execution failed: {str(e)}")
        send_telegram_alert(f"❌ Kernel crashed with error:\n{str(e)}")


if __name__ == "__main__":
    main()

if not verify_identity():
    send_telegram_alert("⚠️ Soul signature verification failed. Kernel halted.")
    print("❌ Soul Signature Rejected.")
    exit()
    
if not verify_kernel_signature():
    send_telegram_alert("🚨 Kernel override attempt detected. Prophetic Guard triggered.")
    print("❌ Kernel verification blocked.")
    exit()

log_dream(prompt)  # hifadhi ndoto ya kila prompt
