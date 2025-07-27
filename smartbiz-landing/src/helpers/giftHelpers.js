// giftHelpers.js 🚀 SmartBiz Live Gift Engine — Enhanced with Special Glow

// 🎨 Unique Animations by Tier
const animationByTier = {
  Lite: 'float-up',
  Rare: 'spiral-spark',
  Epic: 'orbit-flip',
  Legendary: 'crown-zoom',
  Mythic: 'shine-rise',
  Supreme: 'kingdom-power',
  Default: 'float-up'
}

// 🔊 Sounds Only for Premium Tiers
const soundByTier = {
  Epic: '/sounds/epic-swish.mp3',
  Mythic: '/sounds/blast.mp3',
  Supreme: '/sounds/legendary.mp3'
}

// 💠 Ultra Glow Effects by Coin Value
function getSpecialGlowEffect(coins) {
  if (coins >= 5000) return '/effects/universe-blast.svg'
  if (coins >= 2000) return '/effects/fusion-orb.svg'
  if (coins >= 1000) return '/effects/fullscreen-burst.svg'
  if (coins >= 500) return '/effects/ring-wave.svg'
  if (coins >= 200) return '/effects/ray-glow.svg'
  if (coins >= 100) return '/effects/soft-glow.svg'
  return null
}

// ⏱️ Duration Based on Coin Value
function getDurationByCoins(coins) {
  if (coins >= 5000) return 6000
  if (coins >= 2000) return 5000
  if (coins >= 1000) return 4000
  if (coins >= 200) return 3000
  if (coins >= 50) return 2500
  if (coins >= 10) return 2000
  return 1600
}

// 🔮 Fallback for Gift Visual Effects
function getDefaultEffect(gift) {
  if (gift.effect) return gift.effect
  const glow = getSpecialGlowEffect(gift.coins)
  if (glow) return glow
  if (['Mythic', 'Supreme', 'Legendary'].includes(gift.tier)) {
    return '/effects/sparkle-glow.svg'
  }
  return null
}

// 🖥️ Display Mode by Value
function getDisplayMode(coins) {
  if (coins >= 1000) return 'fullscreen'
  if (coins >= 200) return 'glow'
  return 'center'
}

// 🧬 Generate Smart Gift Object
export function buildGift(rawGift) {
  const now = Date.now()

  return {
    id: rawGift.id || `gift-${now}`, // Ensure ID exists
    ...rawGift,
    animation: rawGift.animation || getDefaultAnimation(rawGift.tier),
    duration: rawGift.duration || getDurationByCoins(rawGift.coins),
    effect: getDefaultEffect(rawGift),
    sound: rawGift.sound || soundByTier[rawGift.tier] || null,
    mode: getDisplayMode(rawGift.coins),
    timestamp: now
  }
}

// 🎞️ Fallback Animation Getter
export function getDefaultAnimation(tier) {
  return animationByTier[tier] || animationByTier.Default
}

// 🔊 Play Gift Sound (safe across platforms)
export function playGiftSound(gift) {
  if (gift?.sound) {
    try {
      const audio = new Audio(gift.sound)
      audio.volume = 0.85
      audio.play().catch((err) => {
        console.warn('🔇 Sound blocked or failed:', err)
      })
    } catch (error) {
      console.warn('🎧 Gift sound error:', error)
    }
  }
}
