<template>
  <div class="px-2 sm:px-6 lg:px-2 lg:pr-96">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-white">Batch Analytics</h1>
        <p class="mt-2 text-sm text-gray-400">A list of the recent START Fellowship batches and their KPIs</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <!-- Sort dropdown -->
      <Menu as="div" class="relative">
        <MenuButton class="flex items-center gap-x-1 text-sm font-medium leading-6 text-white">
          Sort by
          <ChevronUpDownIcon class="h-5 w-5 text-gray-500" aria-hidden="true" />
        </MenuButton>
        <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
          <MenuItems class="absolute right-0 z-10 mt-2.5 w-40 origin-top-right rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 focus:outline-none">
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-50' : '', 'block px-3 py-1 text-sm leading-6 text-gray-900']">Date</a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-50' : '', 'block px-3 py-1 text-sm leading-6 text-gray-900']">Batch size</a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-50' : '', 'block px-3 py-1 text-sm leading-6 text-gray-900']">Funding</a>
            </MenuItem>
          </MenuItems>
        </transition>
      </Menu>
      </div>
    </div>

    <div class="mt-6">
      <!-- Heading -->
      <div class="flex flex-col items-start justify-between gap-x-8 gap-y-4 bg-gray-700/10 px-4 py-4 sm:flex-row sm:items-center sm:px-6 lg:px-8">
        <div>
          <div class="flex items-center gap-x-3">
            <div class="flex-none rounded-full bg-red-400/10 p-1 text-red-400">
              <div class="h-2 w-2 rounded-full bg-current" />
            </div>
            <h1 class="flex gap-x-3 text-base leading-7">
              <span class="font-semibold text-white">FS Batch Winter 2023</span>
              <span class="text-gray-600">/</span>
              <span class="font-semibold text-white">#16</span>
            </h1>
          </div>
          <p class="mt-2 text-xs leading-6 text-gray-400">"Many AI startups this batch"</p>
        </div>
        <div class="order-first flex-none rounded-full bg-indigo-200/20 px-2 py-1 text-xs font-medium text-indigo-400 ring-1 ring-inset ring-indigo-500/30 sm:order-none">Accelerator Boost</div>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-1 bg-gray-700/10 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="(stat, statIdx) in stats3" :key="stat.name" :class="[statIdx % 2 === 1 ? 'sm:border-l' : statIdx === 2 ? 'lg:border-l' : '', 'border-t border-white/5 py-6 px-4 sm:px-6 lg:px-6']">
          <p class="text-sm font-medium leading-6 text-gray-400">{{ stat.name }}</p>
          <p class="mt-2 flex items-baseline gap-x-2">
            <span class="text-4xl font-semibold tracking-tight text-white">{{ stat.value }}</span>
            <span v-if="stat.unit" class="text-sm text-gray-400">{{ stat.unit }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="mt-6">
      <!-- Heading -->
      <div class="flex flex-col items-start justify-between gap-x-8 gap-y-4 bg-gray-700/10 px-4 py-4 sm:flex-row sm:items-center sm:px-6 lg:px-8">
        <div>
          <div class="flex items-center gap-x-3">
            <div class="flex-none rounded-full bg-green-400/10 p-1 text-green-400">
              <div class="h-2 w-2 rounded-full bg-current" />
            </div>
            <h1 class="flex gap-x-3 text-base leading-7">
              <span class="font-semibold text-white">FS Batch Autumn 2023</span>
              <span class="text-gray-600">/</span>
              <span class="font-semibold text-white">#15</span>
            </h1>
          </div>
          <p class="mt-2 text-xs leading-6 text-gray-400">"Very diverse participants"</p>
        </div>
        <div class="order-first flex-none rounded-full bg-amber-200/20 px-2 py-1 text-xs font-medium text-amber-500 ring-1 ring-inset ring-amber-500/30 sm:order-none">Accelerator Ignite</div>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-1 bg-gray-700/10 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="(stat, statIdx) in stats2" :key="stat.name" :class="[statIdx % 2 === 1 ? 'sm:border-l' : statIdx === 2 ? 'lg:border-l' : '', 'border-t border-white/5 py-6 px-4 sm:px-6 lg:px-6']">
          <p class="text-sm font-medium leading-6 text-gray-400">{{ stat.name }}</p>
          <p class="mt-2 flex items-baseline gap-x-2">
            <span class="text-4xl font-semibold tracking-tight text-white">{{ stat.value }}</span>
            <span v-if="stat.unit" class="text-sm text-gray-400">{{ stat.unit }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="mt-6">
      <!-- Heading -->
      <div class="flex flex-col items-start justify-between gap-x-8 gap-y-4 bg-gray-700/10 px-4 py-4 sm:flex-row sm:items-center sm:px-6 lg:px-8">
        <div>
          <div class="flex items-center gap-x-3">
            <div class="flex-none rounded-full bg-green-400/10 p-1 text-green-400">
              <div class="h-2 w-2 rounded-full bg-current" />
            </div>
            <h1 class="flex gap-x-3 text-base leading-7">
              <span class="font-semibold text-white">FS Batch Summer 2023</span>
              <span class="text-gray-600">/</span>
              <span class="font-semibold text-white">#14</span>
            </h1>
          </div>
          <p class="mt-2 text-xs leading-6 text-gray-400">"Strong attendance from Latin America"</p>
        </div>
        <div class="order-first flex-none rounded-full bg-pink-200/20 px-2 py-1 text-xs font-medium text-pink-500 ring-1 ring-inset ring-pink-500/30 sm:order-none">Incubator</div>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-1 bg-gray-700/10 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="(stat, statIdx) in stats1" :key="stat.name" :class="[statIdx % 2 === 1 ? 'sm:border-l' : statIdx === 2 ? 'lg:border-l' : '', 'border-t border-white/5 py-6 px-4 sm:px-6 lg:px-6']">
          <p class="text-sm font-medium leading-6 text-gray-400">{{ stat.name }}</p>
          <p class="mt-2 flex items-baseline gap-x-2">
            <span class="text-4xl font-semibold tracking-tight text-white">{{ stat.value }}</span>
            <span v-if="stat.unit" class="text-sm text-gray-400">{{ stat.unit }}</span>
          </p>
        </div>
      </div>
    </div>

  </div>

  <!-- Activity feed -->
  <aside class="bg-black/10 lg:fixed lg:bottom-0 lg:right-0 lg:top-2 lg:w-96 lg:overflow-y-auto lg:border-l lg:border-white/5">
    <header class="flex items-center justify-between border-b border-white/5 px-4 py-4 sm:px-6 sm:py-6 lg:px-8">
      <h2 class="text-base font-semibold leading-7 text-white">Activity feed</h2>
      <a href="#" class="text-sm font-semibold leading-6 text-indigo-400">View all</a>
    </header>
    <ul role="list" class="divide-y divide-white/5">
      <li v-for="item in activityItems" :key="item.commit" class="px-4 py-4 sm:px-6 lg:px-8">
        <div class="flex items-center gap-x-3">
          <img :src="item.user.imageUrl" alt="" class="h-6 w-6 flex-none rounded-full bg-gray-800" />
          <h3 class="flex-auto truncate text-sm font-semibold leading-6 text-white">{{ item.user.name }}</h3>
          <time :datetime="item.dateTime" class="flex-none text-xs text-gray-600">{{ item.date }}</time>
        </div>
        <p class="mt-3 truncate text-sm text-gray-500">
          Changed <span class="text-gray-400">{{ item.companyName }}</span> (<span class="font-mono text-gray-400">{{ item.attribute }}</span> to <span class="text-gray-400">{{ item.new_value }}</span
          >)
        </p>
      </li>
    </ul>
  </aside>
</template>

<script setup>
import { ref } from 'vue'
import {
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Listbox,
  ListboxOption,
  ListboxLabel,
  ListboxOptions,
  ListboxButton
} from '@headlessui/vue'
import {
  FaceSmileIcon, XMarkIcon
} from '@heroicons/vue/24/outline'
import {ChevronUpDownIcon, FaceFrownIcon, FireIcon, HandThumbUpIcon, HeartIcon, PaperClipIcon} from '@heroicons/vue/20/solid'

const moods = [
  { name: 'Excited', value: 'excited', icon: FireIcon, iconColor: 'text-white', bgColor: 'bg-red-500' },
  { name: 'Loved', value: 'loved', icon: HeartIcon, iconColor: 'text-white', bgColor: 'bg-pink-400' },
  { name: 'Happy', value: 'happy', icon: FaceSmileIcon, iconColor: 'text-white', bgColor: 'bg-green-400' },
  { name: 'Sad', value: 'sad', icon: FaceFrownIcon, iconColor: 'text-white', bgColor: 'bg-yellow-400' },
  { name: 'Thumbsy', value: 'thumbsy', icon: HandThumbUpIcon, iconColor: 'text-white', bgColor: 'bg-blue-500' },
  { name: 'I feel nothing', value: null, icon: XMarkIcon, iconColor: 'text-gray-400', bgColor: 'bg-transparent' },
]

const selected = ref(moods[5])

const activityItems = [
  {
    user: {
      name: 'Michael Foster',
      imageUrl: 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Freoa Health',
    attribute: 'fte',
    new_value: '31',
    date: '1h',
    dateTime: '2023-01-23T11:00',
  },
  {
    user: {
      name: 'Samantha Bloom',
      imageUrl: 'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Orbit AI',
    attribute: 'looking for',
    new_value: 'co-founder',
    date: '2h',
    dateTime: '2023-01-23T10:00',
  },
  {
    user: {
      name: 'Carlos Henrique',
      imageUrl: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Tech Innovate',
    attribute: 'last funding round',
    new_value: 'Sep 2023, 2M$',
    date: '3h',
    dateTime: '2023-01-23T09:00',
  },
  {
    user: {
      name: 'Ayesha Malik',
      imageUrl: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'GreenTech Solutions',
    attribute: 'fte',
    new_value: '75',
    date: '5h',
    dateTime: '2023-01-23T07:00',
  },
  {
    user: {
      name: 'John Doe',
      imageUrl: 'https://images.unsplash.com/photo-1563132337-f159f484226c?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Freoa Health',
    attribute: 'address',
    new_value: 'Berlin',
    date: '8h',
    dateTime: '2023-01-23T04:00',
  },
  {
    user: {
      name: 'Linda Smith',
      imageUrl: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Global Dynamics',
    attribute: 'kpis',
    new_value: '$1M ARR',
    date: '1d',
    dateTime: '2023-01-22T11:00',
  },
  {
    user: {
      name: 'Marco Polo',
      imageUrl: 'https://images.unsplash.com/photo-1524502397800-2eeaad7c3fe6?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Historic Ventures',
    attribute: 'target market',
    new_value: 'Asian production',
    date: '2d',
    dateTime: '2023-01-21T11:00',
  },
  {
    user: {
      name: 'Emma Clarke',
      imageUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
    companyName: 'Creative Solutions',
    attribute: 'milestone',
    new_value: 'product launch',
    date: '3d',
    dateTime: '2023-01-20T09:00',
  }
];


const stats1 = [
  { name: 'Number of partcipants', value: '31' },
  { name: 'Amount of funding raised', value: '50', unit: 'k $' },
  { name: 'Number of teams', value: '12' },
  { name: 'Startups\' Survival rate', value: '63.5%' },
]

const stats2 = [
  { name: 'Number of partcipants', value: '28' },
  { name: 'Amount of funding raised', value: '117', unit: 'k $' },
  { name: 'Number of teams', value: '10' },
  { name: 'Startups\' Survival rate', value: '73.5%' },
]

const stats3 = [
  { name: 'Number of partcipants', value: '27' },
  { name: 'Amount of funding raised', value: '280', unit: 'k $' },
  { name: 'Number of teams', value: '11' },
  { name: 'Startups\' Survival rate', value: '94.5%' },
]

</script>