<!-- 这里只要按了保存无论先生女士都会变成女士！！！ -->
<template>
	<view class="container">
		<view class="address-form">
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">联系人</view>
					<input type="text" v-model="form.name" placeholder="请填写收货人的姓名" placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">性别</view>
					<view class="radio" @tap="form.gender = !form.gender">
						<image :src="form.gender ? '/static/images/common/gouxuankuang.png' : '/static/images/common/round-black-selected.png'"></image>
						<view>先生</view>
					</view>
					<view class="radio" @tap="form.gender = !form.gender">
						<image :src="!form.gender ? '/static/images/common/gouxuankuang.png' : '/static/images/common/round-black-selected.png'"></image>
						<view>女士</view>
					</view>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">手机号</view>
					<input type="text" v-model="form.phone" placeholder="请填写收货手机号码" placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">收货地址</view>
					<input type="text" @tap="chooseLocation" v-model="form.address" placeholder="点击选择" placeholder-class="placeholder"/>
					<image src="/static/images/common/icon_jump_black3.png" class="jump-icon"></image>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">门牌号</view>
					<!-- v-model的意思是输入的传到form.description中去 -->
					<input type="text" v-model="form.description" placeholder="例:B座6楼606室" placeholder-class="placeholder"/>
				</view>
			</list-cell>
			
			<list-cell padding="30rpx" last>
				<view class="form-item">
					<view class="radio" @tap="form.is_default = !form.is_default">
						<image :src="!form.is_default ? '/static/images/common/gouxuankuang.png' : '/static/images/common/round-black-selected.png'"></image>
						<view>设为默认地址</view>
					</view>
				</view>
			</list-cell>
		</view>
		
		<view class="save-btn">
			<button type="info" @tap="saveform">保存</button>
		</view>
		
		<view class="save-btn">
			<button type="info" @tap="deleteform">删除</button>
		</view>
		
	</view>
</template>

<script>
	//用到了listCell
	import listCell from '@/components/list-cell/list-cell.vue'
	
	export default {
		components: {
			listCell
		},
		data() {
			return {
				 form: {
				}
				
			}
		},
		//会传入参数来进行选择用哪条数据初始化
		async onLoad({id}) {
			if(id) {
				const res=await this.$myRequest({
					url:'/getadresstest/',
					data:{
						user_id:getApp().globalData.openId,
						id:id
					}
				})
				this.form=res.data.data
				// console.log(res.data.data)
				//console.log(this.form)
			}
		},
		
		methods: {
			chooseLocation() {
				uni.chooseLocation({
					success: res => {
						const {errMsg, address, latitude, longitude, name} = res
						if(errMsg === "chooseLocation:ok") {
							this.form = Object.assign(
								this.form, 
								{complete_address: address, latitude, longitude, address: name},
							)
						}
					}
				})
			},
			
			async saveform(){//保存数据并跳转
				if(this.form.gender){
					this.form.gender=1
				}
				else{
					this.form.gender=0
				}
				
				if(this.form.is_default){
					this.form.is_default=1
				}
				else{
					this.form.is_default=0
				}
			
				const res=await this.$myRequest({
					url:'/setadresstest/',
					data:{
						"id": this.form.id,//去寻找需要
						"user_id": this.form.user_id, //同上
						"name": this.form.name,
						"phone": this.form.phone,
						"address": this.form.address,
						"complete_address": this.form.complete_address,
						"description": this.form.description,
						"latitude": this.form.latitude,
						"longitude": this.form.longitude,
						"gender_0": this.form.gender,
						"is_default": this.form.is_default,
						
					}
				})
				// console.log(res.data.data)
				//console.log("成功")
				//console.log(this.form.gender)
			
				//返回上一级页面
				uni.navigateBack({
					url: '/pages/addresses/addresses'
				})
			},
			
			//删除地址，需要访问数据库并删除！
			async deleteform(){
						
				const res=await this.$myRequest({
					url:'/deleteadresstest/',
					data:{
						"id": this.form.id,//去寻找需要
						"user_id": this.form.user_id, //同上					
					}
				})
							
				//返回上一级页面
				uni.navigateBack({
					url: '/pages/addresses/addresses'
				})
			}
		}
		
	}
</script>

<style lang="scss" scoped>
.address-form {
	margin-top: 20rpx;
	
	.form-item {
		width: 100%;
		display: flex;
		align-items: center;
		
		.label {
			width: 160rpx;
		}
		
		input {
			flex: 1;
		}
		
		.jump-icon {
			width: 30rpx;
			height: 48rpx;
		}
		
		.radio {
			display: flex;
			margin-right: 50rpx;
			image {
				width: 40rpx;
				height: 40rpx;
				margin-right: 20rpx;
			}
		}
	}
}

.save-btn {
	padding: 0 30rpx;
	margin-top: 60rpx;
	
	button {
		width: 100%;
		font-size: $font-size-extra-lg;
	}
}
</style>
