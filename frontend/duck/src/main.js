import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import Axios from 'axios'
require('./assets/styles/custom.scss');

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$http = Axios.create({
    withCredentials: true,
})
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')