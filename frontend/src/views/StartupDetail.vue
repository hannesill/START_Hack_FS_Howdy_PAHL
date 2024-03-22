<template>
  <div>
    <div class="px-4 sm:px-0">
      <button @click="goBack" class="mb-4 inline-flex items-center py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-gray-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        ← Go Back
      </button>
    </div>
    <div class="px-4 pb-4 sm:px-0 flex items-start">
      <!-- Image container -->
      <div class="flex-shrink-0 mr-4">
        <img class="h-24 w-auto rounded-full" :src="startup.logo" alt="Profile picture of the founder">
      </div>
      <!-- Text and icon container -->
      <div class="ml-2">
        <div>
          <h3 class="text-base font-semibold leading-7 text-white">{{ startup.name }}</h3>
          <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-400">
            Founded by
            <span v-for="(founder, index) in startup.founders" :key="founder">
              <router-link :to="{ name: 'founderDetail', params: { name: founder }}" class="text-white">
                {{ founder }}
              </router-link>
              <span v-if="index < startup.founders.length - 1">, </span>
            </span>
          </p>
        </div>
        <div class="mt-4 flex items-center space-x-4">
          <a :href="startup.website" class="text-gray-400 hover:text-white">
            <GlobeAltIcon class="h-5 w-5" />
          </a>
          <a :href="startup.linkedin" class="text-gray-400 hover:text-gray-300" target="_blank" rel="noopener noreferrer">
            <span class="sr-only">LinkedIn</span>
            <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" />
            </svg>
          </a>
        </div>
      </div>
    </div>
    <div class="mt-6A border-t border-white/10">
      <dl class="divide-y divide-white/10">
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Description</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.description }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Address</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.address }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Founding Date</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.founding_date }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Status</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.status }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Phase</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.phase }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Full Time Employees</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.fte }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Equity-free Grants (CHF)</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.equity_free_grants_chf }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Business Model Type</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.business_model_type }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Target Market</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.target_market }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Last Update</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.last_update }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">KPIs</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.kpis }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Last Funding Round</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.last_funding_round }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Last Milestone</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.last_milestone }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Looking for</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ startup.looking_for }}</dd>
        </div>
      </dl>
    </div>
  </div>
</template>

<script setup>
import {useRoute, useRouter} from 'vue-router';
import {GlobeAltIcon} from "@heroicons/vue/20/solid/index.js";
import { computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const route = useRoute();

const startup = computed(() => {
  // Use a default empty object to avoid undefined errors
  return store.getters.getStartupByName(route.params.name) || {};
});

const router = useRouter();

const goBack = () => {
  router.go(-1); // This navigates one step back in the browser history
};
</script>
