const OWNER_KEY_NAME = 'owner_token'
const ENCRYPTION_SECRET = 'divine-salt-777' // unaweza tumia hashing lib
const EXPIRY_MINUTES = 15

// 🔐 Basic encryption kwa demonstration (not cryptographically strong)
function encrypt(value) {
  return btoa(`${value}|${ENCRYPTION_SECRET}`)
}

function decrypt(encoded) {
  try {
    const decoded = atob(encoded)
    const [value, salt] = decoded.split('|')
    if (salt === ENCRYPTION_SECRET) return value
    return null
  } catch {
    return null
  }
}

// ✅ Hifadhi encrypted key + timestamp
export function setOwnerKey(rawKey) {
  const encryptedKey = encrypt(rawKey)
  const payload = {
    token: encryptedKey,
    timestamp: Date.now()
  }
  localStorage.setItem(OWNER_KEY_NAME, JSON.stringify(payload))
}

// ✅ Hakiki kama bado ni owner halali na token haija-expire
export function isOwner() {
  const data = localStorage.getItem(OWNER_KEY_NAME)
  if (!data) return false

  try {
    const { token, timestamp } = JSON.parse(data)

    const now = Date.now()
    const elapsed = (now - timestamp) / (1000 * 60) // in minutes

    if (elapsed > EXPIRY_MINUTES) {
      removeOwnerKey()
      return false
    }

    const decrypted = decrypt(token)
    return decrypted === 'prophetic-777-lock'
  } catch {
    return false
  }
}

// ✅ Ondoa ruhusa ya owner
export function removeOwnerKey() {
  localStorage.removeItem(OWNER_KEY_NAME)
}

// ✅ Ruhusu kutumia kwa status check
export function isOwnerActive() {
  return isOwner()
}
