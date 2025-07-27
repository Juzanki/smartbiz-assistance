# GhostCore — Central AI Threat Management Kernel for SmartInjectGPT

from SmartInjectGPT.ghost.ghost_guardian import GhostGuardian
from SmartInjectGPT.security.divine_signature import DivineSignature
from SmartInjectGPT.guardian.trusted_travel import TrustedTravel
from SmartInjectGPT.ghost.honeypot_trap import HoneypotTrap

class GhostCore:
    def __init__(self, owner_hash: str, safe_ips: list):
        self.guardian = GhostGuardian()
        self.signature = DivineSignature(expected_signature_hash=owner_hash)
        self.travel = TrustedTravel()
        self.honeypot = HoneypotTrap()
        self.safe_ips = safe_ips

    def handle_request(self, ip: str, user_agent: str, device_info: str,
                       typing_pattern: str, access_time: str, secret_phrase: str) -> str:

        # Step 1: Check if IP is known or traveling
        if ip not in self.safe_ips and not self.travel.is_ip_allowed(ip):
            prompt = self.travel.request_verification(ip)
            return f"[TRAVEL DETECTED] {prompt}"

        # Step 2: Verify owner identity
        if not self.signature.verify_signature(device_info, typing_pattern, access_time, secret_phrase):
            self.guardian.activate_fake_data()
            self.honeypot.activate_trap(ip, user_agent)
            return "[UNAUTHORIZED] Fake system activated. Honeypot engaged."

        # Step 3: Final check – time consistency
        if not self.travel.is_ip_allowed(ip):
            return "[WAITING] Access pending verification."

        return "[ACCESS GRANTED] Welcome, Owner."

    def get_status(self):
        return {
            "ghost_mode": self.guardian.fake_data_enabled or self.guardian.silent_mode,
            "honeypot_active": self.honeypot.trap_active,
            "last_verified_owner": self.signature.get_last_verified()
        }

    def emergency_lockdown(self):
        self.guardian.activate_silent_mode()
        return "[LOCKDOWN] Silent mode enforced. All injections blocked."
