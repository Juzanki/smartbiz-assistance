<template>
  <div class="min-vh-100 d-flex flex-column justify-content-center align-items-center bg-dark px-3">
    <!-- 🧠 LOGO + Title -->
    <div class="text-center mb-3 mt-4 animate-fade-in">
      <img
        src="@/assets/logo-circle.png"
        alt="SmartBiz Logo"
        class="rounded-circle border border-warning shadow"
        style="width: 72px; height: 72px; background: #fff;"
      />
      <h2 class="fw-bold text-warning mt-3" style="font-size: 1.6rem;">Create Your Account</h2>
      <p class="text-secondary small mt-1">Join SmartBiz and simplify your business journey.</p>
    </div>

    <!-- 🧾 SIGNUP CARD -->
    <div class="card shadow-lg border border-warning rounded-4 p-4 w-100" style="max-width: 400px; background: #181829;">
      <form @submit.prevent="onSignup" autocomplete="off">
        <!-- FULL NAME -->
        <div class="mb-3">
          <label for="fullname" class="form-label text-warning small">Full Name</label>
          <input type="text" id="fullname" v-model.trim="form.full_name" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="60" autocomplete="name" placeholder="e.g. Julius Zakayo" />
        </div>

        <!-- USERNAME -->
        <div class="mb-3">
          <label for="username" class="form-label text-warning small">Username</label>
          <input type="text" id="username" v-model.trim="form.username" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="30" autocomplete="username" placeholder="Unique username" />
        </div>

        <!-- EMAIL -->
        <div class="mb-3">
          <label for="email" class="form-label text-warning small">Email Address</label>
          <input type="email" id="email" v-model.trim="form.email" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="100" autocomplete="email" placeholder="your@email.com" />
        </div>

        <!-- PASSWORD -->
        <div class="mb-3">
          <label for="password" class="form-label text-warning small">Password</label>
          <input type="password" id="password" v-model="form.password" class="form-control bg-[#232338] text-light border-0"
                 required minlength="8" autocomplete="new-password" placeholder="Strong password" />
          <div v-if="form.password && !isStrongPassword(form.password)" class="text-danger small mt-1">
            Password must be at least 8 characters, include upper/lowercase, a number & a symbol.
          </div>
        </div>

        <!-- PHONE -->
        <div class="mb-3">
          <label class="form-label text-warning small">Phone Number</label>
          <div class="d-flex gap-2">
            <select v-model="form.country_code" class="form-select w-auto bg-[#232338] text-light border-0" required>
              <option v-for="code in countryCodes" :key="code.value" :value="code.value">{{ code.label }}</option>
            </select>
            <input type="tel" v-model="form.phone_number" required pattern="^[1-9][0-9]{7,13}$"
                   class="form-control bg-[#232338] text-light border-0"
                   maxlength="13" autocomplete="tel" placeholder="712345678" />
          </div>
          <small class="text-secondary">Start without 0 (e.g. <span class="text-warning">712345678</span>)</small>
        </div>

        <!-- LANGUAGE -->
        <div class="mb-3">
          <label class="form-label text-warning small">Preferred Language</label>
          <select class="form-select bg-[#232338] text-light border-0" v-model="form.language" required>
            <option value="sw">Kiswahili</option>
            <option value="en">English</option>
            <option value="fr">Français</option>
            <option value="ar">العربية</option>
          </select>
        </div>

        <!-- OPTIONAL FIELDS -->
        <div class="mb-3">
          <label class="form-label text-warning small">Business Name <span class="text-secondary">(Optional)</span></label>
          <input type="text" class="form-control bg-[#232338] text-light border-0" v-model="form.business_name" maxlength="60" />
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small">Business Type <span class="text-secondary">(Optional)</span></label>
          <select class="form-select bg-[#232338] text-light border-0" v-model="form.business_type">
            <option value="">Select Type</option>
            <option value="Retail">Retail</option>
            <option value="Service">Service</option>
            <option value="Wholesale">Wholesale</option>
            <option value="Education">Education</option>
            <option value="Other">Other</option>
          </select>
        </div>

        <!-- TERMS -->
        <div class="form-check d-flex align-items-center gap-2 mb-3">
          <input type="checkbox" id="terms" v-model="agreed" required
                 class="form-check-input bg-[#232338] border-warning"
                 style="accent-color: #FFD700; width: 1.15em; height: 1.15em;" />
          <label for="terms" class="form-check-label text-light small">
            I agree to the <a href="#" class="text-warning text-decoration-underline">terms and conditions</a>
          </label>
        </div>

        <!-- SIGN UP BUTTON -->
        <button class="btn btn-warning w-100 fw-bold py-2 rounded-3" :disabled="loading || !canSubmit">
          <span v-if="loading"><span class="spinner-border spinner-border-sm me-2"></span> Signing Up...</span>
          <span v-else>Sign Up</span>
        </button>
      </form>

      <!-- ALREADY ACCOUNT -->
      <div class="text-center mt-4 small text-secondary">
        Already have an account?
        <router-link to="/login" class="text-warning fw-bold text-decoration-underline ms-1">Login</router-link>
      </div>
    </div>

    <!-- Extra space bottom -->
    <div class="mt-4 mb-3"></div>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

