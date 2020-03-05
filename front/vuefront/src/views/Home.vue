<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png"><br>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
		<!-- <button @click="requestCategory" >发起请求商品列表</button> -->
		<br>
		<div id="categorys" >
			<van-cell :title="item.name" :to="'/category/'+item.id+'/'" v-for="(item,index) in categorys" is-link/>
		</div>
		<div id="createCategory" >
			<van-form @submit="requestCreateCategory">
				<van-field
					v-model="categoryName"
					name="categoryName"
					label="分类名"
					placeholder="请输入分类名"
				/>
				<div style="margin: 16px;">
					<van-button round block type="info" native-type="submit">
						提交
					</van-button>
				</div>
			</van-form>
			
		</div>
		<!-- <label for="">用户名</label> <input type="text" v-model="username"><br>
		<label for="">密码</label> <input type="text" v-model="password"><br>
		<button @click="requestToken" >发起请求Token</button><br>
		<label for="">商品名</label> <input type="text" v-model="categoryName"><br>
		<button @click="requestCreateCategory" >发起请求创建商品</button><br> -->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
	data(){
		return {
			categoryName:"",
			username:'jqk1315',
			password:'123456',
			categorys:[],
		}
	},
	created() {
		this.$api.getCategoryList().then(res=>{
			console.log(res)
			this.categorys = res.data
		}).catch(err=>{
			console.log(err)
		})
	},
	methods:{
		requestCategory(){
			this.$api.getCategoryList().then(res=>{
				console.log(res)
			}).catch(err=>{
				console.log(err)
			})
		},
		requestCreateCategory(){
			console.log("+++")
			if (this.categoryName != ""){
				this.$api.createCategory({
					name:this.categoryName
				}).then(res=>{
					console.log("创建成功",res)
					this.categorys.push(res.data)
					this.categoryName = ""
				}).catch(err=>{
					console.log("出错了111",err)
				})
				// this.$http({
// 					method:'post',
// 					url:'http://127.0.0.1:8000/api/v1/categorys/',
// 					data:{
// 						name:this.categoryName,
// 					},
// 					headers:{
// 						Authorization:"Basic anFrMTMxNToxMjM0NTY="}
// 					}).then(res=>{
// 						console.log("+++",res)
// 						
// 					}).catch(err=>{
// 						console.log("出错了",err)
// 					})
				
			}
			else{
				console.log("分类名不能为空")
			}
			
				
				
			
			
		}
		
	}
}
</script>
