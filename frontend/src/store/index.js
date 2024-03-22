import { createStore } from 'vuex';
import axios from 'axios';

export const store = createStore({
  state() {
    return {
      startups: [],
      founders: [],
    };
  },
  mutations: {
    setFounders(state, founders) {
      state.founders = founders;
    },
    setStartups(state, startups) {
      state.startups = startups;
    },
    addFounder(state, founder) {
      state.founders.push(founder);
    },
    addStartup(state, startup) {
      state.startups.push(startup);
    },
  },
  actions: {
    fetchFounders({ commit }) {
      axios.get('http://localhost:8000/founders/')
        .then(response => {
          commit('setFounders', response.data);
        })
        .catch(error => console.error(error));
    },
    fetchStartups({ commit }) {
      axios.get('http://localhost:8000/startups/')
        .then(response => {
          commit('setStartups', response.data);
        })
        .catch(error => console.error(error));
    },
    fetchFounderByName({ commit }, name) {
      axios.get(`http://localhost:8000/founders/${name}`)
        .then(response => {
          commit('addFounder', response.data);
        })
        .catch(error => console.error(error));
    },
    fetchStartupByName({ commit }, name) {
      axios.get(`http://localhost:8000/startups/${name}`)
        .then(response => {
          commit('addStartup', response.data);
        })
        .catch(error => console.error(error));
    },
  },
  getters: {
    getAllFounders: (state) => state.founders,
    getFounderByName: (state) => (name) => {
      return state.founders.find(founder => founder.name === name);
    },
    getAllStartups: (state) => state.startups,
    getStartupByName: (state) => (name) => {
      return state.startups.find(startup => startup.name === name);
    }
  },
});
