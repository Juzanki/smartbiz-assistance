import { createRouter, createWebHistory } from 'vue-router'

// === Auth Pages
import LoginPage from '@/pages/auth/LoginPage.vue'
import RegisterPage from '@/pages/auth/RegisterPage.vue'
import RegisterConfirmation from '@/pages/auth/RegisterConfirmation.vue'
import ForgotPassword from '@/pages/auth/ForgotPassword.vue'

// === Public
import HomeView from '@/modules/SmartInjectGPT/HomeView.vue'

// === Owner Pages
import DashboardOwner from '@/pages/owner/DashboardOwner.vue'
import ManageAdmins from '@/pages/owner/ManageAdmins.vue'
import OtpLogs from '@/pages/owner/OtpLogs.vue'
import ActivityLogs from '@/pages/owner/ActivityLogs.vue'
import SecurityPanel from '@/pages/owner/SecurityPanel.vue'
import SystemSettings from '@/pages/owner/SystemSettings.vue'
import InjectPage from '@/pages/owner/InjectPage.vue'
import LogsPage from '@/pages/owner/LogsPage.vue'
import ShieldPage from '@/pages/owner/ShieldPage.vue'

// === Admin Pages (Lazy Load)
const AdminDashboard = () => import('@/pages/Admins/AdminDashboard.vue')
const AdminManageUsers = () => import('@/pages/Admins/AdminManageUsers.vue')
const AdminLogsPage = () => import('@/pages/Admins/AdminLogsPage.vue')

// === GPT Modules (Lazy Load)
const VisionConsole = () => import('@/modules/SmartInjectGPT/VisionConsole.vue')
const AIChatBot = () => import('@/modules/SmartInjectGPT/AIChatBot.vue')
const DreamTrigger = () => import('@/modules/SmartInjectGPT/DreamTrigger.vue')
const KernelMonitor = () => import('@/modules/SmartInjectGPT/KernelMonitor.vue')
const PromptHistory = () => import('@/modules/SmartInjectGPT/PromptHistory.vue')

// === Errors
const NotAuthorized = () => import('@/pages/errors/NotAuthorized.vue')
const NotFound = () => import('@/pages/errors/NotFound.vue')

// === Route Definitions
const routes = [
  // Public
  { path: '/', name: 'home', component: HomeView },

  // Auth
  { path: '/login', name: 'login', component: LoginPage, meta: { guestOnly: true } },
  { path: '/register', name: 'register', component: RegisterPage, meta: { guestOnly: true } },
  { path: '/register-confirmation', name: 'registerConfirmation', component: RegisterConfirmation, meta: { guestOnly: true } },
  { path: '/forgot-password', name: 'forgotPassword', component: ForgotPassword, meta: { guestOnly: true } },

  // Owner Pages
  ...[
    ['dashboard-owner', DashboardOwner],
    ['manage-admins', ManageAdmins],
    ['otp-logs', OtpLogs],
    ['activity-logs', ActivityLogs],
    ['security-panel', SecurityPanel],
    ['settings', SystemSettings],
    ['inject-page', InjectPage],
    ['logs', LogsPage],
    ['shield-page', ShieldPage],
  ].map(([name, component]) => ({
    path: `/${name}`,
    name,
    component,
    meta: { requiresAuth: true, role: 'owner' }
  })),

  // Admin Pages
  { path: '/admin', name: 'adminDashboard', component: AdminDashboard, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/manage-users', name: 'adminManageUsers', component: AdminManageUsers, meta: { requiresAuth: true, role: 'admin' } },
  { path: '/admin/logs', name: 'adminLogs', component: AdminLogsPage, meta: { requiresAuth: true, role: 'admin' } },

  // GPT Tools
  { path: '/vision-console', name: 'visionConsole', component: VisionConsole, meta: { requiresAuth: true, role: 'owner' } },
  { path: '/ai-chatbot', name: 'aiChatbot', component: AIChatBot, meta: { requiresAuth: true, role: 'owner' } },
  { path: '/dream-trigger', name: 'dreamTrigger', component: DreamTrigger, meta: { requiresAuth: true, role: 'owner' } },
  { path: '/kernel-monitor', name: 'kernelMonitor', component: KernelMonitor, meta: { requiresAuth: true, role: 'owner' } },
  { path: '/prompt-history', name: 'promptHistory', component: PromptHistory, meta: { requiresAuth: true, role: 'owner' } },

  // Errors
  { path: '/unauthorized', name: 'notAuthorized', component: NotAuthorized },
  { path: '/:pathMatch(.*)*', name: 'notFound', component: NotFound }
]

// === Router Instance
const router = createRouter({
  history: createWebHistory(),
  routes
})

// === Navigation Guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token')
  const role = localStorage.getItem('user_role')

  // Restrict guest-only pages for authenticated users
  if (to.meta.guestOnly && token) {
    return next({ name: role === 'admin' ? 'adminDashboard' : 'dashboardOwner' })
  }

  // Auth-protected pages
  if (to.meta.requiresAuth) {
    if (!token) return next({ name: 'login' })
    if (to.meta.role && to.meta.role !== role) {
      return next({ name: 'notAuthorized' })
    }
  }

  next()
})

export default router
