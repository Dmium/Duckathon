import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import Axios from 'axios'
require('./assets/styles/custom.scss');
import VueBootstrapTypeahead from 'vue-bootstrap-typeahead'

Vue.use(BootstrapVue)
Vue.component('vue-bootstrap-typeahead', VueBootstrapTypeahead)
Vue.config.productionTip = false
Vue.prototype.$http = Axios.create({
    withCredentials: true,
    baseURL: 'http://localhost:8000/',
})
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')