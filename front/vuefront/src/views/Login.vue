<template>
	<div id="login">
		<van-field
			v-model="username"
			name="username"
			label="用户名"
			placeholder="请输入用户名"
		/>
		<van-field
			v-model="password"
			type="password"
			name="password"
			label="密码"
			placeholder="请输入密码"
		/>
		<div style="margin: 16px;">
			<van-button round block type="info" @click="requestToenk">登陆</van-button>
		</div>
</van-form>
		
	</div>
</template>

<script>
export default {
	data() {
		return {
			username: 'jqk1315',
			password: '123456',
			};
		},
	methods: {
		requestToenk() {
			this.$api.getToken({
					username:this.username,
					password:this.password
				}).then(res=>{
					console.log("+++")
				this.$jsCookie.set("refresh",res.data.refresh);
				this.$jsCookie.set("access",res.data.access);
				
			}).catch(err=>{
				console.log("请求失败",err)
			})
			
		},
	  },
};

	
</script>

<style>
	
	
</style>
