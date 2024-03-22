import { createRouter, createWebHistory } from 'vue-router';

// Import the components that will be used in different routes
const Dashboard = () => import('../views/Dashboard.vue');
const Founders = () => import('../views/Founders.vue');
const Startups = () => import('../views/Startups.vue');

// Define routes
const routes = [
  // Redirect to /dashboard as a default route
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', component: Dashboard, name: 'Dashboard' },
  { path: '/founders', component: Founders, name: 'Founders' },
  { path: '/startups', component: Startups, name: 'Startups' },
  { path: '/founders/:name', name: 'founderDetail', component: () => import('../views/FounderDetail.vue') },
  { path: '/startups/:name', name: 'startupDetail', component: () => import('../views/StartupDetail.vue') },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
