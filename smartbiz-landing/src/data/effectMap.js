export const effectMap = {
  // 🌫️ Movement / Trail Effects
  smokeTrail: () => import('@/components/effects/SmokeTrail.vue'),
  shockWave: () => import('@/components/effects/ShockWave.vue'),
  sparkleBurst: () => import('@/components/effects/SparkleBurst.vue'),

  // 🔦 Lighting & Glow
  spotlight: () => import('@/components/effects/SpotlightGlow.vue'),
  neonFrame: () => import('@/components/effects/NeonFrame.vue'),
  stageLighting: () => import('@/components/effects/StageLighting.vue'),

  // ⚡ Energy / Impact
  energyPulse: () => import('@/components/effects/EnergyPulse.vue'),
  fireworksBurst: () => import('@/components/effects/FireworksBurst.vue'),

  // 🚩 Symbolic / Thematic
  flagPlant: () => import('@/components/effects/FlagPlantEffect.vue'),
  express: () => import('@/components/effects/ExpressEffect.vue'),

  // 💬 Enhanced Live Effects
  floatingComments: () => import('@/components/effects/FloatingComments.vue'),
  floatingParticles: () => import('@/components/effects/FloatingParticles.vue'),

  // 😎 Fun Layered Filters
  facefilter: () => import('@/components/effects/FacefilterLayer.vue'),
}
