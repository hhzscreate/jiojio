<template>
	<view class="container">
		<view class="address-form">
			<list-cell padding="30rpx">
				<view class="form-item">
					<image :src="url" mode="aspectFill"></image>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">用户名</view>
					<input type="text" v-model="username"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">生日</view>
					<input type="text" v-model="birthday"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">电话</view>
					<input type="text" v-model="telephone"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
	
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">头像图片</view>
					<input type="text" v-model="url" placeholder-class="placeholder"/>
				</view>
			</list-cell>
		</view>
		
		<view class="save-btn" @tap="setnewmenu" >
			<button type="info">确认修改</button>
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
				username:'',
				birthday:'',
				telephone:'',
				url:'',
				id:''
			}
		},
		onLoad:function(e){
			// var temp=e.newsid.img;
			console.log(e)
			this.username=e.username;
			this.birthday=e.birthday;
			this.telephone=e.telephone;
			this.url=e.url;
			this.id=e.id;
		},
		methods: {
				radioChange(e){
					this.support_takeaway=e.detail.value;
				},
				radioChange2(e){
					this.is_single=e.detail.value;
				},
				setnewmenu(){
					uni.request({
						url: 'http://8.142.82.195/alteruser',
						method: 'GET',
						data: {
							'id':this.id,
							'url':this.url,
							'telephone':this.telephone,
							'birthday':this.birthday,
							'username':this.username
						},
						success: res => {this.message=res.data.msg;console.log(this.message)
						uni.showToast({
							title: this.message,
							duration: 2000
						});
						},
						fail: () => {
							uni.showToast({
								title: "网络有问题！！",
								duration: 2000
							});
						},
						complete: () => {}
					});
					
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
