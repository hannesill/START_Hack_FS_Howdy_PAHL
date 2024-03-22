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
        <img class="h-24 w-auto rounded-full" :src="founder.image" alt="Profile picture of the founder">
      </div>
      <!-- Text and icon container -->
      <div class="ml-2">
        <div>
          <h3 class="text-base font-semibold leading-7 text-white">{{ founder.name }}</h3>
          <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-400">
            {{ founder.role }} @
            <router-link :to="{ name: 'startupDetail', params: { name: founder.name }}" class="text-white">
              {{ founder.name }}
            </router-link>
          </p>
        </div>
        <div class="mt-4 flex items-center space-x-4">
          <a :href="`mailto:${founder.email}`" class="text-gray-400 hover:text-white">
            <EnvelopeIcon class="h-5 w-5" />
          </a>
          <a :href="`tel:${founder.phone}`" class="text-gray-400 hover:text-white">
            <PhoneIcon class="h-5 w-5" />
          </a>
          <a :href="founder.linkedin" class="text-gray-400 hover:text-gray-300" target="_blank" rel="noopener noreferrer">
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
          <dt class="text-sm font-medium leading-6 text-white">Address</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.address }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Birthdate</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.birthdate }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Cofounders</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">
            Test, Test
          </dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Skills</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.skills }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Role</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.role }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Education</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.education_degree }} @{{ founder.education_school }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Professional Experience</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.professional_experience_job}} @{{ founder.professional_experience_company }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">About</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">Fugiat ipsum ipsum deserunt culpa aute sint do nostrud anim incididunt cillum culpa consequat. Excepteur qui ipsum aliquip consequat sint. Sit id mollit nulla mollit nostrud in ea officia proident. Irure nostrud pariatur mollit ad adipisicing reprehenderit deserunt qui eu.</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-white">Last Update</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-400 sm:col-span-2 sm:mt-0">{{ founder.last_update }}</dd>
        </div>
      </dl>
    </div>
  </div>
</template>

<script setup>
import {computed, onMounted} from 'vue';
import {useRoute, useRouter} from 'vue-router';
import { useStore } from 'vuex';
import { EnvelopeIcon, PhoneIcon } from '@heroicons/vue/20/solid'

const store = useStore();
const route = useRoute();
const router = useRouter();

const goBack = () => {
  router.go(-1); // This navigates one step back in the browser history
};

const founder = computed(() => {
  return store.getters.getFounderByName(route.params.name);
});

// Computed property to get all founders from the store
const founders = computed(() => store.getters.getAllFounders);

// Method to fetch all founders from the API and update the store
function loadFounders() {
  store.dispatch('fetchFounders');
}

// Fetch all founders when the component is mounted
onMounted(loadFounders);

</script>
