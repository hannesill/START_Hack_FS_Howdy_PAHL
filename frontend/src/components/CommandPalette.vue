<template>
  <TransitionRoot :show="open" as="template" @after-leave="query = ''" appear>
    <Dialog as="div" class="relative z-100" @close="open = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-25 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-100 w-screen overflow-y-auto p-4 sm:p-6 md:p-20">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="ease-in duration-200" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
          <DialogPanel class="mx-auto max-w-3xl transform divide-y divide-gray-100 overflow-hidden rounded-xl bg-white shadow-2xl ring-1 ring-black ring-opacity-5 transition-all">
            <Combobox v-slot="{ activeOption }" @update:modelValue="onSelect">
              <div class="relative">
                <MagnifyingGlassIcon class="pointer-events-none absolute left-4 top-3.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                <ComboboxInput class="h-12 w-full border-0 bg-transparent pl-11 pr-4 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm" placeholder="Search..." @change="query = $event.target.value" />
              </div>

              <ComboboxOptions v-if="query === '' || filteredPeople.length > 0" class="flex transform-gpu divide-x divide-gray-100" as="div" static hold>
                <div :class="['max-h-96 min-w-0 flex-auto scroll-py-4 overflow-y-auto px-6 py-4', activeOption && 'sm:h-96']">
                  <h2 v-if="query === ''" class="mb-4 mt-2 text-xs font-semibold text-gray-500">Recent searches</h2>
                  <div hold class="-mx-2 text-sm text-gray-700">
                    <ComboboxOption v-for="person in query === '' ? recent : filteredPeople" :key="person.id" :value="person" as="template" v-slot="{ active }">
                      <div :class="['group flex cursor-default select-none items-center rounded-md p-2', active && 'bg-gray-100 text-gray-900']">
                        <img :src="person.image" alt="" class="h-6 w-6 flex-none rounded-full" />
                        <span class="ml-3 flex-auto truncate">{{ person.name }}</span>
                        <ChevronRightIcon v-if="active" class="ml-3 h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                      </div>
                    </ComboboxOption>
                  </div>
                </div>

                <div v-if="activeOption" class="hidden h-96 w-1/2 flex-none flex-col divide-y divide-gray-100 overflow-y-auto sm:flex">
                  <div class="flex-none p-6 text-center">
                    <img :src="activeOption.image" alt="" class="mx-auto h-16 w-16 rounded-full" />
                    <h2 class="mt-3 font-semibold text-gray-900">
                      {{ activeOption.name }}
                    </h2>
                    <p class="text-sm leading-6 text-gray-500">{{ activeOption.role }}</p>
                  </div>
                  <div class="flex flex-auto flex-col justify-between p-6">
                    <dl class="grid grid-cols-1 gap-x-6 gap-y-3 text-sm text-gray-700">
                      <dt class="col-end-1 font-semibold text-gray-900">Phone</dt>
                      <dd>{{ activeOption.phone }}</dd>
                      <dt class="col-end-1 font-semibold text-gray-900">LinkedIn</dt>
                      <dd class="truncate">
                        <a :href="activeOption.linkedin" class="text-indigo-600 underline">
                          {{ activeOption.linkedin }}
                        </a>
                      </dd>
                      <dt class="col-end-1 font-semibold text-gray-900">Email</dt>
                      <dd class="truncate">
                        <a :href="`mailto:${activeOption.email}`" class="text-indigo-600 underline">
                          {{ activeOption.email }}
                        </a>
                      </dd>
                    </dl>
                    <button @click="visitPage" type="button" class="mt-6 w-full rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Visit Page</button>
                  </div>
                </div>
              </ComboboxOptions>

              <div v-if="query !== '' && filteredPeople.length === 0" class="px-6 py-14 text-center text-sm sm:px-14">
                <UsersIcon class="mx-auto h-6 w-6 text-gray-400" aria-hidden="true" />
                <p class="mt-4 font-semibold text-gray-900">No people found</p>
                <p class="mt-2 text-gray-500">We couldn’t find anything with that term. Please try again.</p>
              </div>
            </Combobox>
          </DialogPanel>
        </TransitionChild>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import {onMounted, onBeforeUnmount, ref, computed} from 'vue';
import { MagnifyingGlassIcon, ChevronRightIcon, UsersIcon } from '@heroicons/vue/24/outline';
import { Combobox, ComboboxInput, ComboboxOptions, ComboboxOption, Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue';
import {useStore} from "vuex";
import {useRouter} from "vue-router";

const store = useStore()
// Computed properties to get all founders & startups from the store
const founders = computed(() => store.getters.getAllFounders);
const startups = computed(() => store.getters.getAllStartups);

// Methods to fetch all founders & startups from the API and update the store
function loadFounders() {
  store.dispatch('fetchFounders');
}
function loadStartups() {
  store.dispatch('fetchStartups');
}

// Fetch all founders & startups when the component is mounted
onMounted(loadFounders);
onMounted(loadStartups);

const recent = [];
const open = ref(false); // Controls the visibility of the command palette
const query = ref('');

const filteredPeople = computed(() => {
  if (query.value === '') {
    return [];
  } else {
    // Access the array with founders.value before filtering
    return founders.value.filter(founder =>
      founder.name.toLowerCase().includes(query.value.toLowerCase())
    );
  }
});

function onSelect(person) {

}

// Add event listeners for keyboard shortcuts
onMounted(() => {
  document.addEventListener('keydown', handleKeydown);
});

onBeforeUnmount(() => {
  document.removeEventListener('keydown', handleKeydown);
});

function handleKeydown(event) {
  console.log(`Key pressed: ${event.key}, Meta: ${event.metaKey}, Ctrl: ${event.ctrlKey}`);
  // For macOS, 'metaKey' is true if the command key is pressed
  // For Windows/Linux, you might want to check for 'ctrlKey' as well
  const isCmdO = (event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k';

  if (isCmdO) {
    event.preventDefault(); // Prevent the default browser action (e.g., open file dialog)
    open.value = !open.value; // Toggle the command palette visibility
  } else if (event.key === 'Escape') {
    open.value = false; // Close the command palette
  }
}

const router = useRouter();

const visitPage = () => {
  router.push('/founders/Alex%20Smith');
  open.value = false;
};

</script>