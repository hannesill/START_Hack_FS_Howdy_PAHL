<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold leading-6">Startups</h1>
        <p class="mt-2 text-sm text-gray-400">A list of all the startups in the START Fellowship database.</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Filter</button>
      </div>
    </div>
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <table class="min-w-full divide-y divide-gray-300">
            <thead>
              <tr>
                <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold sm:pl-0">Name</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Description</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Status</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Business Model</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Phase</th>
                <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-400">
              <tr v-for="startup in startups" :key="startup.id">
                <td class="whitespace-nowrap py-5 pl-4 pr-3 text-sm sm:pl-0">
                  <div class="flex items-center">
                    <div class="h-11 w-11 flex-shrink-0">
                      <img class="h-11 w-11 rounded-full" :src="startup.logo" alt="" />
                    </div>
                    <div class="ml-4 cursor-pointer" @click="goToStartup(startup.name)">
                      <div class="font">{{ startup.name }}</div>
                      <div class="mt-1 text-gray-400">
                        <span v-for="(founder, index) in startup.founders" :key="founder">
                          {{ founder }}<span v-if="index < startup.founders.length - 1">, </span>
                        </span>
                      </div>
                    </div>
                  </div>
                </td>
                <td class="whitespace-normal break-words px-3 py-5 text-sm">
                  <div class="mt-1 text-gray-400">{{ startup.description }}</div>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-400">
                  <span class="inline-flex items-center rounded-md bg-green-400 px-2 py-1 text-xs font-medium text-green-800 ring-1 ring-inset ring-green-600/20">Active</span>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm">
                  <div class="mt-1 text-gray-400">{{ startup.business_model_type }}</div>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-400">{{ startup.phase }}</td>
                <td class="relative whitespace-nowrap py-5 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                  <a :href="startup.linkedin" class="text-gray-400 hover:text-gray-300" target="_blank" rel="noopener noreferrer">
                    <span class="sr-only">LinkedIn</span>
                    <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" />
                    </svg>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import {computed, onMounted} from 'vue';
import { useStore } from 'vuex';

const store = useStore();

// Computed property to get all founders from the store
const startups = computed(() => store.getters.getAllStartups);

// Method to fetch all founders from the API and update the store
function loadStartups() {
  store.dispatch('fetchStartups');
}

// Fetch all founders when the component is mounted
onMounted(loadStartups);

const router = useRouter();

function goToStartup(name) {
  router.push(`/startups/${name}`);
}

</script>