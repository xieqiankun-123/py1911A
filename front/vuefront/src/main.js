import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vant from 'vant';
import 'vant/lib/index.css';
Vue.use(Vant);
// 注册axios
// import axios from 'axios';
// Vue.prototype.$http=axios;

Vue.config.productionTip = false
import * as api from './api/api.js'
Vue.prototype.$api = api;

// 将js-cookie注册进原型
import jsCookie from 'js-cookie'
Vue.prototype.$jsCookie = jsCookie;



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
