
import jsCookie from 'js-cookie'
import axios from 'axios'


axios.defaults.baseURL = 'http://127.0.0.1:8000'
// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
		console.log(config)
		if(config.headers.Authorization == null){
			config.headers.Authorization = `Bearer ${jsCookie.get('access')}`;
		}
		return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });

var hasRefresh = false
axios.interceptors.response.use(function (response) {
    // Do something with response data
    return response;
  }, function (error) {
    // Do something with response error
	console.log(error.response.status,"==");
	if (error.response.status == 401 && !hasRefresh){
		console.log("授权失败")
		hasRefresh = true
		axios.post("/refresh/",{
			refresh:jsCookie.get('refresh')  
		}).then(res=>{
				hasRefresh = false
				console.log("刷新成功");
				jsCookie.set("access",res.data.access);
				// jsCookie.set("refresh",res.data.access);
				}).catch(err=>{
				console.log("刷新失败");
				jsCookie.remove("refresh");
				jsCookie.remove("access");
				})
		
	}
    return Promise.reject(error);
  });

export const getCategoryList = ()=>{
	// console.log("发起了请求商品列表")
	return axios.get("/api/v1/categorys/")
}
export const createCategory = (params)=>{
	return axios.post("/api/v1/categorys/",params)
}

export const getToken = (params)=>{
	return axios.post("/obtain_token/",params)
}

export const getCategory = (params)=>{
	return axios.get(`/api/v1/categorys/${params.id}/`)
}