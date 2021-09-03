<template>
	<view class="content">
		
		<view class="input-group">
			<view class="input-row border">
				<text class="title">账号：</text>
				<m-input type="text" clearable v-model="userId" placeholder="请输入账号"></m-input>
			</view>
			<view class="input-row border">
				<text class="title">密码：</text>
				<m-input type="password" displayable v-model="password" placeholder="请输入密码"></m-input>
			</view>
			
			
		</view>
		
		<view class="btn-row">
			<!-- <button type="primary" class="primary" :loading="loginBtnLoading" @tap="bindLogin">登录</button> -->
			<button type="primary" class="primary" @tap="Login">登录</button>
		</view>
		
		
		<view class="action-row">
			<navigator url="../reg/reg">注册账号</navigator>
		</view>
	</view>
</template>

<script>
	import mInput from '../../components/m-input.vue'
	export default {
		components: {
			mInput
		},
		data(){
			return{
				password:'',
				userId:''
			}
			
		},
		methods:{
			async Login(){//保存数据并跳转
				const res=await this.$myRequest({
					url:'/logintest/',
					data:{
						"userId": this.userId, //同上
						"password":this.password
					}
				})
				// console.log(res.data.data)
				//可以在response的msg里面判断是否成功
				// console.log(res)
				if(res.data.status){
					//设置全局登录变量
					getApp().globalData.isLogin=true
					///getApp().globalData.userInfo=res.data.data
					getApp().globalData.openId=res.data.data[0].userId
					getApp().globalData.userId=res.data.data[0].userId
					getApp().globalData.userName=res.data.data[0].userName		
					//返回上一级页面
					var pages = getCurrentPages();
					var prevPage = pages[pages.length - 2]; //上一个页面
					prevPage.closeLoginPopup()
					//console.log(getApp().globalData.isLogin)
					uni.navigateBack({
						url: '/pages/my/my'
					})
					
				}
				else{//可以弹出提醒框
					uni.showModal({
						title: '提示',
						content: '密码错误或账号错误，请重试',
						showCancel: false
					})
					return
				}
				
			}
		}
	}
</script>

<style>
	m-input {
		width: 100%;
		/* min-height: 100%; */
		display: flex;
		flex: 1;
	}
	
	.content {
		display: flex;
		flex: 1;
		flex-direction: column;
		background-color: #efeff4;
		padding: 10px;
	}
	
	.input-group {
		background-color: #ffffff;
		margin-top: 20px;
		position: relative;
	}
	
	.input-group::before {
		position: absolute;
		right: 0;
		top: 0;
		left: 0;
		height: 1px;
		content: '';
		-webkit-transform: scaleY(.5);
		transform: scaleY(.5);
		background-color: #c8c7cc;
	}
	
	.input-group::after {
		position: absolute;
		right: 0;
		bottom: 0;
		left: 0;
		height: 1px;
		content: '';
		-webkit-transform: scaleY(.5);
		transform: scaleY(.5);
		background-color: #c8c7cc;
	}
	
	.input-row {
		display: flex;
		flex-direction: row;
		position: relative;
		/* font-size: 18px; */
		height: 40px;
		line-height: 40px;
	}
	
	.input-row .title {
		width: 70px;
		padding-left: 15px;
	}
	
	.input-row.border::after {
		position: absolute;
		right: 0;
		bottom: 0;
		left: 8px;
		height: 1px;
		content: '';
		-webkit-transform: scaleY(.5);
		transform: scaleY(.5);
		background-color: #c8c7cc;
	}
	
	.btn-row {
		margin-top: 25px;
		padding: 10px;
	}
	
	.action-row {
		display: flex;
		flex-direction: row;
		justify-content: center;
	}
	
	.action-row navigator {
		color: #007aff;
		padding: 0 10px;
	}
</style>
