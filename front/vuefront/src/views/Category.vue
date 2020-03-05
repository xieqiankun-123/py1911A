<template>
	<div v-if="category">
		<van-nav-bar
		  :title="'这里是分类详情页'+category.id"
		  left-text="返回"
		  left-arrow
		  @click-left="onClickLeft"
		/>
		
		<span>这里是分类详情页{{$route.params.id}}</span>
		<div >
			
			<b>商品ID:</b><span v-text="category.id" ></span><br>
			<b>商品名:</b><span v-text="category.name" ></span><br>
			<div id="goods" >
				<van-cell :title="item.name" v-for="(item,index) in category.goods" is-link/>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		data(){
			return{
				category:null
			}
		},
		created() {
			this.$api.getCategory({
				id:this.$route.params.id
			}).then(res=>{
				console.log(res)
				this.category = res.data
			}).catch(err=>{
				console.log("出错了",err)
				
			})
			console.log("_____欢迎来到分类页面_____")
		},
		methods:{
			onClickLeft(){
				this.$router.go(-1)
			}
			
		}
		
		
	}
	
</script>

<style>
</style>