// 🌍 Country Codes for Phone Input
const countryCodes = [
  { value: '+255', label: '🇹🇿 +255 (TZ)' },
  { value: '+254', label: '🇰🇪 +254 (KE)' },
  { value: '+256', label: '🇺🇬 +256 (UG)' },
  { value: '+250', label: '🇷🇼 +250 (RW)' },
  { value: '+257', label: '🇧🇮 +257 (BI)' },
  { value: '+211', label: '🇸🇸 +211 (SS)' },
  { value: '+27',  label: '🇿🇦 +27 (ZA)' },
  { value: '+234', label: '🇳🇬 +234 (NG)' },
  { value: '+233', label: '🇬🇭 +233 (GH)' },
  { value: '+20',  label: '🇪🇬 +20 (EG)' },
  { value: '+1',   label: '🇺🇸 +1 (US)' },
  { value: '+44',  label: '🇬🇧 +44 (UK)' },
  { value: '+91',  label: '🇮🇳 +91 (IN)' }
]

// 📦 Dependencies
const toast = useToast()
const router = useRouter()

// 🔄 Form State
const form = ref({
  full_name: '',
  username: '',
  email: '',
  password: '',
  country_code: '+255',
  phone_number: '',
  language: 'sw',
  business_name: '',
  business_type: ''
})

const agreed = ref(false)
const loading = ref(false)

// ✅ Password Validation
const isStrongPassword = (password) =>
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/.test(password)

// ✅ Form Validation Check
const canSubmit = computed(() =>
  form.value.full_name &&
  form.value.username &&
  form.value.email &&
  form.value.password &&
  form.value.phone_number &&
  agreed.value &&
  isStrongPassword(form.value.password)
)

// 🌐 API Base (production or fallback)
const API_BASE = import.meta.env.VITE_API_BASE?.trim() || 'https://api.smartbiz.tld'

// 🚀 Handle Signup Logic
const onSignup = async () => {
  if (!canSubmit.value) {
    toast.error('Please fill all required fields correctly!')
    return
  }

  loading.value = true
  try {
    const payload = { ...form.value }
    payload.phone_number = `${form.value.country_code}${form.value.phone_number}`

    const { data } = await axios.post(`${API_BASE}/auth/register`, payload)

    toast.success('🎉 Signup successful! Please login.')
    setTimeout(() => {
      router.push('/login')
    }, 1000)
  } catch (err) {
    const errorMsg =
      err.response?.data?.detail ||
      err.response?.data?.message ||
      err.message ||
      '❌ Signup failed. Please try again.'

    toast.error(errorMsg)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 🌑 Dark Background Base */
.bg-dark {
  background: #181829 !important;
}

/* 🧊 Card Styling */
.card {
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.4), 0 0 0 2px #ffd70033;
  border: 2px solid #ffd700 !important;
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 32px rgba(0, 0, 0, 0.5), 0 0 0 2px #ffd70066;
}

/* 📝 Inputs & Selects */
input.form-control,
select.form-select,
.form-check-input {
  background: #232338 !important;
  color: #fff !important;
  border: none !important;
  border-radius: 0.5rem;
  padding: 0.65rem 0.85rem;
  font-size: 0.95rem;
  transition: box-shadow 0.25s ease;
}

input.form-control::placeholder {
  color: #bbb !important;
  opacity: 0.85;
}
select.form-select {
  color: #ccc !important;
}

/* ✨ Focus States */
input:focus,
select:focus {
  outline: none !important;
  box-shadow: 0 0 0 2px #ffd70099 !important;
}

/* 🟡 Divider Line */
hr {
  border-top: 2px solid #ffd700 !important;
  opacity: 0.6;
  margin-top: 1rem;
  margin-bottom: 1.5rem;
}

/* 🌟 Primary Action Button */
.btn-warning {
  background-color: #ffd700 !important;
  color: #181829 !important;
  font-weight: 700;
  font-size: 1rem;
  border: none !important;
  border-radius: 0.6rem;
  transition: all 0.2s ease;
}
.btn-warning:hover {
  background-color: #ffdd33 !important;
  box-shadow: 0 0 10px rgba(255, 214, 0, 0.4);
}
.btn-warning:active,
.btn-warning:focus {
  background: #ffec80 !important;
  outline: none !important;
}

/* 📌 Labels & Text */
.text-warning {
  color: #ffd700 !important;
}
.form-label,
.form-check-label {
  font-size: 0.85rem;
  color: #ccc;
}

/* 🧷 Checkbox Styling */
.form-check-input {
  accent-color: #ffd700 !important;
  width: 1.15em;
  height: 1.15em;
  margin-top: 0.25em;
  border: 2px solid #ffd700 !important;
  border-radius: 0.3em;
  cursor: pointer;
  appearance: auto !important;
  -webkit-appearance: auto !important;
}
.form-check-label {
  cursor: pointer;
}

/* 📱 Responsive Adjustments */
@media (max-width: 480px) {
  h2 {
    font-size: 1.3rem !important;
  }

  .btn-warning {
    font-size: 0.95rem;
    padding: 0.6rem 1.1rem;
  }

  input.form-control,
  select.form-select {
    font-size: 0.9rem;
    padding: 0.6rem 0.85rem;
  }
}
</style>

