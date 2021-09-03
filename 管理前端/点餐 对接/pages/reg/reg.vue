<template>
	<view class="content">
		
		<view class="input-group">
			<view class="input-row border">
				<text class="title">账号：</text>
				<m-input type="password" displayable v-model="user" placeholder="请输入账号"></m-input>
			</view>
			<view class="input-row border">
				<text class="title">密码：</text>
				<m-input type="password" displayable v-model="password" placeholder="请输入密码"></m-input>
			</view>
			
			
		</view>
		
		<view class="btn-row">
			<button type="primary" class="primary" :loading="loginBtnLoading" @tap="bindLogin">登录</button>
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
		data() {
			return {
				user: '',
				password:''
			}
		},
		methods:{
		bindLogin(){
						uni.request({
							url: 'http://8.142.82.195/register',
							method: 'GET',
							data: { username: this.user ,
							password:this.password},
							success: res => {console.log(res)},
							fail: () => {},
							complete: () => {}
						});
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
