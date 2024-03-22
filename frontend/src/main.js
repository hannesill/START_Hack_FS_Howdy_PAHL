import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router
import './output.css';
import { store } from './store';


const app = createApp(App);
app.use(store);
app.use(router)
app.mount('#app');

// TODO: Fix the underlying issue of the cursor not changing to a pointer when hovering over an anchor tag after reloading the page
document.addEventListener('mouseover', (e) => {
  if (e.target.matches('a') || e.target.closest('a')) { // Adjust selector as needed
    e.target.style.cursor = 'pointer';
  }
});