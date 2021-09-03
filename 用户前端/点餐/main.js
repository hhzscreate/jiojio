import Vue from 'vue'
import App from './App'
import store from './store'
//import util from './common/util.js'

import {myRequest} from './util/api.js'
//挂到全局
Vue.prototype.$myRequest=myRequest

Vue.config.productionTip = false

App.mpType = 'app'

Vue.prototype.$store = store
//Vue.prototype.$util = util

const app = new Vue({
	store,
    ...App
})
app.$mount()
