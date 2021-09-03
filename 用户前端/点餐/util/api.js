const BASE_URL ='http://8.142.82.195'
export const myRequest = (options) =>{
	return new Promise((resolve,reject)=>{
		uni.request({
			url:BASE_URL+options.url,
			method:options.method || 'GET',
			data:options.data || {},
			success:(res)=>{
				resolve(res)
			},
			fail:(err)=>{
				uni.showToast({
					title:'获取数据失败'
				})
				reject(err)
			}
		})
	})
}

//基本每个页面都用到，则在main.js中引用并挂全局即可