<template>
  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="open = false">
      <div class="fixed inset-0 bg-gray-900 bg-opacity-50" />

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
            <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
              <DialogPanel class="pointer-events-auto w-screen max-w-md">
                <div class="flex h-full flex-col overflow-y-scroll bg-gray-800 py-6 shadow-xl">
                  <div class="px-4 sm:px-6">
                    <div class="flex items-start justify-between">
                      <DialogTitle class="text-lg font-semibold leading-6 text-white">Panel title</DialogTitle>
                      <div class="ml-3 flex h-7 items-center">
                        <button type="button" class="relative rounded-md bg-gray-800 text-gray-400 hover:text-gray-300 focus:outline-none" @click="open = false">
                          <span class="sr-only">Close panel</span>
                          <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                        </button>
                      </div>
                    </div>
                  </div>
                  <div class="relative mt-6 flex-1 px-4 sm:px-6">
                    <!-- Filter Form -->
                    <form id="filterForm" @submit.prevent="applyFilters">
                      <div class="grid grid-cols-1 gap-4">
                        <div>
                          <label for="name" class="block text-sm font-medium text-gray-300">Name</label>
                          <input type="text" id="name" v-model="filters.name" class="mt-1 block w-full rounded-md bg-gray-700 border-transparent focus:border-indigo-500 focus:bg-gray-600 focus:ring-0 text-white sm:text-sm">
                        </div>
                        <div>
                          <label for="professionalExperience" class="block text-sm font-medium text-gray-300">Professional Experience</label>
                          <input type="text" id="professionalExperience" v-model="filters.professionalExperience" class="mt-1 block w-full rounded-md bg-gray-700 border-transparent focus:border-indigo-500 focus:bg-gray-600 focus:ring-0 text-white sm:text-sm">
                        </div>
                        <div>
                          <label for="education" class="block text-sm font-medium text-gray-300">Education</label>
                          <input type="text" id="education" v-model="filters.education" class="mt-1 block w-full rounded-md bg-gray-700 border-transparent focus:border-indigo-500 focus:bg-gray-600 focus:ring-0 text-white sm:text-sm">
                        </div>
                        <!-- Add more filters as needed -->
                      </div>
                      <div class="mt-4">
                        <button type="submit" class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                          Apply Filters
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold leading-6">Founders</h1>
        <p class="mt-2 text-sm text-gray-400">A list of all the founders in the START Fellowship database.</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <button @click="toggleSlideOver" type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Filter</button>
      </div>
    </div>
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <table class="min-w-full divide-y divide-gray-300">
            <thead>
              <tr>
                <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold sm:pl-0">Name</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Professional Experience</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Education</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Status</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold">Role</th>
                <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                  <span class="sr-only">Edit</span>
                </th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold"></th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-400">
              <tr v-for="founder in enrichedFounders" :key="founder.name">
                <td class="whitespace-nowrap py-5 pl-4 pr-3 text-sm sm:pl-0">
                  <div class="flex items-center">
                    <div class="h-11 w-11 flex-shrink-0">
                      <img class="h-11 w-11 rounded-full" :src="founder.image" alt="" />
                    </div>
                    <div class="ml-4 cursor-pointer" @click="goToFounder(founder.name)">
                      <div class="font">{{ founder.name }}</div>
                      <div class="mt-1 text-gray-400">{{ founder.email }}</div>
                    </div>
                  </div>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm">
                  <div>{{ founder.professional_experience_job }}</div>
                  <div class="mt-1 text-gray-400">{{ founder.professional_experience_company }}</div>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm">
                  <div>{{ founder.education_degree }}</div>
                  <div class="mt-1 text-gray-400">{{ founder.education_school }}</div>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-400">
                  <span class="inline-flex items-center rounded-md bg-green-400 px-2 py-1 text-xs font-medium text-green-800 ring-1 ring-inset ring-green-600/20">Active</span>
                </td>
                <td class="whitespace-nowrap px-3 py-5 text-sm text-gray-400">{{ founder.role }}</td>
                <td class="relative whitespace-nowrap py-5 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                  <a :href="founder.linkedin" class="text-gray-400 hover:text-gray-300" target="_blank" rel="noopener noreferrer">
                    <span class="sr-only">LinkedIn</span>
                    <svg class="h-5 w-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.338 16.338H13.67V12.16c0-.995-.017-2.277-1.387-2.277-1.39 0-1.601 1.086-1.601 2.207v4.248H8.014v-8.59h2.559v1.174h.037c.356-.675 1.227-1.387 2.526-1.387 2.703 0 3.203 1.778 3.203 4.092v4.711zM5.005 6.575a1.548 1.548 0 11-.003-3.096 1.548 1.548 0 01.003 3.096zm-1.337 9.763H6.34v-8.59H3.667v8.59zM17.668 1H2.328C1.595 1 1 1.581 1 2.298v15.403C1 18.418 1.595 19 2.328 19h15.34c.734 0 1.332-.582 1.332-1.299V2.298C19 1.581 18.402 1 17.668 1z" clip-rule="evenodd" />
                    </svg>
                  </a>
                </td>
                <td class="relative whitespace-nowrap py-5 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
                  <span :class="`inline-flex items-center rounded-md bg-orange-400/20 border border-orange-300 px-2 py-1 text-xs font-medium text-white`">
                    🔥 {{ founder.flames }}
                  </span>
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
import {computed, onMounted, reactive, ref} from 'vue'
import {useStore} from "vuex";
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const filters = reactive({
  name: '',
  professionalExperience: '',
  education: '',
  // Add more attributes as needed
})

const router = useRouter();
const store = useStore();

// Computed property to get all founders from the store
const founders = computed(() => store.getters.getAllFounders);

// Method to fetch all founders from the API and update the store
function loadFounders() {
  store.dispatch('fetchFounders');
}

// Fetch all founders when the component is mounted
onMounted(loadFounders);

function goToFounder(name) {
  router.push(`/founders/${name}`);
}
function toggleSlideOver() {
  open.value = !open.value;
}

function applyFilters() {
  // Logic to apply filters based on `filters` object
  // This might involve fetching filtered data or filtering an existing list
  console.log('Applying filters:', filters)

  // Optionally close the slide-over after applying filters
  open.value = false
}

// Method to generate random flames (1 to 5) for each founder
const getRandomFlames = () => Math.floor(Math.random() * 5) + 1;

// Add a computed property to enrich founders with random flames
const enrichedFounders = computed(() => {
  return founders.value.map(founder => ({
    ...founder,
    flames: getRandomFlames(),
  }));
});

</script>